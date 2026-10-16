(function () {
  var modal = document.querySelector('[data-video-modal]');
  if (!modal) {
    return;
  }

  var frame = modal.querySelector('[data-video-modal-frame]');
  var externalLink = modal.querySelector('[data-video-modal-external]');
  var closeButton = modal.querySelector('.video-modal-close');
  var lastTrigger = null;

  function videoIdFromUrl(href) {
    var url;
    try {
      url = new URL(href, window.location.href);
    } catch (error) {
      return null;
    }

    var host = url.hostname.replace(/^www\./, '');
    var videoId = null;

    if (host === 'youtube.com' || host === 'm.youtube.com') {
      if (url.pathname === '/watch') {
        videoId = url.searchParams.get('v');
      } else if (url.pathname.indexOf('/shorts/') === 0 || url.pathname.indexOf('/embed/') === 0) {
        videoId = url.pathname.split('/')[2];
      }
    } else if (host === 'youtu.be') {
      videoId = url.pathname.slice(1).split('/')[0];
    }

    return videoId && /^[A-Za-z0-9_-]{11}$/.test(videoId) ? videoId : null;
  }

  function closeModal() {
    modal.hidden = true;
    document.body.classList.remove('video-modal-open');
    frame.src = '';

    if (lastTrigger) {
      lastTrigger.focus();
      lastTrigger = null;
    }
  }

  function openModal(trigger, videoId) {
    var sourceUrl = trigger.href;
    var title = trigger.getAttribute('aria-label') || 'YouTube recording';

    lastTrigger = trigger;
    frame.title = title;
    frame.src = 'https://www.youtube-nocookie.com/embed/' + videoId + '?autoplay=1&rel=0';
    externalLink.href = sourceUrl;
    modal.hidden = false;
    document.body.classList.add('video-modal-open');
    closeButton.focus();
  }

  document.addEventListener('click', function (event) {
    var anchor = event.target.closest('a[href]');
    if (!anchor || anchor.hasAttribute('data-video-modal-external')) {
      return;
    }

    var videoId = videoIdFromUrl(anchor.href);
    if (!videoId) {
      return;
    }

    event.preventDefault();
    openModal(anchor, videoId);
  });

  modal.addEventListener('click', function (event) {
    if (event.target.hasAttribute('data-video-modal-close')) {
      closeModal();
    }
  });

  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape' && !modal.hidden) {
      closeModal();
    }
  });
}());
