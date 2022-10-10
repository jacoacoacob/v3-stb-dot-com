import { qs } from "./qs";
import { useEvent } from "./use-event";
import { prefersReducedMotion } from "./prefers-reduced-motion";

function easeOut(
  currentFrame: number,
  start: number,
  distanceToTravelFromStart: number,
  totalFrames: number,
) {
  return Math.round(
    -distanceToTravelFromStart * (currentFrame /= totalFrames) * (currentFrame - 2) + start
  )
}

interface SmoothScrollOptions {
  totalFrames?: number;
  offset?: number;
  targetSelector?: string;
}

function smoothScroll(
  options: SmoothScrollOptions = {},
  callback: ((didComplete: boolean) => void)
) {
  const { totalFrames: _totalFrames, offset: _offset, targetSelector } = options;

  // There could be multiple elements that match selector or classname 'scroll-target' on the page.
  // Select the first one.
  const target = qs(targetSelector ?? ".scroll-target");

  if (!target) {
    return;
  }

  const offset = _offset ?? 0;
  const totalFrames = _totalFrames ?? 20;

  const start = window.scrollY;
  const final = target.getBoundingClientRect().top + start + offset;
  const distanceToTravelFromStart = final - start;

  let currentFrame = 0;
  let animationY = easeOut(currentFrame, start, distanceToTravelFromStart, totalFrames);
  let animationHandle: number;


  // // Disabling This seems to always immediately cancel scroll on iPhone :(
  // const [listenWindowScroll, forgetWindowScroll] = useEvent(window, "scroll", () => {
  //   // if (animationY !== window.scrollY) {
  //   //   cancelSroll(false);
  //   //   alert("HUMAN SCROLLED!")
  //   // }
  // });

  // listenWindowScroll();

  function cancelSroll(didComplete: boolean) {
    cancelAnimationFrame(animationHandle);
    // forgetWindowScroll();
    callback(didComplete);
  }

  if (prefersReducedMotion()) {
    window.scrollTo(0, final);
    return;
  }

  (function animateScroll() {
    if (currentFrame === totalFrames) {
      window.scrollTo(0, final);
      cancelSroll(true);
      return;
    }
    animationY = easeOut(currentFrame, start, distanceToTravelFromStart, totalFrames);
    window.scrollTo(0, animationY);
    currentFrame += 1;
    animationHandle = requestAnimationFrame(animateScroll);
  })();
}

function setupScrollPromptButton() {
  const scrollPromptButton = qs("#btn-scroll-prompt");

  if (!scrollPromptButton) {
    console.warn(
      "[setupScrollPromptButton] Couldn't find element using selector '#btn-scroll-prompt'"
    )
  }

  const [listenClick, forgetClick] = useEvent(
    scrollPromptButton,
    "click",
    () => {
      smoothScroll(
        {
          targetSelector: ".scroll-target",
          offset: -80,
          totalFrames: 40,
        },
        (didComplete) => {
          console.log("[SmoothScroll::didComplete]", didComplete);
        }
      );
    }
  );

  listenClick();

  return forgetClick;
}

export { setupScrollPromptButton };
