
function useEvent<EventType extends Event>(elem: Element | Window | Document, type: string, listener: (event: EventType) => void) {
  function setup() {
    elem.addEventListener(type, listener as EventListener);
  }

  function teardown() {
    elem.removeEventListener(type, listener as EventListener);
  }

  return [setup, teardown]
}

function useKeyboardEvent(element: Element, type: string, listener: (event: KeyboardEvent) => void) {
  return useEvent<KeyboardEvent>(element, type, listener);
}

export { useEvent, useKeyboardEvent };
