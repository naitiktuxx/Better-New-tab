# ThinkPage — The Ultimate New Tab & Custom Homepage

<p align="center">
  <img src="./app-icon.svg" width="110" alt="ThinkPage Logo" />
</p>

<p align="center">
  <strong>The familiar elegance of Google Chrome's interface, supercharged with AI assistants, custom search engines, speed tests, and privacy-first local controls.</strong>
</p>

<p align="center">
  <a href="https://thinkpage.vercel.app"><img src="https://img.shields.io/badge/Live_Demo-Try_ThinkPage_Now-blue.svg?style=for-the-badge&logo=vercel" alt="Live Demo" /></a>
  <a href="https://github.com/naitiktuxx/ThinkPage-Bridge-Extension"><img src="https://img.shields.io/badge/Firefox_Extension-ThinkPage_Bridge-orange.svg?style=for-the-badge&logo=firefox" alt="Firefox Extension" /></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" alt="License MIT" /></a>
  <img src="https://img.shields.io/badge/PWA-Offline_First-success.svg?style=for-the-badge" alt="PWA Ready" />
</p>

---

## Contents

- [What is ThinkPage?](#what-is-thinkpage)
- [Why ThinkPage? (Chrome vs. ThinkPage)](#why-thinkpage-chrome-vs-thinkpage)
- [What Extra Does ThinkPage Offer?](#what-extra-does-thinkpage-offer)
- [Key Features](#key-features)
  - [1. Universal & Custom Search Engines](#1-universal--custom-search-engines)
  - [2. One-Click AI Assistant Bar](#2-one-click-ai-assistant-bar)
  - [3. Google Lens Image Search UI](#3-google-lens-image-search-ui)
  - [4. Built-in Network Speed Test](#4-built-in-network-speed-test)
  - [5. Smart Speed Dial & App Store Icon Finder](#5-smart-speed-dial--app-store-icon-finder)
  - [6. Deep Aesthetics & Glassmorphism](#6-deep-aesthetics--glassmorphism)
  - [7. Multi-User Profiles](#7-multi-user-profiles)
  - [8. Firefox Native History Integration](#8-firefox-native-history-integration)
  - [9. Offline PWA & Data Portability](#9-offline-pwa--data-portability)
- [Feature Comparison Matrix](#feature-comparison-matrix)
- [Step-by-Step Setup Guide](#step-by-step-setup-guide)
  - [How to set as your browser New Tab / Homepage](#how-to-set-as-your-browser-new-tab--homepage)
  - [Installing as a Desktop / Mobile App (PWA)](#installing-as-a-desktop--mobile-app-pwa)
  - [Setting up the Firefox History Bridge](#setting-up-the-firefox-history-bridge)
- [Data Privacy & Google Takeout Import](#data-privacy--google-takeout-import)
- [Troubleshooting & FAQ](#troubleshooting--faq)
- [License & Community](#license--community)

---

## What is ThinkPage?

**ThinkPage** is a sleek, privacy-first custom homepage and new-tab dashboard designed to elevate your daily web browsing. Inspired by the clean, iconic aesthetic of Google Chrome's new-tab interface, ThinkPage retains that comfortable, intuitive feel—while removing Chrome's restrictions and packing in powerful productivity tools that Google never gave you.

Whether you want one-click access to your favorite AI models, a built-in speed test, custom wallpapers, automated high-resolution app icons, or isolated work/personal profiles, ThinkPage transforms every new tab into a personal command center.

> 🚀 **Try it immediately in your browser**: [https://thinkpage.vercel.app](https://thinkpage.vercel.app)

---

## Why ThinkPage? (Chrome vs. ThinkPage)

Google Chrome's default new-tab page is clean, but rigid:
- You are locked into Google Search.
- Your shortcuts are limited to generic favicons.
- You can't switch to dark modes like Catppuccin or apply Glassmorphism background blurs.
- There is no quick way to jump into AI tools like ChatGPT, Claude, or Perplexity.
- You have to open third-party websites just to run a quick internet speed test.

**ThinkPage gives you the best of both worlds**: the minimalist layout you already know and love, combined with total customization, zero tracking, and powerful built-in utilities.

---

## What Extra Does ThinkPage Offer?

Here is a quick snapshot of what ThinkPage adds on top of standard browser new-tab pages:

| Feature                  | Default Chrome New Tab  |                                 ThinkPage Homepage                                 |
| ------------------------ | :---------------------: | :--------------------------------------------------------------------------------: |
| **Search Engine Choice** |       Google only       | Google, DuckDuckGo, Bing, Brave, Kagi, Ecosia, SearXNG + **Custom Engine Creator** |
| **AI Assistants Bar**    |         ❌ None          |            ⚡ **ChatGPT, Gemini, Claude, Perplexity, DeepSeek, Copilot**            |
| **Visual Search (Lens)** |       Restricted        |       📸 **Google Lens UI with drag-and-drop, image URL, & clipboard paste**       |
| **Network Speed Test**   |         ❌ None          |          📶 **Built-in Cloudflare & Fast.com speed test (Pill or Modal)**          |
| **Shortcut Icons**       |    Low-res favicons     |       🎨 **App Store Icon Finder, squircle masking, glowing glass borders**        |
| **Visual Styling**       |    Basic light/dark     | 💎 **Liquid Glassmorphism, Catppuccin Macchiato, Custom Wallpapers, Font Pickers** |
| **Multiple Profiles**    |   Browser-level only    |     👤 **Instant in-tab Profiles (Work, Personal, Study) with separate state**     |
| **Privacy & Offline**    | Tracks queries to cloud |     🛡️ **100% Client-Side, local history, works offline via Service Worker**      |
| **History Import**       |       Restricted        |            📦 **Import Google Takeout (`MyActivity.json`) search logs**            |

---

## Key Features

### 1. Universal & Custom Search Engines
Switch seamlessly between Google, Bing, DuckDuckGo, Brave, Kagi, Ecosia, and SearXNG. 

Want to search a private index or internal site? Use the **Custom Engine Creator** to set custom search query URLs (e.g. `https://example.com/search?q=`), upload custom logos, and pick stylish typography for your logo branding (Inter, Outfit, Montserrat, Playfair Display, Pacifico).

### 2. One-Click AI Assistant Bar
Launch directly into your preferred AI tool straight from the search bar. Easily switch between **ChatGPT**, **Google Gemini**, **Anthropic Claude**, **Perplexity AI**, **DeepSeek**, and **Microsoft Copilot**.

### 3. Google Lens Image Search UI
Search by image with an authentic Google Lens UI card. Paste an image URL, drag-and-drop an image file from your computer, or paste directly from your clipboard—with automatic fallback options for Bing Visual Search and DuckDuckGo.

### 4. Built-in Network Speed Test
Check your internet speed without navigating away from your dashboard. Powered by **Cloudflare** (`speed.cloudflare.com`) or **Fast.com**, you can view your download, upload, and latency metrics as an inline live status pill or an expanded modal card.

### 5. Smart Speed Dial & App Store Icon Finder
Add your favorite websites as speed-dial shortcuts. Don't settle for blurry favicons—ThinkPage includes an integrated **App Store Icon Search** that fetches official high-definition app icons automatically. Customize shortcut appearance with squircle masks, glowing glass borders, and color normalization.

### 6. Deep Aesthetics & Glassmorphism
Make your browser look stunning:
- **Themes**: Switch between Light Mode, Dark Mode, Catppuccin Macchiato, or Auto (Device preference).
- **Liquid Glass Effect**: Enable dynamic backdrop-filter glassmorphism with custom accent colors.
- **Curated Backgrounds**: Choose from preset wallpaper themes (Space & Astronomy, Cyberpunk & Neon, Modern Architecture, Nature & Landscapes, Minimalist Abstract, Sleek Dark) or upload your own wallpaper.
- **Layout Fine-Tuning**: Adjust search bar width, vertical placement, and horizontal/vertical logo offsets down to the exact pixel.

### 7. Multi-User Profiles
Keep your life organized. Create separate profiles for **Work**, **Personal**, **Research**, or **Gaming**. Each profile gets its own shortcut layout, search history, wallpaper, and theme preferences.

### 8. Firefox Native History Integration
Using Firefox? Install the companion [ThinkPage Bridge Extension](https://github.com/naitiktuxx/ThinkPage-Bridge-Extension) to query your native Firefox browsing history directly inside ThinkPage search suggestions without sending any browsing data off your machine.

### 9. Offline PWA & Data Portability
ThinkPage registers a Progressive Web App (PWA) Service Worker, caching application assets so your new tab opens instantly even without an internet connection. Export your complete setup as a JSON backup anytime, or import past search history directly from **Google Takeout** (`MyActivity.json`).

---

## Feature Comparison Matrix

| Capability | Chrome Default | Momentum | Infinity Tab | ThinkPage |
|---|:---:|:---:|:---:|:---:|
| **Price** | Free | Paid Tier ($4/mo) | Free / Ads | **100% Free & Open Source** |
| **Build Setup Needed** | No | Closed | Closed | **Zero Build (Vanilla HTML/CSS/JS)** |
| **Privacy / Telemetry** | Google Tracked | Cloud Account | Account / Ads | **Zero Tracking / 100% Local** |
| **AI Assistants Integration** | ❌ No | Paid only | ❌ No | **Included (6+ AI Models)** |
| **Built-in Speed Test** | ❌ No | ❌ No | ❌ No | **Included (Cloudflare / Fast.com)** |
| **Custom Engine Fonts & Logos** | ❌ No | ❌ No | ❌ No | **Included** |
| **Google Takeout History Import**| ❌ No | ❌ No | ❌ No | **Included** |
| **Firefox Native History Bridge**| ❌ No | ❌ No | ❌ No | **Included (Optional Extension)** |

---

## Step-by-Step Setup Guide

### How to set as your browser New Tab / Homepage

#### Google Chrome / Brave / Edge / Arc
1. Open your browser settings and navigate to **On startup** / **Homepage**.
2. Select **Open a specific page or set of pages**.
3. Enter `https://thinkpage.vercel.app` (or your local self-hosted URL `http://localhost:8000`).
4. To override new tabs, install a standard extension like *Custom New Tab URL* or *New Tab Override* pointing to `https://thinkpage.vercel.app`.

#### Mozilla Firefox
1. Open Firefox **Settings** → **Home**.
2. Under **Homepage and new windows**, select **Custom URLs...** and enter `https://thinkpage.vercel.app`.
3. Under **New tabs**, choose **Custom URLs...** and paste `https://thinkpage.vercel.app`.

---

### Installing as a Desktop / Mobile App (PWA)

ThinkPage can be installed directly onto your computer or smartphone like a native application:

- **Desktop (Chrome / Edge / Brave)**: Click the **Install Icon** in the address bar (or menu `...` → *Install ThinkPage*).
- **iOS (Safari)**: Tap the **Share** button → **Add to Home Screen**.
- **Android (Chrome)**: Tap the **Menu** dots → **Add to Home Screen**.

Once installed, ThinkPage opens in a standalone window and works completely offline!

---

### Setting up the Firefox History Bridge

For the ultimate Firefox setup with native history suggestions and automatic address bar focus:

1. Visit the [ThinkPage-Bridge-Extension Repository](https://github.com/naitiktuxx/ThinkPage-Bridge-Extension).
2. Install the `.xpi` add-on release into Firefox.
3. Open ThinkPage, click **Customize** in the bottom right, and expand **Search & tools**.
4. Enable **Use browser history (Extension)**.

Now, as you type in the search bar, native Firefox history items will automatically populate your suggestions!

---

## Data Privacy & Google Takeout Import

### Your Data Stays Local
ThinkPage does **not** collect telemetry, track your clicks, or send search queries to any third-party analytics servers. Your history logs, custom shortcuts, and profile settings are saved locally inside your browser (`localStorage` & `IndexedDB`).

### Importing Google Takeout History
Want your past Google search history available in ThinkPage suggestions?

1. Go to [Google Takeout](https://takeout.google.com) and select **My Activity (Search history)** in JSON format.
2. Download and unzip your Takeout archive.
3. In ThinkPage, open the **Search History** modal (or click the history icon).
4. Select the **Import History** tab.
5. Drag and drop your `MyActivity.json` file directly into the drop zone.

---

## Troubleshooting & FAQ

#### Q: Can I run ThinkPage completely offline without Vercel or any server?
**A:** Yes! Download the code repository, open `index.html` in your browser, or host it locally with `python3 -m http.server 8000`. The service worker will cache all required resources.

#### Q: How do I change the default search engine?
**A:** Click **Customize** in the bottom right corner → expand **Search & tools** → select your preferred engine under **Search** (Google, DuckDuckGo, Bing, Brave, Kagi, Ecosia, SearXNG, or Custom).

#### Q: How do I fetch official high-res icons for my custom shortcuts?
**A:** When adding or editing a shortcut, click the **App Store Icon** button next to the icon URL input. Search for the app name, click the official icon from the results, and click **Done**!

#### Q: The Speed Test button isn't loading results. What should I do?
**A:** Ensure your adblocker or privacy extension isn't blocking requests to `speed.cloudflare.com` or `fast.com`. You can also switch between Cloudflare and Fast.com in **Customize → Speed test**.

---

## License & Community

Distributed under the **MIT License**. See [`LICENSE`](./LICENSE) for full details.

Built with ❤️ by **Naitik**  
Connect on X (Twitter): [@naitiktux](https://x.com/naitiktux)  
Live Demo: [thinkpage.vercel.app](https://thinkpage.vercel.app)
