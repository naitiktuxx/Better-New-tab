# ThinkPage

ThinkPage is a lightweight customizable browser new tab page. It runs locally in your browser and uses local storage to keep your preferences, shortcuts, and custom settings private.

Live site: https://thinkpage.vercel.app

## Background

Firefox is open and flexible, but the simple layout of Chrome's default new tab page is convenient. ThinkPage combines that clean design with custom search engines, personalized shortcuts, and customizable themes without sending your data to external tracking services.

## Core Features and Functionality

Search engine switching
You can switch search engines between Google, Bing, DuckDuckGo, or custom search endpoints. Typing into the search bar pulls live search suggestions directly from the selected provider into the autocomplete dropdown.

Custom shortcuts and speed dial
Users can add, remove, and reorder shortcuts with custom labels and icons. Shortcut categories include web applications and direct links to AI services like ChatGPT, Gemini, and Claude.

Themes and visual customization
ThinkPage includes light mode, dark mode, Catppuccin themes, and custom color accents. Background options support solid colors, curated wallpapers, or custom image uploads with optional glassmorphism blur effects.

Image search
The search bar supports visual image queries. You can upload an image file, paste an image from your clipboard, or provide an image URL to query Google Lens.

Profiles and data management
You can create multiple profiles to isolate settings for work and personal use. All configuration settings stay in browser local storage and can be backed up or transferred using JSON export and import.

Offline support and self hosting
The web app uses a Progressive Web App service worker to function offline. You can also host ThinkPage on your own machine using the included Python server script.

## Firefox Extension Integration

The optional ThinkPage Bridge extension connects ThinkPage directly with Firefox to replace the browser default new tab page.

When enabled, opening a new tab immediately focuses the search bar so you can start typing right away. The extension also accesses local Firefox history to display relevant search suggestions in real time.

1. Download the latest `.xpi` file from the ThinkPage Bridge repository.
2. Open `about:addons` in Firefox.
3. Select Install Add-on From File from the settings menu and choose the `.xpi` file.

## Privacy

ThinkPage contains no tracking scripts or external telemetry. All preferences and saved shortcuts remain in your browser local storage. When you perform a search or upload a wallpaper, your browser sends requests directly to those third party services.

## Running Locally and Releases

To run the local HTTP server:

```bash
python3 server.py
```

To build a clean source code ZIP archive:

```bash
python3 create_release.py
```

Commits pushed to the main repository branch automatically build and publish source code ZIP packages on GitHub Releases.

## License

MIT License. See LICENSE for details.
