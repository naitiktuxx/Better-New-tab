# ThinkPage

<img src="./app-icon.svg" width="96" alt="ThinkPage Logo" />

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Live Demo](https://img.shields.io/badge/Live_Demo-thinkpage.vercel.app-blue.svg)](https://thinkpage.vercel.app)
[![Firefox Bridge Extension](https://img.shields.io/badge/Firefox_Extension-ThinkPage_Bridge-orange.svg)](https://github.com/naitiktuxx/ThinkPage-Bridge-Extension)

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
- **Themes & wallpapers**: Light, Dark, Catppuccin, preset wallpapers, or custom image uploads
- **Glassmorphism UI**: Optional backdrop blur effects inspired by macOS
- **AI shortcuts**: Quick access to ChatGPT, Gemini and Claude etc. 
- **Image search**: Lens-style image search supporting URLs, drag-and-drop, and clipboard paste
- **Profiles**: Separate settings, history, and shortcuts for different profiles
- **Offline support**: Works offline as a Progressive Web App
- **Firefox integration**: Optional companion extension for history suggestions and tab handling

---

## Firefox Extension

The optional **[ThinkPage-Bridge-Extension](https://github.com/naitiktuxx/ThinkPage-Bridge-Extension)** handles new-tab focus and lets ThinkPage use Firefox's native browsing history for search suggestions.

It can also set ThinkPage as the default new tab page in Firefox and other Gecko based browsers.

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

### Create a Release ZIP
To generate a clean ZIP archive of the source code for distribution:

```bash
python3 create_release.py
```
Or click **Download Release ZIP** in the ThinkPage settings panel (Account & System section).

---

## Contributing

Contributions and bug reports are welcome! Feel free to open an issue or submit a pull request.

Connect on X: [@naitiktux](https://x.com/naitiktux)

---

## License

MIT License. See [LICENSE](./LICENSE).
