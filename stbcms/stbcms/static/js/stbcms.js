
/**
 * 
 * @param {string} selector 
 * @returns {HTMLElement | undefined}
 */
function qs(selector) {
  return document.querySelector(selector);
}

/**
 * 
 * @param {HTMLElement} element 
 * @param {string} event 
 * @param {((event: Event | MouseEvent | KeyboardEvent) => void)} listener 
 * @returns 
 */
 function useEventListener(element, event, listener) {
  function setup() {
    element.addEventListener(event, listener);
  }

  function teardown() {
    element.removeEventListener(event, listener);
  }

  return [setup, teardown]
}

/**
 * 
 * @param {HTMLElement} container 
 */
function useTrapFocus(container, selector) {
  const focusableElements = container.querySelectorAll(selector);

  let focusCursor = 0;

  function increment() {
    focusCursor = focusCursor + 1 > focusableElements.length - 1 ? 0 : focusCursor + 1;
  }

  function decrement() {
    focusCursor = focusCursor - 1 < 0 ? focusableElements.length - 1 : focusCursor - 1;
  }

  return useEventListener(container, "keydown", (event) => {
    if (event.key === "Tab") {
      event.shiftKey ? decrement() : increment();
      focusableElements[focusCursor].focus();
      event.preventDefault();
    }
  });
}


function useMobileMenu(navbar) {
  const btnMenuOpen = qs("#mobile-menu-open");
  const btnMenuClose = qs("#mobile-menu-close");

  const [trapFocus, releaseFocus] = useTrapFocus(navbar, "[data-mobile-menu-focusable='true']");

  const menuMachine = {
    state: "closed",
    toggleState() {
      this.state = this.state === "closed" ? "open" : "closed";
      this.tick();
    },
    setState(newState) {
      this.state = newState;
      this.tick();
    },
    actions: {
      closed() {
        document.documentElement.classList.remove(
          "mobile-menu-open"
        );
        releaseFocus();
      },
      open() {
        document.documentElement.classList.add(
          "mobile-menu-open"
        );
        trapFocus();
      },
    },
    tick() {
      this.actions[this.state]()
    },
  };

  const [setupCloseMenuListener] = useEventListener(
    window,
    "focus",
    closeMenu
  );

  setupCloseMenuListener()

  function closeMenu(event) {
    if (localStorage.locationHref !== location.href) {
      menuMachine.state = "closed";
      menuMachine.tick();
    }
    localStorage.locationHref = location.href;
  }

  closeMenu()

  btnMenuOpen.addEventListener("click", event => {
    menuMachine.setState("open");
  });

  btnMenuClose.addEventListener("click", event => {
    menuMachine.setState("closed");
  });
}

function useNavbar() {
  const navbar = qs("#navbar");

  useMobileMenu(navbar);
}

useNavbar();
