
function qs(selector: string): HTMLElement | null {
  return document.querySelector(selector);
}

function qsAll(selector: string): NodeListOf<HTMLElement> {
  return document.querySelectorAll(selector);
}

export { qs, qsAll };
