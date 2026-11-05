const { contextBridge, ipcRenderer } = require('electron');
contextBridge.exposeInMainWorld('studio', {
  saveText: (payload) => ipcRenderer.invoke('save-text', payload),
  openImage: () => ipcRenderer.invoke('open-image'),
  readImage: (path) => ipcRenderer.invoke('read-image', path),
  openSupportPage: () => ipcRenderer.invoke('open-support-page')
});
