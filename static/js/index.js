let copyResetTimer;

async function copyBibTeX() {
  const citation = document.getElementById('bibtex-code');
  const button = document.querySelector('.copy-bibtex-btn');
  const label = button?.querySelector('.copy-text');
  const status = document.querySelector('.copy-status');
  if (!citation || !button || !label) return;
  if (button.getAttribute('aria-busy') === 'true') return;

  window.clearTimeout(copyResetTimer);
  button.setAttribute('aria-busy', 'true');
  if (status) status.textContent = '';
  let copied = false;
  try {
    if (navigator.clipboard?.writeText) {
      try {
        await navigator.clipboard.writeText(citation.textContent);
        copied = true;
      } catch {
        copied = fallbackCopy(citation.textContent);
      }
    } else {
      copied = fallbackCopy(citation.textContent);
    }
  } finally {
    button.removeAttribute('aria-busy');
  }

  button.classList.toggle('copied', copied);
  label.textContent = copied ? 'Copied' : 'Copy failed';
  if (status) status.textContent = copied ? 'Citation copied.' : 'Copy failed. Select and copy the citation below.';
  copyResetTimer = window.setTimeout(() => {
    button.classList.remove('copied');
    label.textContent = 'Copy';
    if (status && copied) status.textContent = '';
  }, 1800);
}

function fallbackCopy(text) {
  const previousFocus = document.activeElement;
  const textArea = document.createElement('textarea');
  textArea.value = text;
  textArea.setAttribute('readonly', '');
  textArea.style.position = 'fixed';
  textArea.style.left = '-9999px';
  document.body.appendChild(textArea);
  try {
    textArea.select();
    return document.execCommand('copy');
  } catch {
    return false;
  } finally {
    textArea.remove();
    previousFocus?.focus({ preventScroll: true });
  }
}

function scrollToTop() {
  window.scrollTo({
    top: 0,
    behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth'
  });
}

const scrollButton = document.querySelector('.scroll-to-top');
const hero = document.querySelector('.publication-hero');
if (scrollButton && hero && 'IntersectionObserver' in window) {
  const observer = new IntersectionObserver(([entry]) => {
    scrollButton.classList.toggle('visible', !entry.isIntersecting && entry.boundingClientRect.bottom < 0);
  });
  observer.observe(hero);
}
