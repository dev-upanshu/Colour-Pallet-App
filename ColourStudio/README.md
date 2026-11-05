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
- The installer config expects an optional `assets/icon.ico`; remove the `icon` line from `package.json` if you do not add a custom icon.
