/* dotAIO by dotmod: search, section chips, card galleries and lightbox.
   Same behaviour as the main masterlist page. The one addition: photos here
   load from dotmod.com and retailer sites, so any photo that fails to load is
   dropped from its card and the lightbox instead of showing as broken. */

/* ---- search and section chips ---- */
(function () {
  var q = document.getElementById('q');
  var cats = Array.prototype.slice.call(document.querySelectorAll('.cat'));
  var chips = Array.prototype.slice.call(document.querySelectorAll('.chip'));
  var empty = document.getElementById('empty');
  var emptyMsg = document.getElementById('empty-msg');

  function filter() {
    var term = q.value.trim().toLowerCase();
    var shown = 0;
    cats.forEach(function (sec) {
      var n = 0;
      sec.querySelectorAll('.card').forEach(function (c) {
        var hit = !term || c.getAttribute('data-search').indexOf(term) !== -1;
        c.hidden = !hit;
        if (hit) n++;
      });
      var count = sec.querySelector('.cat-count');
      var total = +count.getAttribute('data-total');
      count.textContent = term ? (n + ' of ' + total) : (total + (total === 1 ? ' item' : ' items'));
      sec.hidden = n === 0;
      var chip = document.querySelector('.chip[data-target="' + sec.id + '"]');
      if (chip) { chip.hidden = n === 0; chip.querySelector('.chip-n').textContent = n; }
      shown += n;
    });
    empty.hidden = shown !== 0;
    if (!shown) emptyMsg.textContent = 'Nothing in the list matches “' + q.value.trim() + '”.';
  }
  q.addEventListener('input', filter);
  document.getElementById('clear').addEventListener('click', function () { q.value = ''; filter(); q.focus(); });

  var strip = document.querySelector('.chips');
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        chips.forEach(function (c) {
          var on = c.getAttribute('data-target') === en.target.id;
          c.classList.toggle('is-active', on);
          if (on && strip.scrollWidth > strip.clientWidth) {
            var left = c.offsetLeft - (strip.clientWidth - c.offsetWidth) / 2;
            strip.scrollTo({ left: Math.max(0, left), behavior: reduce ? 'auto' : 'smooth' });
          }
        });
      });
    }, { rootMargin: '-35% 0px -60% 0px' });
    cats.forEach(function (s) { io.observe(s); });
  }
})();

/* ---- card galleries: one big photo, three thumbs, hover to swap, click to zoom ---- */
(function () {
  var lb = document.getElementById('lb');
  var lbImg = document.getElementById('lb-img');
  var lbCap = document.getElementById('lb-cap');
  var shots = [], at = 0, title = '', opener = null;

  function paint() {
    lbImg.src = shots[at];
    lbImg.alt = title;
    lbCap.innerHTML = '';
    lbCap.appendChild(document.createTextNode(title));
    if (shots.length > 1) {
      var s = document.createElement('span');
      s.textContent = 'Photo ' + (at + 1) + ' of ' + shots.length;
      lbCap.appendChild(s);
    }
    document.getElementById('lb-prev').hidden = shots.length < 2;
    document.getElementById('lb-next').hidden = shots.length < 2;
  }
  function open(list, name, index, from) {
    shots = list; title = name; at = index; opener = from;
    paint();
    lb.hidden = false;
    document.body.style.overflow = 'hidden';
    document.getElementById('lb-close').focus();
  }
  function close() {
    lb.hidden = true;
    lbImg.src = '';
    document.body.style.overflow = '';
    if (opener) { opener.focus(); opener = null; }
  }
  function step(d) { if (shots.length > 1) { at = (at + d + shots.length) % shots.length; paint(); } }

  document.getElementById('lb-close').addEventListener('click', close);
  document.getElementById('lb-prev').addEventListener('click', function (e) { e.stopPropagation(); step(-1); });
  document.getElementById('lb-next').addEventListener('click', function (e) { e.stopPropagation(); step(1); });
  lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
  document.addEventListener('keydown', function (e) {
    if (lb.hidden) return;
    if (e.key === 'Escape') close();
    else if (e.key === 'ArrowLeft') step(-1);
    else if (e.key === 'ArrowRight') step(1);
  });

  /* Resolves to the src if the photo loads, or null if it doesn't. */
  function probe(src) {
    return new Promise(function (done) {
      var im = new Image();
      im.referrerPolicy = 'no-referrer';
      im.onload = function () { done(im.naturalWidth > 1 ? src : null); };
      im.onerror = function () { done(null); };
      im.src = src;
    });
  }

  function emptyRow(ul) {
    for (var i = 0; i < 3; i++) {
      var li = document.createElement('li');
      var slot = document.createElement('span');
      slot.className = 'thumb-empty';
      slot.setAttribute('aria-hidden', 'true');
      li.appendChild(slot);
      ul.appendChild(li);
    }
  }

  function placeholder(well) {
    well.innerHTML = '<div class="ph">Photo coming soon</div>';
    well.removeAttribute('role');
    well.removeAttribute('tabindex');
    well.style.cursor = 'default';
  }

  function build(card, well, hero, name, list) {
    var ul = document.createElement('ul');
    ul.className = 'thumbs';
    ul.setAttribute('aria-label', name + ' photos');
    well.insertAdjacentElement('afterend', ul);

    if (!list.length) { placeholder(well); emptyRow(ul); return; }
    if (hero.getAttribute('src') !== list[0]) hero.src = list[0];

    /* Photo 1 holds the big slot; the thumb row is the other three shots. */
    var rest = list.slice(1);
    var buttons = [];
    for (var i = 0; i < 3; i++) {
      var li = document.createElement('li');
      if (i < rest.length) {
        var b = document.createElement('button');
        b.type = 'button';
        b.className = 'thumb';
        b.setAttribute('aria-label', 'Photo ' + (i + 2) + ' of ' + name);
        var im = document.createElement('img');
        im.src = rest[i]; im.alt = ''; im.loading = 'lazy'; im.decoding = 'async';
        b.appendChild(im);
        li.appendChild(b);
        buttons.push(b);
      } else {
        var slot = document.createElement('span');
        slot.className = 'thumb-empty';
        slot.setAttribute('aria-hidden', 'true');
        li.appendChild(slot);
      }
      ul.appendChild(li);
    }

    var shown = 0;
    function show(i) {
      if (i === shown) return;
      shown = i;
      hero.src = list[i];
      buttons.forEach(function (b, n) { b.classList.toggle('is-active', n + 1 === i); });
    }
    buttons.forEach(function (b, i) {
      b.addEventListener('mouseenter', function () { show(i + 1); });
      b.addEventListener('focus', function () { show(i + 1); });
      b.addEventListener('click', function () { open(list, name, i + 1, b); });
    });
    ul.addEventListener('mouseleave', function () { show(0); });
    ul.addEventListener('focusout', function (e) { if (!ul.contains(e.relatedTarget)) show(0); });
    well.addEventListener('click', function () { open(list, name, shown, hero); });
    well.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(list, name, shown, hero); }
    });
    well.tabIndex = 0;
    well.setAttribute('role', 'button');
    well.setAttribute('aria-label', 'Enlarge photo of ' + name);
  }

  Array.prototype.forEach.call(document.querySelectorAll('.card'), function (card) {
    var well = card.querySelector('.well');
    var hero = well.querySelector('img');
    var name = card.querySelector('.name').textContent.trim();
    if (!hero) { build(card, well, null, name, []); return; }

    var srcs = [hero.getAttribute('src')];
    Array.prototype.forEach.call(well.querySelectorAll('.shot-src'), function (img) {
      srcs.push(img.getAttribute('src'));
      img.remove();
    });
    Promise.all(srcs.map(probe)).then(function (ok) {
      build(card, well, hero, name, ok.filter(Boolean));
    });
  });
})();
