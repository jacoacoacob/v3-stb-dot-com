import { qs } from "./qs";

function setupBreadcrumbs() {
  const isBreadcrumbs = Boolean((window as any).CMS_NAVBAR_DATA?.isBreadcrumbs);

  const wasBreadcrumbs = (function() {
    try {
      return JSON.parse(localStorage.wasBreadcrumbs || false);
    } catch (error) {
      console.error(error);
      return false
    }
  })();

  localStorage.wasBreadcrumbs = isBreadcrumbs;
  
  const bc = qs(".navbar-breadcrumbs");
  const bcListWrapper = qs(".navbar-breadcrumbs-list-wrapper");

  if (isBreadcrumbs) {
    bc.classList.add("h-6");
  }

  if (isBreadcrumbs && !wasBreadcrumbs) {
    bcListWrapper.classList.add(
      "h-0",
      "overflow-hidden",
      "transition-all",
      "duration-300",
    );
    setTimeout(() => {
      bcListWrapper.classList.remove(
        "h-0",
        "opacity-0",
      );
      bcListWrapper.classList.add(
        "h-6",
      );
    });
  }

}

export { setupBreadcrumbs };
