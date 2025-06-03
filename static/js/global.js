
(function () {
  const style = document.createElement('style');
  style.innerHTML = `
    .flash-message {
        position: fixed;
        top: 20px;
        right: -400px;
        background-color: #1e2138;
        color: #ffffff;
        border-left: 5px solid #D6ED16;
        padding: 15px 20px;
        border-radius: 8px;
        box-shadow: 0 4px 10px #00000060;
        z-index: 9999;
        min-width: 250px;
        max-width: 400px;
        font-size: 14px;
        opacity: 0;
        transition: all 0.5s ease-in-out;
        font-family: 'Poppins', sans-serif;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .flash-message.show {
        right: 20px;
        opacity: 1;
    }
    .flash-success { border-left-color: #4CAF50; }
    .flash-error { border-left-color: #f44336; }
    .flash-info  { border-left-color: #D6ED16; }

    .flash-icon {
        font-size: 18px;
        flex-shrink: 0;
    }
    .flash-text {
        flex: 1;
    }
  `;
  document.head.appendChild(style);

  window.showFlashMessage = function (message, type = 'info') {
    const flash = document.createElement('div');
    flash.className = `flash-message flash-${type}`;

    const icon = document.createElement('span');
    icon.className = 'flash-icon';

    switch (type) {
      case 'success': icon.textContent = '✅'; break;
      case 'error': icon.textContent = '❌'; break;
      case 'info':
      default: icon.textContent = 'ℹ️'; break;
    }

    const text = document.createElement('span');
    text.className = 'flash-text';
    text.textContent = message;

    flash.appendChild(icon);
    flash.appendChild(text);
    document.body.appendChild(flash);

    setTimeout(() => flash.classList.add('show'), 50);
    setTimeout(() => {
      flash.classList.remove('show');
      setTimeout(() => flash.remove(), 500);
    }, 5000);
  };
})();
