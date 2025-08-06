// assets/copy_plot.js
// Defines clientsided copyPlotImage function for Dash

// window.dash_clientside = window.dash_clientside || {};
// window.dash_clientside.clientside = Object.assign(
//     window.dash_clientside.clientside || {},
//     {
//         copyPlotImage: function(n_clicks, imageData) {
//             // Only run after a click and if we have image data
//             if (!n_clicks || !imageData) {
//                 return window.dash_clientside.no_update;
//             }
//             try {
//                 // Strip off data URI prefix if present
//                 let b64 = imageData;
//                 if (b64.startsWith('data:image')) {
//                     b64 = b64.split(',')[1];
//                 }
//                 const binary = atob(b64);
//                 const len = binary.length;
//                 const array = new Uint8Array(len);
//                 for (let i = 0; i < len; i++) {
//                     array[i] = binary.charCodeAt(i);
//                 }
//                 const blob = new Blob([array], { type: 'image/png' });
//                 const item = new ClipboardItem({ 'image/png': blob });
//                 navigator.clipboard.write([item]);
//             } catch (err) {
//                 console.error('Error copying plot image:', err);
//             }
//             // return unchanged data so the Store isn't cleared
//             return imageData;
//         }
//     }
// );

// assets/clientside.js
window.dash_clientside = Object.assign({}, window.dash_clientside, {
  clientside: {
    copyPlotImage: function(n_clicks, stored_image_data) {
      if (n_clicks && stored_image_data) {
        const img = new Image();
        img.src = 'data:image/png;base64,' + stored_image_data;
        img.onload = function() {
          const canvas = document.createElement('canvas');
          canvas.width = this.naturalWidth;
          canvas.height = this.naturalHeight;
          canvas.getContext('2d').drawImage(this, 0, 0);
          canvas.toBlob(function(blob) {
            const item = new ClipboardItem({ 'image/png': blob });
            navigator.clipboard.write([item]);
          });
        };
      }
      // keep the button label stable
      return "Copy Plot to Clipboard";
    }
  }
});