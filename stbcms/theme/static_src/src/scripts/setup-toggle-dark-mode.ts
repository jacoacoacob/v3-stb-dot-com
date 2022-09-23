import { qsAll } from "./qs";
import { useEvent } from "./use-event";

function setupToggleDarkMode() {

  function getIsDarkMode() {
    return localStorage.getItem("dark-mode") === "true";
  }

  function setIsDarkMode(value: boolean) {
    localStorage.setItem("dark-mode", JSON.stringify(value));
  }

  function onToggleDarkMode() {
    setIsDarkMode(!getIsDarkMode());
    updateUI();
  }

  function updateUI() {
    if (getIsDarkMode()) {
      document.documentElement.classList.add("dark");
    } else {
      document.documentElement.classList.remove("dark");
    }
  }

  updateUI();

  const unlisteners: (() => void)[] = [];

  qsAll("[data-toggle-dark-mode]").forEach(element => {
    const [listen, unlisten] = useEvent(element, "click", onToggleDarkMode);
    listen();
    unlisteners.push(unlisten);
  });

  function cleanupListeners() {
    unlisteners.forEach(unlisten => unlisten());
  }

  return cleanupListeners;
}

export { setupToggleDarkMode };
