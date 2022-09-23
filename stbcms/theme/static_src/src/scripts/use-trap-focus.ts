import { useKeyboardEvent } from "./use-event";
import { qsAll } from "./qs";

function useTrapFocus(container: HTMLElement, selector: string) {
  const focusableElements = qsAll(selector);

  let focusCursor = 0;

  function increment() {
    focusCursor = focusCursor + 1 > focusableElements.length - 1 ? 0 : focusCursor + 1;
  }

  function decrement() {
    focusCursor = focusCursor - 1 < 0 ? focusableElements.length - 1 : focusCursor - 1;
  }

  return useKeyboardEvent(container, "keydown", (event) => {
    if (event.key === "Tab") {
      event.shiftKey ? decrement() : increment();
      focusableElements[focusCursor].focus();
      event.preventDefault();
    }
  });
}

export { useTrapFocus };
