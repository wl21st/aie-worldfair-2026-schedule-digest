(function () {
  function isYouTubeLink(anchor) {
    var url;

    try {
      url = new URL(anchor.href, window.location.href);
    } catch (error) {
      return false;
    }

    var host = url.hostname.replace(/^www\./, '');
    return host === 'youtube.com' || host === 'm.youtube.com' || host === 'youtu.be';
  }

  function configureYouTubeLink(anchor) {
    if (!isYouTubeLink(anchor)) {
      return;
    }

    anchor.target = '_blank';
    anchor.rel = 'noopener';
  }

  document.querySelectorAll('a[href]').forEach(configureYouTubeLink);

  document.addEventListener('click', function (event) {
    var anchor = event.target.closest('a[href]');
    if (anchor) {
      configureYouTubeLink(anchor);
    }
  });
}());
