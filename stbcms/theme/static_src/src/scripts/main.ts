import { qs } from "./qs";
import { useEvent } from "./use-event";
import { useTrapFocus } from "./use-trap-focus";

function useMobileMenu(navbar: HTMLElement) {
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

  const [setupCloseMenuListener] = useEvent(
    window,
    "focus",
    closeMenu
  );

  setupCloseMenuListener()

  function closeMenu() {
    if (localStorage.locationHref !== location.href) {
      menuMachine.state = "closed";
      menuMachine.tick();
    }
    localStorage.locationHref = location.href;
  }

  closeMenu()

  btnMenuOpen?.addEventListener("click", event => {
    menuMachine.setState("open");
  });

  btnMenuClose?.addEventListener("click", event => {
    menuMachine.setState("closed");
  });
}

function useNavbar() {
  const navbar = qs("#navbar")!;

  useMobileMenu(navbar);
}

useNavbar();
