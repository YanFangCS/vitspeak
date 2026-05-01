function copyBibTeX() {
  const bibtexElement = document.getElementById('bibtex-code');
  const button = document.querySelector('.copy-bibtex-btn');
  const label = button ? button.querySelector('.copy-text') : null;

  if (!bibtexElement || !button || !label) {
    return;
  }

  const text = bibtexElement.textContent;
  const markCopied = () => {
    button.classList.add('copied');
    label.textContent = 'Copied';
    window.setTimeout(() => {
      button.classList.remove('copied');
      label.textContent = 'Copy';
    }, 1800);
  };

  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(text).then(markCopied).catch(() => fallbackCopy(text, markCopied));
    return;
  }

  fallbackCopy(text, markCopied);
}

function fallbackCopy(text, onCopied) {
  const textArea = document.createElement('textarea');
  textArea.value = text;
  textArea.setAttribute('readonly', '');
  textArea.style.position = 'absolute';
  textArea.style.left = '-9999px';
  document.body.appendChild(textArea);
  textArea.select();
  document.execCommand('copy');
  document.body.removeChild(textArea);
  onCopied();
}

function scrollToTop() {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
}

window.addEventListener('scroll', () => {
  const scrollButton = document.querySelector('.scroll-to-top');
  if (!scrollButton) {
    return;
  }
  scrollButton.classList.toggle('visible', window.scrollY > 360);
});
