# ThinkPage

<img src="./app-icon.svg" width="96" alt="ThinkPage Logo" />

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Live Demo](https://img.shields.io/badge/Live_Demo-thinkpage.vercel.app-blue.svg)](https://thinkpage.vercel.app)
[![Firefox Bridge Extension](https://img.shields.io/badge/Firefox_Extension-ThinkPage_Bridge-orange.svg)](https://github.com/naitiktuxx/ThinkPage-Bridge-Extension/releases)

A customizable, offline-first new tab dashboard for your browser.

> Live demo: [https://thinkpage.vercel.app](https://thinkpage.vercel.app)

---

## Screenshots

<!-- Screenshots will be added here. -->

---

## Why I made it

I like Firefox because it's open source and customizable, but I preferred the clean look of Chrome's default homepage. I wanted to make something similar while letting users choose their own search engines—like Google, Bing, DuckDuckGo, or custom providers—and customize the page layout.

I also added a glassmorphism theme option inspired by the visual style I like on macOS.

---

## Features

- **Search engine options**: Google, Bing, DuckDuckGo, and custom search engines
- **Shortcuts & web apps**: Customizable speed dial links with icon picker
- **Themes & wallpapers**: Dark, Catppuccin, and color themes, preset wallpapers, or custom image uploads
- **Glassmorphism UI**: Optional backdrop blur effects inspired by macOS
- **AI shortcuts**: Quick access to ChatGPT, Gemini and Claude etc. 
- **Image search**: Lens-style image search supporting URLs, drag-and-drop, and clipboard paste
- **Profiles**: Separate settings, history, and shortcuts for different profiles
- **Offline support**: Works offline as a Progressive Web App
- **Firefox integration**: Optional companion extension for history suggestions and tab handling

---

## Firefox Extension — ThinkPage Bridge ⭐ Recommended

The best way to use ThinkPage in Firefox is with the **[ThinkPage Bridge](https://github.com/naitiktuxx/ThinkPage-Bridge-Extension)** companion extension. It unlocks features that aren't possible from a plain web page:

- **Sets ThinkPage as your new tab page** in Firefox (and other Gecko-based browsers) natively
- **Auto-focuses the search bar** the instant a new tab opens — no clicking required
- **Syncs Firefox browsing history** into ThinkPage for real-time search suggestions
- **Instant toggle** — pause the extension from its popup to revert to Firefox's native new tab (`about:home`) at any time

### Install ThinkPage Bridge

#### Method 1 — Direct `.xpi` Install (Easiest)

1. Go to the **[Releases page](https://github.com/naitiktuxx/ThinkPage-Bridge-Extension/releases)** and download the latest `thinkpage-bridge-vX.X.X.xpi`
2. Open Firefox → `about:addons` (or `Ctrl+Shift+A` / `Cmd+Shift+A`)
3. Click the **⚙️ gear icon** → **Install Add-on From File…**
4. Select the downloaded `.xpi` file and click **Add**

#### Method 2 — Temporary (Developer Mode)

1. Download and extract the `.zip` from the **[Releases page](https://github.com/naitiktuxx/ThinkPage-Bridge-Extension/releases)**
2. Open Firefox → `about:debugging#/runtime/this-firefox`
3. Click **Load Temporary Add-on…** and select `manifest.json` inside the extracted folder

> **Note:** After installing, open a new tab — ThinkPage Bridge will automatically redirect it to [thinkpage.vercel.app](https://thinkpage.vercel.app).

---

## Privacy

ThinkPage does not include any analytics or tracking scripts. Preferences, shortcuts, and local settings are stored in your browser (`localStorage`).

When you use search engines, AI tools, wallpaper providers, or other external features, your browser sends requests directly to those services.

---

## AI-assisted development

I used AI tools throughout the project for coding assistance, debugging, research, brainstorming, and writing documentation.

---

## Getting Started

### Use online
Open [thinkpage.vercel.app](https://thinkpage.vercel.app) and set it as your browser homepage or new tab page.

### Install as a PWA
In Chrome, Edge, or Brave, click the install button in the address bar (or select "Add to Home Screen" on mobile) to use ThinkPage as a standalone desktop or mobile app.

### Run & Self-Host Locally
Clone the repository and run the included Python self-hosting server:

```bash
git clone https://github.com/naitiktuxx/ThinkPage.git
cd ThinkPage
python3 server.py
```
Open `http://localhost:8000` in your browser.

### Create & Download Release ZIP
Every commit pushed to `main` automatically triggers a GitHub Actions workflow that builds a clean `ThinkPage-release-vX.X.X.zip` package and attaches it to the [GitHub Releases](https://github.com/naitiktuxx/ThinkPage/releases) page.

To generate the clean ZIP archive locally:

```bash
python3 create_release.py
```
Or click **Download Source** / **View Project Releases (GitHub)** in the What's New release section or the ThinkPage settings panel.

---

## Contributing

Contributions and bug reports are welcome! Feel free to open an issue or submit a pull request.

Connect on X: [@naitiktux](https://x.com/naitiktux)

---

## License

MIT License. See [LICENSE](./LICENSE).
