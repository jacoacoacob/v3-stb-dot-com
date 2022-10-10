import { qs } from "./qs";
import { setupMobileMenu } from "./setup-mobile-menu";
import { setupToggleDarkMode } from "./setup-toggle-dark-mode";
import { setupScrollPromptButton } from "./setup-scroll-prompt-button";

const navbar = qs("#navbar")!;

const cleanupMobileMenuListeners = setupMobileMenu(navbar);
const cleanupToggleDarkmodeListeners = setupToggleDarkMode();
const cleanupScrollPromptButton = setupScrollPromptButton();

window.addEventListener("beforeunload", () => {
  cleanupMobileMenuListeners()
  cleanupToggleDarkmodeListeners();
  cleanupScrollPromptButton();
});
