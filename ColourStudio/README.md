# Colour Studio (Windows desktop)

A local-first Electron desktop app with palette library, favourites, gradient builder, image colour extraction, prompt-based palette generator, website preview, harmony wheel, shade scale, WCAG contrast checker, and CSS/Tailwind export.

## Requirements
- Windows 10/11
- Node.js 20+ (LTS recommended)
- Internet is only needed to download npm packages. The app itself works locally.

## Run from source
1. Extract the ZIP.
2. Open the extracted `ColourStudio` folder in VS Code or PowerShell.
3. Run:
   ```powershell
   npm install
   npm start
   ```

## Build a Windows installer
```powershell
npm install
npm run build:win
```
The installer will be created in `dist/`.

## Notes
- Favourites and theme are saved in localStorage on this Windows user profile.
- Image extraction is processed locally in the app.
- The palette generator is a built-in prompt/rule-based generator. It does not call a hosted AI model and needs no API key.
- Export uses a native Save dialog.
- The project includes a multi-resolution Windows icon at `assets/icon.ico` plus PNG sizes for other app surfaces. The same ICO is used for the app window, installer, uninstaller, and desktop shortcut.

## Support the developer

Use the **Buy Me a Coffee** button in the sidebar to support development: https://buymeacoffee.com/upanshu

Developed by Upanshu Sharma.
