import { qs } from "./qs";
import { useEvent } from "./use-event";
import { useTrapFocus } from "./use-trap-focus";

function setupMobileMenu(navbar: HTMLElement) {
  const btnMenuOpen = qs("#mobile-menu-open");
  const btnMenuClose = qs("#mobile-menu-close");

  const [trapFocus, releaseFocus] = useTrapFocus(navbar, "[data-mobile-menu-focusable='true']");

  const menuMachine = {
    state: "closed",
    toggleState() {
      this.state = this.state === "closed" ? "open" : "closed";
      this.tick();
    },
    setState(newState: "open" | "closed") {
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
      this.actions[this.state as "closed" | "open"]()
    },
  };

  const unlisteners: (() => void)[] = [] 

  const [listenWindowFocus, unlistenWindowFocus] = useEvent(
    window,
    "focus",
    closeMenu
  );

  listenWindowFocus()

  unlisteners.push(unlistenWindowFocus);

  function closeMenu() {
    if (localStorage.locationHref !== location.href) {
      menuMachine.state = "closed";
      menuMachine.tick();
    }
    localStorage.locationHref = location.href;
  }

  closeMenu();

  ([[btnMenuOpen, "open"], [btnMenuClose, "closed"]] as [HTMLElement, "open" | "closed"][]).forEach(
    ([element, state]) => {
      const [listen, unlisten] = useEvent(element, "click", () => {
        menuMachine.setState(state);
      });
      listen();
      unlisteners.push(unlisten);
    })

  function cleanupListeners() {
    unlisteners.forEach(unlisten => unlisten());
  }

  return cleanupListeners;
}

export { setupMobileMenu };
