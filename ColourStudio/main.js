const { app, BrowserWindow, ipcMain, dialog, shell } = require('electron');
const path = require('path');
const fs = require('fs');

function createWindow() {
  const win = new BrowserWindow({
    width: 1440, height: 920, minWidth: 1050, minHeight: 700,
    backgroundColor: '#f8f9fc',
    icon: path.join(__dirname, 'assets', 'icon.ico'),
    webPreferences: { preload: path.join(__dirname, 'preload.js'), contextIsolation: true, nodeIntegration: false }
  });
  win.loadFile(path.join(__dirname, 'index.html'));
}
app.whenReady().then(() => {
  createWindow();
  app.on('activate', () => { if (BrowserWindow.getAllWindows().length === 0) createWindow(); });
});
app.on('window-all-closed', () => { if (process.platform !== 'darwin') app.quit(); });

ipcMain.handle('save-text', async (_event, {suggestedName, content}) => {
  const result = await dialog.showSaveDialog({ defaultPath: suggestedName, filters: [{name:'Text files', extensions:['css','json','txt']}] });
  if (result.canceled || !result.filePath) return { canceled: true };
  fs.writeFileSync(result.filePath, content, 'utf8');
  return { canceled: false, filePath: result.filePath };
});
ipcMain.handle('open-image', async () => {
  const result = await dialog.showOpenDialog({ properties:['openFile'], filters:[{name:'Images',extensions:['png','jpg','jpeg','webp','bmp']}] });
  return result.canceled ? null : result.filePaths[0];
});
ipcMain.handle('read-image', async (_event, filePath) => {
  const ext = path.extname(filePath).slice(1).toLowerCase();
  const mime = ({jpg:'jpeg',jpeg:'jpeg',png:'png',webp:'webp',bmp:'bmp'})[ext] || 'png';
  return `data:image/${mime};base64,${fs.readFileSync(filePath).toString('base64')}`;
});

// Open the creator's support page in the user's default browser.
ipcMain.handle('open-support-page', async () => {
  await shell.openExternal('https://buymeacoffee.com/upanshu');
  return true;
});
