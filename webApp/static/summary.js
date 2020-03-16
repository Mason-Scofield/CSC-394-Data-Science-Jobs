var isMinimized = false;
var isLocked    = false;

var minimize;
var lock;

var summary;
var hidden;
var reveal;

window.addEventListener('load', () => {
    minimize = document.getElementById('minimize');
    lock     = document.getElementById('lock');

    summary = document.getElementById('summary');
    hidden  = () => { summary.style.bottom = '-250px' };
    reveal  = () => { summary.style.bottom = '-5px' };

    showButtons();

    minimize.onclick = () => {
        if (!isMinimized) { maximizeToMinimize(); } // maximized -> minimized
        else              { minimizeToMaximize(); } // minimized -> maximized
    };

    lock.onclick = () => {
        if (!isLocked) { unlockedToLocked(); } // unlocked -> locked
        else           { lockedToUnlocked(); } // locked -> unlocked
    };

    var degrees = 180;

    document.getElementById('refresh').onclick = (e) => {
        var table = document.getElementById('table')
        table.style.opacity = '1';
        table.rows[0].style.display = 'table-row';
        document.getElementById('postings').style.visibility = 'visible';
        e.target.innerText = '';
        e.target.className = 'fas fa-sync w3-hover-opacity';

        e.target.onmousedown = (e) => {
            e.target.style.transform = `rotate(${degrees}deg)`;
            degrees += 180;
        };

        refresh();
    };
});


function showButtons() {
    new IntersectionObserver(() => {
        var rect = summary.getBoundingClientRect();
        var completelyVisible = rect.top    >= 0                  &&
                                rect.left   >= 0                  &&
                                rect.bottom <= window.innerHeight &&
                                rect.right  <= window.innerWidth;
        if (completelyVisible || rect.top < 0) {
            minimize.style.cssText += 'opacity: 0; visibility: hidden;';
            lock.style.cssText     += 'opacity: 0; visibility: hidden;';
        }
        else if (rect.top > 0) {
            minimize.style.cssText += 'opacity: 1; visibility: visible;';
            lock.style.cssText     += 'opacity: 1; visibility: visible;';
            hidden();
            minimizeToMaximize(); lockedToUnlocked();
        }
    }, { threshold: 1.0 }).observe(summary);
}


function maximizeToMinimize() {
    summary.style.position = 'relative';
    summary.onmouseenter = () => {};
    summary.onmouseleave = () => {};

    minimize.classList.remove('fa-window-minimize');
    minimize.classList.add('fa-plus');
    minimize.style.top = '3%';
    isMinimized = true;
}


function minimizeToMaximize() {
    summary.style.position = 'sticky';
    summary.onmouseenter = reveal;
    summary.onmouseleave = hidden;

    minimize.classList.remove('fa-plus');
    minimize.classList.add('fa-window-minimize');
    minimize.style.top = '2%';
    isMinimized = false;
}


function lockedToUnlocked() {
    summary.onmouseenter = reveal;
    summary.onmouseleave = hidden;

    lock.classList.remove('fa-lock');
    lock.classList.add('fa-lock-open');
    isLocked = false;
}


function unlockedToLocked() {
    summary.onmouseenter = () => {};
    summary.onmouseleave = () => {};

    lock.classList.remove('fa-lock-open');
    lock.classList.add('fa-lock');
    isLocked = true;
}


function refresh() {
    let queryString = `/${document.getElementById('locationSelect').value}/jobs?`;

    Array.from(document.getElementsByClassName('slider')).forEach(elem => {
      let key = encodeURI(elem.previousElementSibling.innerText.replace('&', '').replace(/\s/g, ''));
      queryString += key + '=' + elem.value + '&';
    });
    queryString = queryString.substring(0, queryString.length - 1); // since there will be a trailing ampersand

    var numDisplay = 5; // number of postings to display at first
    var more = document.getElementById('more');
    more.classList.remove('w3-hide');

    fetch(queryString)
      .then(response => response.json())
      .then(postings => {
        if (numDisplay >= postings.length) more.classList.add('w3-hide');
        updateJobs(postings, numDisplay);
        more.onclick = () => {
          numDisplay += 5;
          if (numDisplay >= postings.length) more.classList.add('w3-hide');
          updateJobs(postings, numDisplay);
        };
      });
}


function updateJobs(postings, numDisplay) {
    var table = document.getElementById('table');
    var number = postings.length;
    document.getElementById("numPostings").innerText = number + ` job posting${number != 1 ? 's' : ''} curated for you`;

    let len = table.rows.length;
    for (let i = 1; i < len; ++i)
      table.deleteRow(1); // delete everything but the headers

    let i = 0;
    for (let posting of postings) {
        var row = table.insertRow(-1);

        for (let [j, val] of posting.entries()) {
            var cell = row.insertCell(-1);

            if (j !== posting.length - 1) // not the last element
                cell.textContent = val;
            else {
                cell.innerHTML = '<i class="fas fa-external-link-alt"></i>';
                row.onclick = () => { window.open(val); };
            }
        }
        if (++i == numDisplay) break;
    }
}
