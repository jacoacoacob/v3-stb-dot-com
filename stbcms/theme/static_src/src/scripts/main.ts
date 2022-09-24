import { qs } from "./qs";
import { setupMobileMenu } from "./setup-mobile-menu";
// import { setupBreadcrumbs } from "./setup-breadcrumbs";
import { setupToggleDarkMode } from "./setup-toggle-dark-mode";

const navbar = qs("#navbar")!;

// setupBreadcrumbs();
const cleanupMobileMenuListeners = setupMobileMenu(navbar);
const cleanupToggleDarkmodeListeners = setupToggleDarkMode();

window.addEventListener("beforeunload", () => {
  cleanupMobileMenuListeners()
  cleanupToggleDarkmodeListeners();
});
