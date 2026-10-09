"""Local mirror server: isolation headers, byte ranges, and engine batch I/O with GTA KURD localization."""
import argparse, gzip, io, json, mimetypes, os, re, shutil, webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit, unquote, parse_qs

BASE_DIR = Path(__file__).resolve().parent
ROOT = BASE_DIR / 'mirror' / 'playgta5.com'
ASSETS_DIR = BASE_DIR / 'assets'

mimetypes.add_type('application/wasm', '.wasm')
mimetypes.add_type('text/javascript', '.js')
mimetypes.add_type('image/webp', '.webp')
mimetypes.add_type('font/woff', '.woff')

def sync_kurdish_assets():
    """Ensure homepage.html and Kurdish title assets are present in the mirror."""
    homepage = BASE_DIR / 'homepage.html'
    if ROOT.is_dir() and homepage.is_file():
        dest_index = ROOT / 'index.html'
        try:
            shutil.copyfile(homepage, dest_index)
        except Exception:
            pass
        title_art_src = ASSETS_DIR / 'title' / 'art'
        title_art_dst = ROOT / 'b' / '8b0b5899ed' / 'title' / 'art'
        if title_art_src.is_dir() and title_art_dst.is_dir():
            for f in ['ls12_foreground_michael.webp', 'ls13_foreground.webp', 'ls5_foreground.webp']:
                src_f = title_art_src / f
                dst_f = title_art_dst / f
                if src_f.is_file():
                    try:
                        shutil.copyfile(src_f, dst_f)
                    except Exception:
                        pass

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.byte_range = None
        doc_root = str(ROOT) if ROOT.is_dir() else str(BASE_DIR)
        super().__init__(*args, directory=doc_root, **kwargs)

    def end_headers(self):
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        self.send_header('Cross-Origin-Resource-Policy', 'same-origin')
        self.send_header('Accept-Ranges', 'bytes')
        super().end_headers()

    def translate_path(self, path):
        clean_path = urlsplit(path).path
        if clean_path in ('/', '/index.html', '/homepage.html'):
            homepage = BASE_DIR / 'homepage.html'
            if homepage.is_file():
                return str(homepage)
        # Check title asset fallback
        if clean_path.startswith('/b/8b0b5899ed/title/'):
            rel = clean_path[len('/b/8b0b5899ed/title/'):]
            asset_fallback = ASSETS_DIR / 'title' / rel
            if ROOT.is_dir():
                target = ROOT / 'b' / '8b0b5899ed' / 'title' / rel
                if target.is_file():
                    return str(target)
            if asset_fallback.is_file():
                return str(asset_fallback)
        return super().translate_path(path)

    def send_head(self):
        if not self.headers.get('Range'):
            return super().send_head()
        path = Path(self.translate_path(self.path))
        if not path.is_file():
            self.send_error(404)
            return None
        size = path.stat().st_size
        match = re.fullmatch(r'bytes=(\d*)-(\d*)', self.headers['Range'])
        if not match or not any(match.groups()):
            self.send_error(416)
            return None
        start = int(match[1]) if match[1] else max(0, size - int(match[2]))
        end = min(size - 1, int(match[2])) if match[1] and match[2] else size - 1
        if start >= size or end < start:
            self.send_response(416)
            self.send_header('Content-Range', 'bytes */%d' % size)
            self.send_header('Content-Length', '0')
            self.end_headers()
            return None
        self.byte_range = (start, end)
        self.send_response(206)
        self.send_header('Content-Type', self.guess_type(str(path)))
        self.send_header('Content-Range', 'bytes %d-%d/%d' % (start, end, size))
        self.send_header('Content-Length', str(end - start + 1))
        self.end_headers()
        source = path.open('rb')
        source.seek(start)
        return source

    def copyfile(self, source, outputfile):
        if self.byte_range is None:
            return super().copyfile(source, outputfile)
        remaining = self.byte_range[1] - self.byte_range[0] + 1
        while remaining:
            chunk = source.read(min(1024 * 1024, remaining))
            if not chunk:
                break
            outputfile.write(chunk)
            remaining -= len(chunk)

    def do_POST(self):
        url = urlsplit(self.path)
        if url.path != '/data/batch':
            self.send_error(404)
            return
        length = int(self.headers.get('Content-Length', '0'))
        if length > 1024 * 1024:
            self.send_error(413)
            return
        try:
            runs = json.loads(self.rfile.read(length))
            if not isinstance(runs, list) or len(runs) > 1000:
                raise ValueError('invalid batch')
            selected = []
            data_root = (ROOT / 'data').resolve()
            for name, start, end in runs:
                file = (data_root / name).resolve()
                if not file.is_relative_to(data_root) or start < 0 or end < start:
                    raise ValueError('invalid file/range')
                selected.append((file, start, max(0, min(end + 1, file.stat().st_size) - start)))
            total = sum(n for _, _, n in selected)
            if total > 64 * 1024 * 1024:
                raise ValueError('batch exceeds 64 MiB')
            output = io.BytesIO()
            for file, start, n in selected:
                with file.open('rb') as source:
                    source.seek(start)
                    output.write(source.read(n))
            body = output.getvalue()
            compressed = parse_qs(url.query).get('gz') == ['1']
            if compressed:
                body = gzip.compress(body, compresslevel=1)
            self.send_response(200)
            self.send_header('Content-Type', 'application/octet-stream')
            self.send_header('Content-Length', str(len(body)))
            self.send_header('X-Run-Lengths', ','.join(str(n) for _, _, n in selected))
            if compressed:
                self.send_header('Content-Encoding', 'gzip')
            self.end_headers()
            self.wfile.write(body)
        except Exception:
            self.send_error(400)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Serve local GTA KURD game files with byte ranges and COOP/COEP.')
    parser.add_argument('--port', type=int, default=8000, help='Port to listen on (default 8000)')
    parser.add_argument('--open', action='store_true', help='Open browser when server starts')
    options = parser.parse_args()

    sync_kurdish_assets()
    url = f'http://localhost:{options.port}/'
    print(f'GTA KURD Server started: {url} (Ctrl+C to stop)')
    if options.open:
        webbrowser.open(url)

    server = ThreadingHTTPServer(('127.0.0.1', options.port), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\\nShutting down server...')
        server.shutdown()
