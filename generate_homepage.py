# -*- coding: utf-8 -*-
"""
Generates Kurdish Sorani localized homepage.html for playgta5.
"""
import os, sys, shutil

TARGET = r"C:\Users\TOTAL TECH\Desktop\My Ai project\playgta5\homepage.html"
BACKUP = r"C:\Users\TOTAL TECH\Desktop\My Ai project\playgta5\homepage.html.bak"

if not os.path.exists(BACKUP):
    shutil.copyfile(TARGET, BACKUP)

with open(BACKUP, "r", encoding="utf-8") as f:
    orig = f.read()

# 1. Update <title>
orig = orig.replace("<title>game</title>", "<title>GTA V - زمانی کوردی (سۆرانی)</title>")

# 2. Add Google font Vazirmatn and CSS styles for Kurdish RTL and HUD elements
kurdish_css = """
	/* Google Font Vazirmatn for authentic Kurdish Sorani typography */
	@import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700;800;900&display=swap');

	/* Kurdish Typography & RTL overrides */
	body.lang-ckb,
	.lang-ckb #ls-stage,
	.lang-ckb #modes button,
	.lang-ckb #label,
	.lang-ckb #hud,
	.lang-ckb .ckb-font {
		font-family: 'Vazirmatn', 'Segoe UI', Tahoma, Arial, sans-serif !important;
	}
	body.lang-ckb #ls-stage {
		direction: rtl;
	}
	body.lang-ckb #ls-bars {
		left: 96px;
		right: auto;
		direction: rtl;
	}
	body.lang-ckb #ls-logo {
		right: 95px;
		left: auto;
	}
	body.lang-ckb #modes {
		direction: rtl;
	}
	body.lang-ckb .ls-key {
		margin-left: 0;
		margin-right: 5px;
	}
	body.lang-ckb #pct {
		margin-left: 0;
		margin-right: 15px;
	}

	/* Floating Top Bar: Language & Kurdish HUD Guide */
	#ckb-top-bar {
		position: fixed;
		top: 14px;
		right: 16px;
		z-index: 1000;
		display: flex;
		gap: 10px;
		align-items: center;
		direction: rtl;
	}
	.ckb-pill-btn {
		display: inline-flex;
		align-items: center;
		gap: 7px;
		height: 32px;
		padding: 0 14px;
		background: rgba(14, 18, 26, 0.88);
		backdrop-filter: blur(16px);
		-webkit-backdrop-filter: blur(16px);
		border: 1px solid rgba(255, 255, 255, 0.16);
		border-radius: 999px;
		color: #f8fafc;
		font: 600 12px/1 'Vazirmatn', 'Segoe UI', Tahoma, sans-serif;
		cursor: pointer;
		box-shadow: 0 4px 18px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(0, 0, 0, 0.6);
		transition: all .2s cubic-bezier(.16, 1, .3, 1);
		user-select: none;
	}
	.ckb-pill-btn:hover {
		background: rgba(24, 30, 42, 0.95);
		border-color: #f59e0b;
		color: #fbbf24;
		transform: translateY(-1px);
		box-shadow: 0 6px 20px rgba(245, 158, 11, 0.25);
	}
	.ckb-pill-btn:active {
		transform: translateY(0);
	}
	.ckb-pill-btn svg {
		width: 15px;
		height: 15px;
		stroke: currentColor;
		flex-shrink: 0;
	}

	/* Kurdish Tactical In-Game Guide Modal */
	#ckb-guide-modal {
		display: none;
		position: fixed;
		inset: 0;
		z-index: 2000;
		background: rgba(0, 0, 0, 0.75);
		backdrop-filter: blur(10px);
		-webkit-backdrop-filter: blur(10px);
		align-items: center;
		justify-content: center;
	}
	#ckb-guide-modal.open {
		display: flex;
	}
	.ckb-modal-box {
		width: 780px;
		max-width: 94vw;
		max-height: 86vh;
		background: #0d1017;
		border: 1px solid rgba(245, 158, 11, 0.3);
		border-radius: 14px;
		box-shadow: 0 25px 65px rgba(0, 0, 0, 0.85), 0 0 40px rgba(245, 158, 11, 0.1);
		display: flex;
		flex-direction: column;
		overflow: hidden;
		color: #e2e8f0;
		font-family: 'Vazirmatn', 'Segoe UI', Tahoma, sans-serif;
		direction: rtl;
		animation: ckbModalIn .22s cubic-bezier(.16, 1, .3, 1);
	}
	@keyframes ckbModalIn {
		from { opacity: 0; transform: scale(.96) translateY(12px); }
		to { opacity: 1; transform: scale(1) translateY(0); }
	}
	.ckb-modal-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding: 16px 22px;
		background: rgba(18, 23, 32, 0.95);
		border-bottom: 1px solid rgba(255, 255, 255, 0.08);
	}
	.ckb-modal-title {
		font-size: 16px;
		font-weight: 700;
		color: #fbbf24;
		display: flex;
		align-items: center;
		gap: 10px;
	}
	.ckb-modal-close {
		background: none;
		border: 0;
		color: #94a3b8;
		width: 32px;
		height: 32px;
		display: flex;
		align-items: center;
		justify-content: center;
		cursor: pointer;
		border-radius: 6px;
		transition: all .15s;
	}
	.ckb-modal-close:hover {
		color: #fff;
		background: rgba(255, 255, 255, 0.1);
	}
	.ckb-modal-close svg {
		width: 18px;
		height: 18px;
		stroke: currentColor;
	}
	.ckb-tabs {
		display: flex;
		background: #090c10;
		border-bottom: 1px solid rgba(255, 255, 255, 0.06);
		padding: 4px 18px 0;
		gap: 8px;
	}
	.ckb-tab-btn {
		background: none;
		border: none;
		padding: 10px 18px;
		color: #94a3b8;
		font: 600 13px 'Vazirmatn', 'Segoe UI', Tahoma, sans-serif;
		cursor: pointer;
		border-bottom: 2px solid transparent;
		transition: all .2s;
		display: flex;
		align-items: center;
		gap: 7px;
	}
	.ckb-tab-btn svg {
		width: 14px;
		height: 14px;
		stroke: currentColor;
	}
	.ckb-tab-btn:hover {
		color: #e2e8f0;
	}
	.ckb-tab-btn.active {
		color: #fbbf24;
		border-bottom-color: #fbbf24;
	}
	.ckb-tab-content {
		flex: 1;
		overflow-y: auto;
		padding: 22px;
	}
	.ckb-grid {
		display: grid;
		grid-template-columns: repeat(auto-fill, minmax(330px, 1fr));
		gap: 10px;
	}
	.ckb-card {
		display: flex;
		align-items: center;
		justify-content: space-between;
		background: rgba(255, 255, 255, 0.03);
		border: 1px solid rgba(255, 255, 255, 0.06);
		border-radius: 8px;
		padding: 9px 14px;
		transition: border-color .15s, background .15s;
	}
	.ckb-card:hover {
		border-color: rgba(245, 158, 11, 0.35);
		background: rgba(245, 158, 11, 0.04);
	}
	.ckb-badge {
		display: inline-flex;
		align-items: center;
		justify-content: center;
		min-width: 24px;
		height: 22px;
		padding: 0 8px;
		background: #1e2532;
		border: 1px solid rgba(255, 255, 255, 0.2);
		border-radius: 4px;
		color: #fbbf24;
		font: 700 11px monospace;
		box-shadow: 0 2px 4px rgba(0,0,0,0.4);
	}
	.ckb-desc {
		font-size: 13px;
		color: #cbd5e1;
		text-align: right;
	}
	.ckb-mission-box {
		background: rgba(255, 255, 255, 0.02);
		border: 1px solid rgba(255, 255, 255, 0.07);
		border-radius: 10px;
		padding: 14px 18px;
		margin-bottom: 12px;
	}
	.ckb-mission-header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-bottom: 8px;
	}
	.ckb-mission-title {
		font-weight: 700;
		font-size: 14px;
		color: #10b981;
	}
	.ckb-mission-body {
		font-size: 13px;
		line-height: 1.65;
		color: #94a3b8;
	}

	/* In-Game Subtitle HUD banner */
	#ckb-ingame-hud {
		position: fixed;
		bottom: 24px;
		left: 50%;
		transform: translateX(-50%);
		z-index: 100;
		background: rgba(11, 14, 20, 0.9);
		backdrop-filter: blur(12px);
		border: 1px solid rgba(245, 158, 11, 0.35);
		border-radius: 8px;
		padding: 8px 20px;
		color: #fef08a;
		font: 600 14px/1.4 'Vazirmatn', 'Segoe UI', Tahoma, sans-serif;
		text-shadow: 0 1px 3px rgba(0,0,0,0.8);
		box-shadow: 0 8px 24px rgba(0,0,0,0.6);
		direction: rtl;
		display: none;
		pointer-events: none;
		text-align: center;
		max-width: 80vw;
	}
"""

orig = orig.replace("</style>", kurdish_css + "\n</style>")

# 3. Add top-bar, modal, and HUD HTML elements right after <body>
kurdish_dom = """
<div id="ckb-top-bar">
	<button id="ckb-lang-toggle" class="ckb-pill-btn" title="گۆڕینی زمان">
		<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
		<span id="ckb-lang-label">کوردی (سۆرانی)</span>
	</button>
	<button id="ckb-guide-toggle" class="ckb-pill-btn" title="ڕێبەری کۆنتڕۆڵ (K)">
		<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="6" width="20" height="12" rx="4"/><path d="M6 12h4m-2-2v4m9-2h.01m3-2h.01"/></svg>
		<span id="ckb-guide-label">ڕێبەری کوردی (K)</span>
	</button>
</div>

<div id="ckb-guide-modal">
	<div class="ckb-modal-box">
		<div class="ckb-modal-header">
			<div class="ckb-modal-title">
				<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="6" width="20" height="12" rx="4"/><path d="M6 12h4m-2-2v4m9-2h.01m3-2h.01"/></svg>
				<span id="ckb-modal-title-text">ڕێبەری کۆنتڕۆڵ و یارمەتیدەری یاری GTA V</span>
			</div>
			<button id="ckb-modal-close-btn" class="ckb-modal-close" title="داخستن">
				<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
			</button>
		</div>
		<div class="ckb-tabs">
			<button class="ckb-tab-btn active" data-tab="controls">
				<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="6" width="20" height="12" rx="4"/><path d="M6 12h4m-2-2v4"/></svg>
				<span id="ckb-tab-ctrl-title">کۆنتڕۆڵەکانی یاری</span>
			</button>
			<button class="ckb-tab-btn" data-tab="missions">
				<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
				<span id="ckb-tab-miss-title">چیرۆک و ئەرکەکان</span>
			</button>
			<button class="ckb-tab-btn" data-tab="cheats">
				<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
				<span id="ckb-tab-cht-title">کۆدە نهێنییەکان</span>
			</button>
		</div>
		<div class="ckb-tab-content" id="ckb-tab-controls-pane">
			<div class="ckb-grid" id="ckb-controls-list"></div>
		</div>
		<div class="ckb-tab-content" id="ckb-tab-missions-pane" style="display:none">
			<div id="ckb-missions-list"></div>
		</div>
		<div class="ckb-tab-content" id="ckb-tab-cheats-pane" style="display:none">
			<div class="ckb-grid" id="ckb-cheats-list"></div>
		</div>
	</div>
</div>

<div id="ckb-ingame-hud"></div>
"""

orig = orig.replace("<body>\n<canvas", "<body>\n" + kurdish_dom + "\n<canvas")

# 4. In <script type="module">: replace ACTS, LOADING, showModes, key listeners, labels
# Locate start choice section
start_anchor = "let startMode = q.get('mode') === 'story' ? 1 : q.get('mode') === 'sandbox' ? (q.get('map') === 'env_test' ? 3 : 2) : 0;"

kurdish_localization_js = """// ---- Kurdish Sorani Localization System (کوردیی سۆرانی) ----------------------------------------------------
let currentLang = localStorage.getItem('gta_lang') || 'ckb'; // Default to Kurdish Sorani!
if (currentLang === 'ckb') {
	document.body.classList.add('lang-ckb');
	document.documentElement.lang = 'ckb';
	document.documentElement.dir = 'rtl';
}

const I18N = {
	ckb: {
		langName: 'کوردی (سۆرانی)',
		guideLabel: 'ڕێبەری کوردی (K)',
		modalTitle: 'ڕێبەری کۆنتڕۆڵ و یارمەتیدەری یاری GTA V',
		tabControls: 'کۆنتڕۆڵەکانی یاری',
		tabMissions: 'چیرۆک و ئەرکەکان',
		tabCheats: 'کۆدە نهێنییەکان',
		starting: 'دەستپێکردن...',
		preparingShaders: 'ئامادەکردنی شه‌یده‌ره‌كان...',
		chooseMap: 'بۆ بەردەوامبوون نەخشەیەک دیاری بکە',
		chooseMode: 'بۆ بەردەوامبوون مۆدی چیرۆک یاخود مۆدی ئازاد دیاری بکە',
		gameData: 'داتای یاری: ',
		mbSec: ' مێگابایت/چرکە',
		noProgress: 'هیچ پێشکەوتنێک نییە بۆ ماوەی {quiet} چرکە (دوایین هەنگاو: {lastStep}): لەوانەیە ڕامی ئامێرەکەت پڕ بووبێت. پەڕەکانی تر دابخە یان نوێی بکەرەوە.',
		captureMouse: 'کلیک لەسەر یاری بکە بۆ کۆنتڕۆڵی ماوس (Esc بۆ بەردان، Shift+P بۆ دۆخی کیبۆرد، = بۆ نیشاندانی FPS)',
		notIsolated: 'پەڕەکە لە دۆخی cross-origin isolated نییە: لە ڕێگەی localhost یان https بیکەرەوە',
		lowMemory: 'ئامێری خاوەن ڕامی کەم ({mem} GB): پەڕەکانی تر دابخە بۆ کارکردنی بێ کێشە.',
		gpuLost: 'دەزگای گرافیک پچڕا ({code}): شاشەکە ڕەش دەمێنێتەوە. لاپەڕەکە نوێ بکەرەوە.',
		gameStopped: 'یارییەکە وەستا ({kind}): ',
		oomHint: ' - پێدەچێت کێشەی کەمیی ڕام بێت: پەڕەکانی تر دابخە و نوێی بکەرەوە.',
		reloadHint: ' - لاپەڕەکە نوێ بکەرەوە.',
		acts: {
			back: ['گەڕانەوە', 'Backspace'],
			map5: ['نەخشەی لۆس سانتۆس (GTA V)', '5'],
			map6: ['نەخشەی تاقیکاری (GTA VI)', '6'],
			sandbox: ['مۆدی ئازاد', 'Space'],
			story: ['مۆدی چیرۆک', 'Enter'],
		},
		loading: {
			1: 'بارکردنی مۆدی چیرۆک...',
			2: 'بارکردنی مۆدی ئازاد: نەخشەی لۆس سانتۆس...',
			3: 'بارکردنی مۆدی ئازاد: نەخشەی تاقیکاری...'
		},
		controls: [
			{ key: 'W, A, S, D', desc: 'جووڵەکردن و ڕۆیشتن (بەرەو پێش، دواوە، چەپ، ڕاست)' },
			{ key: 'Shift (چەپ)', desc: 'ڕاکردنی زۆر خێرا (Sprint)' },
			{ key: 'Space', desc: 'بازدان / سەرکەوتن بەسەر دیوار و بەربەستەکان' },
			{ key: 'F / Enter', desc: 'سواربوون و دابەزین لە ئۆتۆمبێل، ماتۆڕ یان فڕۆکە' },
			{ key: 'کلیکی چەپ', desc: 'تەقەکردن، شەڕکردن بە مشت یان فڕێدانی بۆمب' },
			{ key: 'کلیکی ڕاست', desc: 'نیشانگرتن بە چەک (Aim)' },
			{ key: 'Tab', desc: 'کردنەوەی مینیوی دەورەیی چەکەکان (Weapon Wheel)' },
			{ key: 'Q', desc: 'سەنگەرگرتن لە پشت دیوار و ستوونەکان (Cover)' },
			{ key: 'تیر بۆ سەرەوە (↑)', desc: 'دەرکردنی مۆبایلی زیرەک (Phone)' },
			{ key: 'R', desc: 'پڕکردنەوەی فیشەکی چەک (Reload)' },
			{ key: 'E', desc: 'دەنگی هۆڕنی ئۆتۆمبێل / کارلێککردن لەگەڵ شتەکان' },
			{ key: 'Space (لە ئۆتۆمبێل)', desc: 'برێکی دەستی (Handbrake) بۆ خلیسکاندن' },
			{ key: 'Ctrl (چەپ)', desc: 'دۆخی خشین و خۆشاردنەوە (Stealth Mode)' },
			{ key: 'Q (لە ئۆتۆمبێل)', desc: 'گۆڕینی ئیستگەی ڕادیۆی ئۆتۆمبێل' },
			{ key: 'Alt (چەپ)', desc: 'گۆڕینی کەسایەتی (مایکڵ، فرانکڵین، تریڤۆر)' },
			{ key: 'V', desc: 'گۆڕینی کامێرا (کەسایەتی یەکەم یان سێیەم)' },
			{ key: 'Esc / P', desc: 'ڕاگرتنی کاتیی یاری و بینینی نەخشەی شار' },
			{ key: '=', desc: 'نیشاندان یان شاردنەوەی ڕێژەی فرەیم (FPS)' },
			{ key: 'K', desc: 'کردنەوە یان داخستنی ئەم ڕێبەرە کوردییە' }
		],
		missions: [
			{
				title: 'ئەرکی یەکەم: پێشەکیی لودندۆرف (Prologue)',
				body: 'لە بانکی لودندۆرف، بە بۆمبی دەستی دەرگای خەزێنەی بانکەکە بتەقێنەرەوە. پارەکە کۆبکەرەوە و لەگەڵ هاوڕێکانت ڕابکە بەرەو دەرەوە. کاتێک پۆلیس دەورەتان دەدات لە پشت ستوونەکان بە کلیلی Q سەنگەر بگرە و بە کلیکی ڕاست نیشان بگرە و تەقەیان لێ بکە تا دەگەیتە ئۆتۆمبێلی هەڵاتن.'
			},
			{
				title: 'ئەرکی دووەم: فرانکڵین و لامار (Franklin & Lamar)',
				body: 'سەربکەوە ناو یەکێک لە دوو ئۆتۆمبێلە سوپەرسپۆرتەکان، بە خێرایی شوێن لامار بکەوە بەناو شەقامەکانی لۆس سانتۆسدا. لە پێچە تیژەکاندا برێکی دەستی (Space) بەکاربهێنە تاکو دەگەیتە پێشانگای ئۆتۆمبێلی سیمۆن.'
			},
			{
				title: 'ئەرکی سێیەم: وەرگرتنەوەی شتومەک (Repossession)',
				body: 'لەگەڵ لامار بچۆ بۆ ڤیسپوچی بۆ هێنانەوەی ماتۆڕە سەوزەکە. بە چەک تەقە لە چەتەکانی ڤاگۆس بکە و شوێن ماتۆڕە هەڵاتووەکە بکەوە بەناو شاردا تا دەیگریتەوە.'
			}
		],
		cheats: [
			{ key: 'TURTLE', desc: 'تەندروستی تەواو و قەڵغانی گوللەبەند (Max Health & Armor)' },
			{ key: 'TOOLUP', desc: 'دەستکەوتنی هەموو چەکەکان و فیشەکی زۆر (All Weapons)' },
			{ key: 'PAINKILLER', desc: 'نەمر بوون بۆ ماوەی ٥ خولەک (Invincibility)' },
			{ key: 'LAWYERUP', desc: 'کەمکردنەوەی ئەستێرەی پۆلیس (Lower Wanted Level)' },
			{ key: 'FUGITIVE', desc: 'زیادکردنی ئەستێرەی پۆلیس (Raise Wanted Level)' },
			{ key: 'CATCHME', desc: 'ڕاکردنی زۆر خێرا (Fast Sprint)' },
			{ key: 'HOPTOIT', desc: 'بازدانی زۆر بەرز (Super Jump)' },
			{ key: 'SKYFALL', desc: 'فڕین و بەربوونەوە لە ئاسمانەوە (Skyfall)' },
			{ key: 'DEADEYE', desc: 'هێواشکردنەوەی کات لە کاتی نیشانگرتن (Slow-Mo Aim)' },
			{ key: 'COMET', desc: 'هێنانی ئۆتۆمبێلی وەرزشی کۆمێت (Spawn Comet)' },
			{ key: 'RAPIDGT', desc: 'هێنانی ئۆتۆمبێلی وەرزشی ڕاپید GT (Spawn Rapid GT)' },
			{ key: 'ROCKET', desc: 'هێنانی ماتۆڕی وەرزشی PCJ-600 (Spawn PCJ-600)' }
		]
	},
	en: {
		langName: 'English',
		guideLabel: 'Game Guide (K)',
		modalTitle: 'GTA V Controls & Mission Guide',
		tabControls: 'Game Controls',
		tabMissions: 'Story & Missions',
		tabCheats: 'Cheat Codes',
		starting: 'Starting...',
		preparingShaders: 'Preparing shaders',
		chooseMap: 'Choose a map to continue',
		chooseMode: 'Choose Story Mode or Sandbox Mode to continue',
		gameData: 'Game data: ',
		mbSec: ' MB/s',
		noProgress: 'No progress for {quiet} s (last step: {lastStep}): the device may be out of memory. Close other tabs, or reload.',
		captureMouse: 'click the game to capture the mouse (Esc releases it, Shift+P switches keyboard mode, = shows FPS)',
		notIsolated: 'not cross-origin isolated: open the page over https (or localhost); the server sends COOP/COEP',
		lowMemory: 'Low-memory device ({mem} GB reported): close other tabs.',
		gpuLost: 'The graphics device was lost ({code}): the screen will stay black. Reload the page.',
		gameStopped: 'The game stopped ({kind}): ',
		oomHint: ' - this looks like a lack of memory: close other tabs and reload.',
		reloadHint: ' - reload the page.',
		acts: {
			back: ['Back', 'Backspace'],
			map5: ['GTA V Map', '5'],
			map6: ['GTA VI Map', '6'],
			sandbox: ['Sandbox Mode', 'Space'],
			story: ['Story Mode', 'Enter'],
		},
		loading: {
			1: 'Loading Story Mode',
			2: 'Loading Sandbox Mode: GTA V Map',
			3: 'Loading Sandbox Mode: GTA VI Map'
		},
		controls: [
			{ key: 'W, A, S, D', desc: 'Movement (Forward, Backward, Strafe Left, Right)' },
			{ key: 'Left Shift', desc: 'Sprint / Run fast' },
			{ key: 'Space', desc: 'Jump / Climb obstacles' },
			{ key: 'F / Enter', desc: 'Enter / Exit vehicle' },
			{ key: 'Left Click', desc: 'Attack / Fire weapon' },
			{ key: 'Right Click', desc: 'Aim weapon' },
			{ key: 'Tab', desc: 'Weapon Wheel selector' },
			{ key: 'Q', desc: 'Take Cover behind walls' },
			{ key: 'Up Arrow', desc: 'Open Smartphone' },
			{ key: 'R', desc: 'Reload weapon' },
			{ key: 'E', desc: 'Horn / Context interaction' },
			{ key: 'Space (in car)', desc: 'Handbrake / Drift' },
			{ key: 'Left Ctrl', desc: 'Stealth mode' },
			{ key: 'Q (in car)', desc: 'Next radio station' },
			{ key: 'Left Alt', desc: 'Character Switch (Michael, Franklin, Trevor)' },
			{ key: 'V', desc: 'Change Camera View' },
			{ key: 'Esc / P', desc: 'Pause Menu & Map' },
			{ key: '=', desc: 'Toggle FPS Counter' },
			{ key: 'K', desc: 'Toggle this Game Guide' }
		],
		missions: [
			{
				title: 'Mission 1: Prologue (Ludendorff Bank)',
				body: 'Blow the vault door with plastic explosives, grab the cash, and take cover behind pillars (Q) when police arrive. Aim with Right Click to take them down and escape to the getaway vehicle.'
			},
			{
				title: 'Mission 2: Franklin and Lamar',
				body: 'Get into one of the sports cars and race through the streets of Los Santos following Lamar. Use the handbrake (Space) on sharp corners to reach Simeons dealership.'
			},
			{
				title: 'Mission 3: Repossession',
				body: 'Head to Vespucci with Lamar to repossess the green motorbike. Eliminate Vagos gang members and chase the fleeing bike through the city.'
			}
		],
		cheats: [
			{ key: 'TURTLE', desc: 'Max Health & Armor' },
			{ key: 'TOOLUP', desc: 'All Weapons & Full Ammo' },
			{ key: 'PAINKILLER', desc: 'Invincibility for 5 minutes' },
			{ key: 'LAWYERUP', desc: 'Lower Wanted Level' },
			{ key: 'FUGITIVE', desc: 'Raise Wanted Level' },
			{ key: 'CATCHME', desc: 'Fast Sprint' },
			{ key: 'HOPTOIT', desc: 'Super Jump' },
			{ key: 'SKYFALL', desc: 'Skyfall (Spawn high in sky)' },
			{ key: 'DEADEYE', desc: 'Slow-Motion Aiming' },
			{ key: 'COMET', desc: 'Spawn Comet Sports Car' },
			{ key: 'RAPIDGT', desc: 'Spawn Rapid GT Sports Car' },
			{ key: 'ROCKET', desc: 'Spawn PCJ-600 Motorbike' }
		]
	}
};

const KEY_CODES = {
	back: ['Backspace'],
	map5: ['Digit5', 'Numpad5'],
	map6: ['Digit6', 'Numpad6'],
	sandbox: ['Space'],
	story: ['Enter', 'NumpadEnter']
};

const setLanguage = (lang) => {
	currentLang = lang;
	localStorage.setItem('gta_lang', lang);
	const i18n = I18N[lang];
	document.documentElement.lang = lang;
	document.documentElement.dir = i18n.acts.back[0] === 'گەڕانەوە' ? 'rtl' : 'ltr';
	document.body.classList.toggle('lang-ckb', lang === 'ckb');
	
	// Update top bar labels
	document.getElementById('ckb-lang-label').textContent = i18n.langName;
	document.getElementById('ckb-guide-label').textContent = i18n.guideLabel;
	document.getElementById('ckb-modal-title-text').textContent = i18n.modalTitle;
	document.getElementById('ckb-tab-ctrl-title').textContent = i18n.tabControls;
	document.getElementById('ckb-tab-miss-title').textContent = i18n.tabMissions;
	document.getElementById('ckb-tab-cht-title').textContent = i18n.tabCheats;
	
	// Refresh guide modal contents
	renderGuideContents();
	showModes();
	
	const lbl = document.getElementById('label');
	if (lbl && !waitingChoice && lbl.textContent.includes('...')) {
		lbl.textContent = i18n.starting;
	}
};

const renderGuideContents = () => {
	const i18n = I18N[currentLang];
	const ctrlList = document.getElementById('ckb-controls-list');
	if (ctrlList) {
		ctrlList.innerHTML = i18n.controls.map(c => `
			<div class="ckb-card">
				<span class="ckb-desc">${c.desc}</span>
				<span class="ckb-badge">${c.key}</span>
			</div>
		`).join('');
	}
	const missList = document.getElementById('ckb-missions-list');
	if (missList) {
		missList.innerHTML = i18n.missions.map(m => `
			<div class="ckb-mission-box">
				<div class="ckb-mission-header">
					<span class="ckb-mission-title">${m.title}</span>
				</div>
				<div class="ckb-mission-body">${m.body}</div>
			</div>
		`).join('');
	}
	const chtList = document.getElementById('ckb-cheats-list');
	if (chtList) {
		chtList.innerHTML = i18n.cheats.map(c => `
			<div class="ckb-card">
				<span class="ckb-desc">${c.desc}</span>
				<span class="ckb-badge">${c.key}</span>
			</div>
		`).join('');
	}
};

// Guide modal interaction
const guideModal = document.getElementById('ckb-guide-modal');
const toggleGuide = () => {
	if (!guideModal) return;
	const open = guideModal.classList.toggle('open');
	if (open && document.pointerLockElement) {
		document.exitPointerLock();
	}
};
const closeGuide = () => {
	if (guideModal) guideModal.classList.remove('open');
};

document.getElementById('ckb-lang-toggle')?.addEventListener('click', () => {
	setLanguage(currentLang === 'ckb' ? 'en' : 'ckb');
});
document.getElementById('ckb-guide-toggle')?.addEventListener('click', toggleGuide);
document.getElementById('ckb-modal-close-btn')?.addEventListener('click', closeGuide);
guideModal?.addEventListener('click', (e) => {
	if (e.target === guideModal) closeGuide();
});

// Guide modal tabs
document.querySelectorAll('.ckb-tab-btn').forEach(btn => {
	btn.addEventListener('click', () => {
		document.querySelectorAll('.ckb-tab-btn').forEach(b => b.classList.remove('active'));
		btn.classList.add('active');
		const tab = btn.dataset.tab;
		document.querySelectorAll('.ckb-tab-content').forEach(p => p.style.display = 'none');
		const pane = document.getElementById('ckb-tab-' + tab + '-pane');
		if (pane) pane.style.display = 'block';
	});
});

renderGuideContents();
"""

# Find the startMode declaration line and inject Kurdish localization before it
orig = orig.replace(start_anchor, kurdish_localization_js + "\n" + start_anchor)

# Now replace ACTS and LOADING and showModes with dynamic localized versions
old_acts_block = """const ACTS = {		// button: text, key cap, key codes
	back: ['Back', 'Backspace', ['Backspace']],
	map5: ['GTA V Map', '5', ['Digit5', 'Numpad5']],
	map6: ['GTA VI Map', '6', ['Digit6', 'Numpad6']],
	sandbox: ['Sandbox Mode', 'Space', ['Space']],
	story: ['Story Mode', 'Enter', ['Enter', 'NumpadEnter']],
};
const LOADING = { 1: 'Loading Story Mode', 2: 'Loading Sandbox Mode: GTA V Map', 3: 'Loading Sandbox Mode: GTA VI Map' };
const modesEl = document.getElementById('modes'), modeButtons = [...modesEl.querySelectorAll('button')];
const isMode = (act) => act === 'story' || act === 'sandbox';
const showModes = () => {
	for (const b of modeButtons) {
		const act = b.dataset.act, loading = !pickingMap && (act === 'story' ? startMode === 1 : act === 'sandbox' && startMode >= 2);
		const text = document.createElement('span'), icon = document.createElement(loading ? 'i' : 'span');
		text.textContent = loading ? LOADING[startMode] : ACTS[act][0];
		icon.className = loading ? 'ls-spin' : 'ls-key';
		icon.textContent = loading ? '' : ACTS[act][1];
		b.replaceChildren(text, icon);
		b.style.order = loading ? 1 : 0;
		b.disabled = startCommitted;
		b.hidden = startCommitted ? !loading : pickingMap === isMode(act);		// the modes, or the map choice with Back
		b.classList.toggle('chosen', loading);
	}
	if (startMode) modesEl.classList.remove('ask');
	if (waitingChoice && !startMode) document.getElementById('label').textContent = pickingMap ? 'Choose a map to continue' : 'Choose Story Mode or Sandbox Mode to continue';
};"""

new_acts_block = """const modesEl = document.getElementById('modes'), modeButtons = [...modesEl.querySelectorAll('button')];
const isMode = (act) => act === 'story' || act === 'sandbox';
const showModes = () => {
	const i18n = I18N[currentLang] || I18N.ckb;
	for (const b of modeButtons) {
		const act = b.dataset.act, loading = !pickingMap && (act === 'story' ? startMode === 1 : act === 'sandbox' && startMode >= 2);
		const text = document.createElement('span'), icon = document.createElement(loading ? 'i' : 'span');
		text.textContent = loading ? i18n.loading[startMode] : i18n.acts[act][0];
		icon.className = loading ? 'ls-spin' : 'ls-key';
		icon.textContent = loading ? '' : i18n.acts[act][1];
		b.replaceChildren(text, icon);
		b.style.order = loading ? 1 : 0;
		b.disabled = startCommitted;
		b.hidden = startCommitted ? !loading : pickingMap === isMode(act);		// the modes, or the map choice with Back
		b.classList.toggle('chosen', loading);
	}
	if (startMode) modesEl.classList.remove('ask');
	if (waitingChoice && !startMode) document.getElementById('label').textContent = pickingMap ? i18n.chooseMap : i18n.chooseMode;
};"""

orig = orig.replace(old_acts_block, new_acts_block)

# Replace the key down listener in the start choice menu so it uses KEY_CODES
old_keydown_block = """addEventListener('keydown', (e) => {
	if (startCommitted || e.ctrlKey || e.altKey || e.metaKey || !document.getElementById('loading')) return;
	const b = modeButtons.find((x) => !x.hidden && ACTS[x.dataset.act][2].includes(e.code));
	if (!b) return;
	act(b.dataset.act);
	e.preventDefault(); e.stopImmediatePropagation();
}, { capture: true });"""

new_keydown_block = """addEventListener('keydown', (e) => {
	if (e.code === 'KeyK' && !e.ctrlKey && !e.altKey && !e.metaKey) {
		toggleGuide();
		e.preventDefault(); e.stopImmediatePropagation();
		return;
	}
	if (guideModal && guideModal.classList.contains('open') && e.code === 'Escape') {
		closeGuide();
		e.preventDefault(); e.stopImmediatePropagation();
		return;
	}
	if (startCommitted || e.ctrlKey || e.altKey || e.metaKey || !document.getElementById('loading')) return;
	const b = modeButtons.find((x) => !x.hidden && KEY_CODES[x.dataset.act] && KEY_CODES[x.dataset.act].includes(e.code));
	if (!b) return;
	act(b.dataset.act);
	e.preventDefault(); e.stopImmediatePropagation();
}, { capture: true });"""

orig = orig.replace(old_keydown_block, new_keydown_block)

# Localize progress messages
orig = orig.replace(
	"label.textContent = lastLabel = 'Preparing shaders';",
	"const _i18n = I18N[currentLang] || I18N.ckb; label.textContent = lastLabel = _i18n.preparingShaders;"
)
orig = orig.replace(
	"hud.textContent = 'click the game to capture the mouse (Esc releases it, Shift+P switches keyboard mode, = shows FPS)';",
	"const _i18n = I18N[currentLang] || I18N.ckb; hud.textContent = _i18n.captureMouse;"
)
orig = orig.replace(
	"if (dataBytes) dataEl.textContent = 'Game data: ' + (dataBytes / 1048576 | 0) + ' MB' + (speed > 1e4 ? ' (' + (speed / 1048576).toFixed(1) + ' MB/s)' : '');",
	"if (dataBytes) { const _i18n = I18N[currentLang] || I18N.ckb; dataEl.textContent = _i18n.gameData + (dataBytes / 1048576 | 0) + ' MB' + (speed > 1e4 ? ' (' + (speed / 1048576).toFixed(1) + _i18n.mbSec + ')' : ''); }"
)

# Localize initial label Starting...
orig = orig.replace('<span id="label">Starting...</span>', '<span id="label">دەستپێکردن...</span>')

# Update screen ORDERS so Franklin is first, Michael (Kurdish Char 1) is second, and Trevor (Kurdish Char 2) is third
orig = orig.replace(
	"const ORDERS = [[0, 16, 18, 3, 12, 2, 17, 10, 9, 8, 15, 6, 11, 14, 4, 7, 13], [0, 4, 6, 17, 11, 16, 18, 7, 9, 15, 3, 14, 10, 13, 2, 8, 12],\n\t\t[0, 7, 16, 14, 13, 3, 10, 2, 15, 18, 8, 9, 4, 17, 12, 6, 11], [0, 8, 18, 9, 13, 4, 11, 14, 7, 17, 6, 12, 3, 16, 2, 15, 10],\n\t\t[0, 11, 12, 7, 18, 14, 9, 13, 4, 2, 15, 11, 8, 16, 6, 3, 17], [0, 10, 16, 2, 13, 17, 8, 9, 18, 3, 12, 6, 7, 4, 14, 15, 10]];",
	"const ORDERS = [[3, 14, 15, 0, 16, 18, 2, 17, 10, 9, 8, 6, 11, 4, 7, 12, 13], [3, 14, 15, 0, 4, 6, 17, 11, 16, 18, 7, 9, 2, 8, 10, 12, 13]];"
)

with open(TARGET, "w", encoding="utf-8") as f:
    f.write(orig)

print("Generated Kurdish-localized homepage.html successfully!")
