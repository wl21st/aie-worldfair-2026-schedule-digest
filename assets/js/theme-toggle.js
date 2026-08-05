(function () {
  var root = document.documentElement;
  var toggle = document.querySelector('[data-theme-toggle]');

  if (!toggle) {
    return;
  }

  var label = toggle.querySelector('.theme-toggle-label');
  var icon = toggle.querySelector('.theme-toggle-icon');

  function updateControl(theme) {
    var isLight = theme === 'light';
    var nextMode = isLight ? 'dark' : 'light';

    toggle.hidden = false;
    toggle.setAttribute('aria-pressed', String(isLight));
    toggle.setAttribute('aria-label', 'Switch to ' + nextMode + ' mode');
    toggle.setAttribute('title', 'Switch to ' + nextMode + ' mode');

    if (label) {
      label.textContent = nextMode === 'light' ? 'Light mode' : 'Dark mode';
    }

    if (icon) {
      icon.textContent = nextMode === 'light' ? '☀' : '☾';
    }
  }

  function setTheme(theme) {
    root.dataset.theme = theme;
    updateControl(theme);
  }

  setTheme(root.dataset.theme === 'light' ? 'light' : 'dark');

  toggle.addEventListener('click', function () {
    var nextTheme = root.dataset.theme === 'light' ? 'dark' : 'light';
    setTheme(nextTheme);

    try {
      window.localStorage.setItem('aie-theme', nextTheme);
    } catch (error) {
      // The visual toggle still works when storage is unavailable.
    }
  });
}());
