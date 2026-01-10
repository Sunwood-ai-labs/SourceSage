# Project: sveltekit-starter-gh-pages

```plaintext
OS: nt
Directory: D:\Prj\CC_WorkSpace\sveltekit-starter-gh-pages

├── .github/
│   └── workflows/
│       └── deploy.yml
├── .vscode/
│   ├── extensions.json
│   └── settings.json
├── src/
│   ├── lib/
│   │   ├── components/
│   │   │   ├── Counter.svelte
│   │   │   └── PathDisplay.svelte
│   │   └── index.ts
│   ├── routes/
│   │   ├── about/
│   │   │   └── +page.svelte
│   │   ├── demo/
│   │   │   └── +page.svelte
│   │   ├── +error.svelte
│   │   ├── +layout.js
│   │   ├── +layout.svelte
│   │   └── +page.svelte
│   ├── app.d.ts
│   └── app.html
├── static/
│   ├── .nojekyll
│   └── robots.txt
├── .npmrc
├── package.json
├── pnpm-workspace.yaml
├── README.md
├── svelte.config.js
├── tsconfig.json
└── vite.config.ts
```

## 📂 Gitリポジトリ情報

### 🌐 基本情報

- 🔗 リモートURL: https://github.com/Sunwood-ai-labs/sveltekit-starter-gh-pages.git
- 🌿 デフォルトブランチ: main
- 🎯 現在のブランチ: main
- 📅 作成日時: 2026-01-10 12:50:32
- 📈 総コミット数: 2

### 🔄 最新のコミット

- 📝 メッセージ: Fix GitHub Actions workflow: correct deploy-pages action name
- 🔍 ハッシュ: f4436a61
- 👤 作者: Maki (sunwood.ai.labs@gmail.com)
- ⏰ 日時: 2026-01-10 12:52:57

### 👥 主要コントリビューター

| 👤 名前 | 📊 コミット数 |
|---------|-------------|
| Maki | 2 |

## 📊 プロジェクト統計

- 📅 作成日時: 2026-01-10 15:36:37
- 📁 総ディレクトリ数: 10
- 📄 総ファイル数: 23
- 📏 最大深度: 3
- 📦 最大ディレクトリ:  (33 エントリ)

### 📊 ファイルサイズと行数

| ファイル | サイズ | 行数 | 言語 |
|----------|--------|------|------|
| README.md | 5.1 KB | 202 | markdown |
| src\routes\+page.svelte | 2.7 KB | 146 | plaintext |
| src\lib\components\PathDisplay.svelte | 1.8 KB | 109 | plaintext |
| src\routes\about\+page.svelte | 1.7 KB | 94 | plaintext |
| src\routes\+error.svelte | 1.4 KB | 90 | plaintext |
| src\routes\demo\+page.svelte | 1.5 KB | 90 | plaintext |
| src\lib\components\Counter.svelte | 1.1 KB | 78 | plaintext |
| .github\workflows\deploy.yml | 1.2 KB | 62 | yaml |
| svelte.config.js | 679.0 B | 27 | javascript |
| package.json | 670.0 B | 24 | json |
| tsconfig.json | 692.0 B | 20 | json |
| src\app.d.ts | 274.0 B | 13 | typescript |
| src\app.html | 286.0 B | 11 | html |
| src\routes\+layout.svelte | 196.0 B | 11 | plaintext |
| .vscode\settings.json | 210.0 B | 10 | json |
| vite.config.ts | 144.0 B | 6 | typescript |
| .vscode\extensions.json | 82.0 B | 6 | json |
| src\routes\+layout.js | 134.0 B | 3 | javascript |
| static\robots.txt | 63.0 B | 3 | plaintext |
| pnpm-workspace.yaml | 35.0 B | 2 | yaml |
| .npmrc | 19.0 B | 1 | plaintext |
| src\lib\index.ts | 75.0 B | 1 | typescript |
| static\.nojekyll | 0.0 B | 0 | plaintext |
| **合計** |  | **1009** |  |

### 📈 言語別統計

| 言語 | ファイル数 | 総行数 | 合計サイズ |
|------|------------|--------|------------|
| plaintext | 10 | 622 | 10.5 KB |
| markdown | 1 | 202 | 5.1 KB |
| yaml | 2 | 64 | 1.2 KB |
| json | 4 | 60 | 1.6 KB |
| javascript | 2 | 30 | 813.0 B |
| typescript | 3 | 20 | 493.0 B |
| html | 1 | 11 | 286.0 B |

`.npmrc`

**サイズ**: 19.0 B | **行数**: 1 行
```plaintext
engine-strict=true
```

`README.md`

**サイズ**: 5.1 KB | **行数**: 202 行
```markdown
# SvelteKit Starter for GitHub Pages

A production-ready SvelteKit starter template configured for deployment to GitHub Pages with TypeScript and pnpm.

**Live Demo:** [https://sunwood-ai-labs.github.io/sveltekit-starter-gh-pages/](https://sunwood-ai-labs.github.io/sveltekit-starter-gh-pages/)

## Features

- ✅ **SvelteKit** - Modern Svelte framework with SSG
- ✅ **TypeScript** - Full type safety
- ✅ **pnpm** - Fast, disk space efficient package manager
- ✅ **GitHub Actions** - Automated deployment pipeline
- ✅ **Static Adapter** - Optimized for GitHub Pages
- ✅ **Base Path Configuration** - Works in subdirectories
- ✅ **Demo Content** - Example pages and components

## Getting Started

### Prerequisites

- Node.js 18 or higher
- pnpm 10 or higher

### Installation

```bash
# Clone the repository
git clone https://github.com/Sunwood-ai-labs/sveltekit-starter-gh-pages.git
cd sveltekit-starter-gh-pages

# Install dependencies
pnpm install

# Start development server
pnpm dev
```

Open [http://localhost:5173](http://localhost:5173) in your browser.

## Development

```bash
# Start dev server
pnpm dev

# Build for production
pnpm build

# Preview production build
pnpm preview

# Type checking
pnpm check

# Type checking with watch mode
pnpm check:watch
```

## Deployment

This project is configured for automatic deployment to GitHub Pages via GitHub Actions.

### Initial Setup

1. **Enable GitHub Pages:**
   - Go to repository Settings > Pages
   - Source: Select "GitHub Actions"

2. **Push to main branch:**
   ```bash
   git push origin main
   ```

The GitHub Actions workflow will automatically build and deploy your site.

### Custom Repository

If you fork or clone this template for your own repository:

1. **Update `svelte.config.js`:**
   ```javascript
   paths: {
     base: process.env.NODE_ENV === 'production' ? '/your-repo-name' : ''
   }
   ```

2. **Update links in README and demo content**

## Project Structure

```
sveltekit-starter-gh-pages/
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions workflow
├── src/
│   ├── lib/
│   │   └── components/         # Reusable components
│   │       ├── Counter.svelte
│   │       └── PathDisplay.svelte
│   └── routes/
│       ├── about/              # About page
│       │   └── +page.svelte
│       ├── demo/               # Demo page
│       │   └── +page.svelte
│       ├── +error.svelte       # 404 page
│       ├── +layout.js          # Root layout config
│       └── +page.svelte        # Home page
├── static/
│   └── .nojekyll              # Bypass Jekyll processing
├── .gitignore
├── package.json
├── pnpm-lock.yaml
├── svelte.config.js           # SvelteKit configuration
├── tsconfig.json              # TypeScript configuration
└── vite.config.js             # Vite configuration
```

## Configuration

### Base Path

The project is configured to work in a subdirectory (`/sveltekit-starter-gh-pages/`) on GitHub Pages:

- **Development:** No base path (empty string)
- **Production:** `/sveltekit-starter-gh-pages/`

All internal links use the `base` import from `$app/paths`:

```svelte
<script>
  import { base } from '$app/paths';
</script>

<a href="{base}/about/">About</a>
```

### Adapter Configuration

Uses `@sveltejs/adapter-static` with:
- `fallback: '404.html'` - SPA routing support
- `precompress: false` - No precompression
- `strict: true` - All routes must be prerenderable

### Prerendering

All routes are prerendered via `src/routes/+layout.js`:

```javascript
export const prerender = true;
export const trailingSlash = 'always';
```

## Troubleshooting

### Base Path Issues

If links don't work after deployment:
1. Verify `paths.base` in `svelte.config.js` matches your repository name
2. Ensure all links use `{base}` prefix
3. Check GitHub Pages settings use "GitHub Actions" as source

### Build Failures

If the GitHub Actions workflow fails:
1. Check the workflow logs in the Actions tab
2. Verify all routes are prerenderable
3. Test locally with `pnpm build`

### 404 Errors

If you get 404 errors on GitHub Pages:
1. Ensure `.nojekyll` file exists in `static/` directory
2. Verify trailing slash is set to `'always'`
3. Check that `fallback: '404.html'` is configured

## Technology Stack

- **Framework:** [SvelteKit](https://kit.svelte.dev/)
- **Language:** [TypeScript](https://www.typescriptlang.org/)
- **Package Manager:** [pnpm](https://pnpm.io/)
- **Deployment:** [GitHub Actions](https://github.com/features/actions) + [GitHub Pages](https://pages.github.com/)
- **Adapter:** [@sveltejs/adapter-static](https://github.com/sveltejs/kit/tree/master/packages/adapter-static)

## Resources

- [SvelteKit Documentation](https://kit.svelte.dev/docs)
- [Adapter Static Documentation](https://svelte.dev/docs/kit/adapter-static)
- [GitHub Pages Documentation](https://docs.github.com/pages)
- [pnpm Documentation](https://pnpm.io/)

## License

MIT

## Contributing

Contributions welcome! Please feel free to submit a Pull Request.

---

Built with ❤️ using SvelteKit and deployed on GitHub Pages
```

`package.json`

**サイズ**: 670.0 B | **行数**: 24 行
```json
{
	"name": "sveltekit-starter-gh-pages",
	"private": true,
	"version": "0.0.1",
	"type": "module",
	"scripts": {
		"dev": "vite dev",
		"build": "vite build",
		"preview": "vite preview",
		"prepare": "svelte-kit sync || echo ''",
		"check": "svelte-kit sync && svelte-check --tsconfig ./tsconfig.json",
		"check:watch": "svelte-kit sync && svelte-check --tsconfig ./tsconfig.json --watch"
	},
	"devDependencies": {
		"@sveltejs/adapter-auto": "^7.0.0",
		"@sveltejs/adapter-static": "^3.0.10",
		"@sveltejs/kit": "^2.49.1",
		"@sveltejs/vite-plugin-svelte": "^6.2.1",
		"svelte": "^5.45.6",
		"svelte-check": "^4.3.4",
		"typescript": "^5.9.3",
		"vite": "^7.2.6"
	}
}
```

`pnpm-workspace.yaml`

**サイズ**: 35.0 B | **行数**: 2 行
```yaml
onlyBuiltDependencies:
  - esbuild
```

`svelte.config.js`

**サイズ**: 679.0 B | **行数**: 27 行
```javascript
import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://svelte.dev/docs/kit/integrations
	// for more information about preprocessors
	preprocess: vitePreprocess(),

	kit: {
		// adapter-static configuration for GitHub Pages
		adapter: adapter({
			pages: 'build',
			assets: 'build',
			fallback: '404.html',
			precompress: false,
			strict: true
		}),

		// Configure base path for GitHub Pages subdirectory
		paths: {
			base: process.env.NODE_ENV === 'production' ? '/sveltekit-starter-gh-pages' : ''
		}
	}
};

export default config;
```

`tsconfig.json`

**サイズ**: 692.0 B | **行数**: 20 行
```json
{
	"extends": "./.svelte-kit/tsconfig.json",
	"compilerOptions": {
		"rewriteRelativeImportExtensions": true,
		"allowJs": true,
		"checkJs": true,
		"esModuleInterop": true,
		"forceConsistentCasingInFileNames": true,
		"resolveJsonModule": true,
		"skipLibCheck": true,
		"sourceMap": true,
		"strict": true,
		"moduleResolution": "bundler"
	}
	// Path aliases are handled by https://svelte.dev/docs/kit/configuration#alias
	// except $lib which is handled by https://svelte.dev/docs/kit/configuration#files
	//
	// To make changes to top-level options such as include and exclude, we recommend extending
	// the generated config; see https://svelte.dev/docs/kit/configuration#typescript
}
```

`vite.config.ts`

**サイズ**: 144.0 B | **行数**: 6 行
```typescript
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()]
});
```

`.github\workflows\deploy.yml`

**サイズ**: 1.2 KB | **行数**: 62 行
```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

# Allow only one concurrent deployment
concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Install pnpm
        uses: pnpm/action-setup@v4
        with:
          version: 10

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - name: Install dependencies
        run: pnpm install --frozen-lockfile

      - name: Setup Pages
        uses: actions/configure-pages@v5

      - name: Build
        env:
          NODE_ENV: production
        run: pnpm run build

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: build

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

`.vscode\extensions.json`

**サイズ**: 82.0 B | **行数**: 6 行
```json
{
	"recommendations": [
		"svelte.svelte-vscode",
		"esbenp.prettier-vscode"
	]
}
```

`.vscode\settings.json`

**サイズ**: 210.0 B | **行数**: 10 行
```json
{
	"editor.formatOnSave": true,
	"editor.defaultFormatter": "esbenp.prettier-vscode",
	"[svelte]": {
		"editor.defaultFormatter": "svelte.svelte-vscode"
	},
	"files.associations": {
		"*.svelte": "svelte"
	}
}
```

`src\app.d.ts`

**サイズ**: 274.0 B | **行数**: 13 行
```typescript
// See https://svelte.dev/docs/kit/types#app.d.ts
// for information about these interfaces
declare global {
	namespace App {
		// interface Error {}
		// interface Locals {}
		// interface PageData {}
		// interface PageState {}
		// interface Platform {}
	}
}

export {};
```

`src\app.html`

**サイズ**: 286.0 B | **行数**: 11 行
```html
<!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		%sveltekit.head%
	</head>
	<body data-sveltekit-preload-data="hover">
		<div style="display: contents">%sveltekit.body%</div>
	</body>
</html>
```

`src\lib\index.ts`

**サイズ**: 75.0 B | **行数**: 1 行
```typescript
// place files you want to import through the `$lib` alias in this folder.
```

`src\lib\components\Counter.svelte`

**サイズ**: 1.1 KB | **行数**: 78 行
```plaintext
<script lang="ts">
	let count = 0;

	function increment() {
		count += 1;
	}

	function decrement() {
		count -= 1;
	}

	function reset() {
		count = 0;
	}
</script>

<div class="counter">
	<h3>Interactive Counter</h3>
	<div class="display">
		<span class="count">{count}</span>
	</div>
	<div class="buttons">
		<button on:click={decrement}>-</button>
		<button on:click={reset}>Reset</button>
		<button on:click={increment}>+</button>
	</div>
</div>

<style>
	.counter {
		padding: 1.5rem;
		background: white;
		border-radius: 8px;
		box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
	}

	h3 {
		margin-top: 0;
		color: #333;
	}

	.display {
		text-align: center;
		margin: 2rem 0;
	}

	.count {
		font-size: 3rem;
		font-weight: bold;
		color: #ff3e00;
	}

	.buttons {
		display: flex;
		gap: 1rem;
		justify-content: center;
	}

	button {
		padding: 0.75rem 1.5rem;
		font-size: 1.2rem;
		background: #ff3e00;
		color: white;
		border: none;
		border-radius: 4px;
		cursor: pointer;
		transition: all 0.2s;
	}

	button:hover {
		background: #cc3200;
		transform: scale(1.05);
	}

	button:active {
		transform: scale(0.95);
	}
</style>
```

`src\lib\components\PathDisplay.svelte`

**サイズ**: 1.8 KB | **行数**: 109 行
```plaintext
<script lang="ts">
	import { base } from '$app/paths';
	import { page } from '$app/stores';

	$: currentPath = $page.url.pathname;
	$: fullUrl = $page.url.href;
</script>

<div class="path-display">
	<h3>Path Configuration Status</h3>

	<div class="info-grid">
		<div class="info-item">
			<strong>Base Path:</strong>
			<code>{base || '/'}</code>
		</div>

		<div class="info-item">
			<strong>Current Path:</strong>
			<code>{currentPath}</code>
		</div>

		<div class="info-item">
			<strong>Full URL:</strong>
			<code class="url">{fullUrl}</code>
		</div>

		<div class="info-item">
			<strong>Environment:</strong>
			<code>{import.meta.env.MODE}</code>
		</div>
	</div>

	<div class="status">
		{#if base}
			<span class="badge success">✓ Base path configured (Production mode)</span>
		{:else}
			<span class="badge info">Development mode (no base path)</span>
		{/if}
	</div>
</div>

<style>
	.path-display {
		padding: 1.5rem;
		background: white;
		border-radius: 8px;
		box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
	}

	h3 {
		margin-top: 0;
		color: #333;
	}

	.info-grid {
		display: flex;
		flex-direction: column;
		gap: 1rem;
		margin: 1rem 0;
	}

	.info-item {
		display: flex;
		flex-direction: column;
		gap: 0.25rem;
	}

	strong {
		color: #666;
		font-size: 0.9rem;
	}

	code {
		background: #f0f0f0;
		padding: 0.5rem;
		border-radius: 4px;
		font-family: 'Courier New', monospace;
		font-size: 0.9rem;
		word-break: break-all;
	}

	.url {
		font-size: 0.8rem;
	}

	.status {
		margin-top: 1rem;
		padding-top: 1rem;
		border-top: 1px solid #e0e0e0;
	}

	.badge {
		display: inline-block;
		padding: 0.5rem 1rem;
		border-radius: 4px;
		font-weight: 500;
	}

	.success {
		background: #d4edda;
		color: #155724;
	}

	.info {
		background: #d1ecf1;
		color: #0c5460;
	}
</style>
```

`src\routes\+error.svelte`

**サイズ**: 1.4 KB | **行数**: 90 行
```plaintext
<script lang="ts">
	import { page } from '$app/stores';
	import { base } from '$app/paths';
</script>

<svelte:head>
	<title>404 - Page Not Found</title>
</svelte:head>

<div class="container">
	<div class="error-content">
		<h1>404</h1>
		<h2>Page Not Found</h2>
		<p>Sorry, the page you're looking for doesn't exist.</p>

		<div class="details">
			<strong>Requested path:</strong>
			<code>{$page.url.pathname}</code>
		</div>

		<nav>
			<a href="{base}/">Go Home</a>
		</nav>
	</div>
</div>

<style>
	.container {
		min-height: 100vh;
		display: flex;
		align-items: center;
		justify-content: center;
		padding: 2rem;
		font-family: system-ui, -apple-system, sans-serif;
	}

	.error-content {
		text-align: center;
		max-width: 500px;
	}

	h1 {
		font-size: 6rem;
		color: #ff3e00;
		margin: 0;
	}

	h2 {
		font-size: 2rem;
		color: #333;
		margin: 1rem 0;
	}

	p {
		color: #666;
		font-size: 1.1rem;
	}

	.details {
		margin: 2rem 0;
		padding: 1rem;
		background: #f5f5f5;
		border-radius: 8px;
	}

	code {
		background: #e0e0e0;
		padding: 0.2rem 0.5rem;
		border-radius: 3px;
		font-family: 'Courier New', monospace;
	}

	nav {
		margin-top: 2rem;
	}

	nav a {
		display: inline-block;
		padding: 0.75rem 1.5rem;
		background: #ff3e00;
		color: white;
		text-decoration: none;
		border-radius: 4px;
		transition: background 0.2s;
	}

	nav a:hover {
		background: #cc3200;
	}
</style>
```

`src\routes\+layout.js`

**サイズ**: 134.0 B | **行数**: 3 行
```javascript
// This can be false if you're using a fallback (i.e. SPA mode)
export const prerender = true;
export const trailingSlash = 'always';
```

`src\routes\+layout.svelte`

**サイズ**: 196.0 B | **行数**: 11 行
```plaintext
<script lang="ts">
	import favicon from '$lib/assets/favicon.svg';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

{@render children()}
```

`src\routes\+page.svelte`

**サイズ**: 2.7 KB | **行数**: 146 行
```plaintext
<script>
	import { base } from '$app/paths';
	import Counter from '$lib/components/Counter.svelte';
</script>

<svelte:head>
	<title>SvelteKit Starter - GitHub Pages</title>
	<meta name="description" content="SvelteKit starter template configured for GitHub Pages deployment" />
</svelte:head>

<div class="container">
	<header>
		<h1>SvelteKit Starter for GitHub Pages</h1>
		<p class="subtitle">A production-ready template with TypeScript and pnpm</p>
	</header>

	<main>
		<section class="intro">
			<h2>Welcome!</h2>
			<p>
				This is a SvelteKit starter project configured for deployment to GitHub Pages.
				It demonstrates proper base path configuration and static site generation.
			</p>
		</section>

		<section class="demo">
			<h2>Demo Component</h2>
			<Counter />
		</section>

		<section class="features">
			<h2>Features</h2>
			<ul>
				<li>✅ SvelteKit with TypeScript</li>
				<li>✅ Static site generation with adapter-static</li>
				<li>✅ GitHub Actions workflow for automatic deployment</li>
				<li>✅ Base path configuration for subdirectory hosting</li>
				<li>✅ pnpm package manager</li>
				<li>✅ Modern Svelte 5 with runes</li>
			</ul>
		</section>

		<section class="navigation">
			<h2>Navigation Demo</h2>
			<p>Base path is correctly configured: <code>{base || '/'}</code></p>
			<nav>
				<a href="{base}/">Home</a>
				<a href="{base}/about/">About</a>
				<a href="{base}/demo/">Demo</a>
			</nav>
		</section>
	</main>

	<footer>
		<p>
			Built with SvelteKit • Deployed on GitHub Pages •
			<a href="https://github.com/Sunwood-ai-labs/sveltekit-starter-gh-pages" target="_blank" rel="noopener">
				View on GitHub
			</a>
		</p>
	</footer>
</div>

<style>
	.container {
		max-width: 800px;
		margin: 0 auto;
		padding: 2rem;
		font-family: system-ui, -apple-system, sans-serif;
	}

	header {
		text-align: center;
		margin-bottom: 3rem;
	}

	h1 {
		font-size: 2.5rem;
		color: #ff3e00;
		margin-bottom: 0.5rem;
	}

	.subtitle {
		font-size: 1.2rem;
		color: #666;
	}

	section {
		margin-bottom: 2rem;
		padding: 1.5rem;
		background: #f5f5f5;
		border-radius: 8px;
	}

	h2 {
		color: #333;
		margin-top: 0;
	}

	ul {
		list-style-position: inside;
	}

	li {
		margin: 0.5rem 0;
	}

	nav {
		display: flex;
		gap: 1rem;
		margin-top: 1rem;
		flex-wrap: wrap;
	}

	nav a {
		padding: 0.5rem 1rem;
		background: #ff3e00;
		color: white;
		text-decoration: none;
		border-radius: 4px;
		transition: background 0.2s;
	}

	nav a:hover {
		background: #cc3200;
	}

	code {
		background: #e0e0e0;
		padding: 0.2rem 0.5rem;
		border-radius: 3px;
		font-family: 'Courier New', monospace;
	}

	footer {
		text-align: center;
		margin-top: 3rem;
		padding-top: 2rem;
		border-top: 1px solid #ddd;
		color: #666;
	}

	footer a {
		color: #ff3e00;
	}
</style>
```

`src\routes\about\+page.svelte`

**サイズ**: 1.7 KB | **行数**: 94 行
```plaintext
<script>
	import { base } from '$app/paths';
</script>

<svelte:head>
	<title>About - SvelteKit Starter</title>
</svelte:head>

<div class="container">
	<h1>About This Starter</h1>

	<section>
		<h2>Purpose</h2>
		<p>
			This starter template demonstrates how to configure SvelteKit for deployment
			to GitHub Pages with proper base path handling.
		</p>
	</section>

	<section>
		<h2>Technology Stack</h2>
		<ul>
			<li><strong>Framework:</strong> SvelteKit (Static Site Generation)</li>
			<li><strong>Language:</strong> TypeScript</li>
			<li><strong>Package Manager:</strong> pnpm</li>
			<li><strong>Deployment:</strong> GitHub Actions → GitHub Pages</li>
			<li><strong>Adapter:</strong> @sveltejs/adapter-static</li>
		</ul>
	</section>

	<section>
		<h2>Configuration Highlights</h2>
		<ul>
			<li>Base path configured for subdirectory hosting</li>
			<li>Trailing slash always enabled for GitHub Pages compatibility</li>
			<li>404 fallback for SPA-style routing</li>
			<li>Prerendering enabled for all routes</li>
		</ul>
	</section>

	<nav>
		<a href="{base}/">← Back to Home</a>
	</nav>
</div>

<style>
	.container {
		max-width: 800px;
		margin: 0 auto;
		padding: 2rem;
		font-family: system-ui, -apple-system, sans-serif;
	}

	section {
		margin: 2rem 0;
		padding: 1.5rem;
		background: #f5f5f5;
		border-radius: 8px;
	}

	h1 {
		color: #ff3e00;
	}

	h2 {
		color: #333;
		margin-top: 0;
	}

	ul {
		list-style-position: inside;
	}

	li {
		margin: 0.5rem 0;
	}

	nav {
		margin-top: 2rem;
	}

	nav a {
		padding: 0.5rem 1rem;
		background: #ff3e00;
		color: white;
		text-decoration: none;
		border-radius: 4px;
		transition: background 0.2s;
	}

	nav a:hover {
		background: #cc3200;
	}
</style>
```

`src\routes\demo\+page.svelte`

**サイズ**: 1.5 KB | **行数**: 90 行
```plaintext
<script>
	import { base } from '$app/paths';
	import Counter from '$lib/components/Counter.svelte';
	import PathDisplay from '$lib/components/PathDisplay.svelte';
</script>

<svelte:head>
	<title>Demo - SvelteKit Starter</title>
</svelte:head>

<div class="container">
	<h1>Interactive Demo</h1>

	<section>
		<h2>Counter Component</h2>
		<p>A simple interactive component to demonstrate client-side reactivity:</p>
		<Counter />
	</section>

	<section>
		<h2>Path Configuration</h2>
		<p>This component displays the current base path configuration:</p>
		<PathDisplay />
	</section>

	<section>
		<h2>Navigation Test</h2>
		<p>Test that navigation works correctly with the base path:</p>
		<nav>
			<a href="{base}/">Home</a>
			<a href="{base}/about/">About</a>
			<a href="{base}/demo/">Demo (Current)</a>
		</nav>
	</section>

	<nav class="back-nav">
		<a href="{base}/">← Back to Home</a>
	</nav>
</div>

<style>
	.container {
		max-width: 800px;
		margin: 0 auto;
		padding: 2rem;
		font-family: system-ui, -apple-system, sans-serif;
	}

	h1 {
		color: #ff3e00;
	}

	section {
		margin: 2rem 0;
		padding: 1.5rem;
		background: #f5f5f5;
		border-radius: 8px;
	}

	h2 {
		color: #333;
		margin-top: 0;
	}

	nav {
		display: flex;
		gap: 1rem;
		margin-top: 1rem;
		flex-wrap: wrap;
	}

	nav a {
		padding: 0.5rem 1rem;
		background: #ff3e00;
		color: white;
		text-decoration: none;
		border-radius: 4px;
		transition: background 0.2s;
	}

	nav a:hover {
		background: #cc3200;
	}

	.back-nav {
		margin-top: 3rem;
		padding-top: 2rem;
		border-top: 1px solid #ddd;
	}
</style>
```

`static\.nojekyll`

**サイズ**: 0.0 B | **行数**: 0 行
```plaintext
(Empty file)
```

`static\robots.txt`

**サイズ**: 63.0 B | **行数**: 3 行
```plaintext
# allow crawling everything by default
User-agent: *
Disallow:
```

