// assets/clipboard.js
window.dash_clientside = Object.assign({}, window.dash_clientside, {
  clipboard: {
    // n_clicks, figure, btn_id 를 받습니다
    copyPlot: function(n_clicks, figure, btn_id) {
      // 초기 렌더
      if (!n_clicks) { return "Copy Plot to Clipboard"; }

      try {
        if (!figure) { throw new Error("No figure"); }

        // 오프스크린 div
        const tmp = document.createElement('div');
        tmp.style.position = 'fixed';
        tmp.style.left = '-10000px';
        tmp.style.top = '-10000px';
        document.body.appendChild(tmp);

        const w = (figure.layout && figure.layout.width)  || 800;
        const h = (figure.layout && figure.layout.height) || 600;

        // 오프스크린 플롯 → 이미지 → 클립보드(폴백: 다운로드)
        window.Plotly.newPlot(
          tmp,
          figure.data || [],
          Object.assign({}, figure.layout || {}, { width: w, height: h }),
          { staticPlot: true }
        ).then(function () {
          return window.Plotly.toImage(tmp, { format: 'png', width: w, height: h, scale: 2 });
        }).then(function (url) {
          return fetch(url);
        }).then(function (res) { return res.blob(); })
          .then(function (blob) {
            if (!navigator.clipboard || !window.ClipboardItem) {
              const a = document.createElement('a');
              a.href = URL.createObjectURL(blob);
              a.download = 'plot.png';
              document.body.appendChild(a);
              a.click();
              a.remove();
              return;
            }
            const item = new ClipboardItem({ [blob.type]: blob });
            return navigator.clipboard.write([item]);
          }).catch(function (err) {
            console.error('Copy failed:', err);
          }).finally(function () {
            try { window.Plotly.purge(tmp); } catch (e) {}
            tmp.remove();
          });

        // ▶ 라벨 자동 원복 (2초 뒤)
        try {
          const btnDomId = JSON.stringify(btn_id);
          setTimeout(function () {
            const btn = document.getElementById(btnDomId);
            if (btn) btn.textContent = "Copy Plot to Clipboard";
          }, 2000);
        } catch (e) {
          // 무시
        }

        // 즉시 버튼 라벨은 "Copied!" 로
        return "Copied!";
      } catch (e) {
        console.error(e);
        return "Copy failed";
      }
    }
  }
});
