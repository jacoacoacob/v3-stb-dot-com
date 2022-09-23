
function qs(selector: string, element?: Element): HTMLElement | null {
  return element ? element.querySelector(selector) : document.querySelector(selector);
}

function qsAll(selector: string, element?: Element): NodeListOf<HTMLElement> {
  return element ? element.querySelectorAll(selector) : document.querySelectorAll(selector);
}

export { qs, qsAll };
