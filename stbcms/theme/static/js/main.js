function $2477b0e0305ba15a$export$836aee6bce45247(selector, element) {
    return element ? element.querySelector(selector) : document.querySelector(selector);
}
function $2477b0e0305ba15a$export$d32deb6b670bc3a1(selector, element) {
    return element ? element.querySelectorAll(selector) : document.querySelectorAll(selector);
}



function $f9fc0a4307b9ed89$export$90fc3a17d93f704c(elem, type, listener) {
    function setup() {
        elem.addEventListener(type, listener);
    }
    function teardown() {
        elem.removeEventListener(type, listener);
    }
    return [
        setup,
        teardown
    ];
}
function $f9fc0a4307b9ed89$export$57aaedcb6bd3df60(element, type, listener) {
    return $f9fc0a4307b9ed89$export$90fc3a17d93f704c(element, type, listener);
}




function $993b902bec18bac8$export$206640e88214a215(container, selector) {
    const focusableElements = (0, $2477b0e0305ba15a$export$d32deb6b670bc3a1)(selector);
    let focusCursor = 0;
    function increment() {
        focusCursor = focusCursor + 1 > focusableElements.length - 1 ? 0 : focusCursor + 1;
    }
    function decrement() {
        focusCursor = focusCursor - 1 < 0 ? focusableElements.length - 1 : focusCursor - 1;
    }
    return (0, $f9fc0a4307b9ed89$export$57aaedcb6bd3df60)(container, "keydown", (event)=>{
        if (event.key === "Tab") {
            event.shiftKey ? decrement() : increment();
            focusableElements[focusCursor].focus();
            event.preventDefault();
        }
    });
}


function $777da45f9e4654b7$export$933baf54561e84b4(navbar) {
    const btnMenuOpen = (0, $2477b0e0305ba15a$export$836aee6bce45247)("#mobile-menu-open");
    const btnMenuClose = (0, $2477b0e0305ba15a$export$836aee6bce45247)("#mobile-menu-close");
    const [trapFocus, releaseFocus] = (0, $993b902bec18bac8$export$206640e88214a215)(navbar, "[data-mobile-menu-focusable]");
    const menuMachine = {
        state: "closed",
        toggleState () {
            this.state = this.state === "closed" ? "open" : "closed";
            this.tick();
        },
        setState (newState) {
            this.state = newState;
            this.tick();
        },
        actions: {
            closed () {
                document.documentElement.classList.remove("mobile-menu-open");
                releaseFocus();
            },
            open () {
                document.documentElement.classList.add("mobile-menu-open");
                btnMenuClose.focus();
                trapFocus();
            }
        },
        tick () {
            this.actions[this.state]();
        }
    };
    const unlisteners = [];
    const [listenWindowFocus, unlistenWindowFocus] = (0, $f9fc0a4307b9ed89$export$90fc3a17d93f704c)(window, "focus", closeMenu);
    listenWindowFocus();
    unlisteners.push(unlistenWindowFocus);
    function closeMenu() {
        if (localStorage.locationHref !== location.href) {
            menuMachine.state = "closed";
            menuMachine.tick();
        }
        localStorage.locationHref = location.href;
    }
    closeMenu();
    [
        [
            btnMenuOpen,
            "open"
        ],
        [
            btnMenuClose,
            "closed"
        ]
    ].forEach(([element, state])=>{
        const [listen, unlisten] = (0, $f9fc0a4307b9ed89$export$90fc3a17d93f704c)(element, "click", ()=>{
            menuMachine.setState(state);
        });
        listen();
        unlisteners.push(unlisten);
    });
    function cleanupListeners() {
        unlisteners.forEach((unlisten)=>unlisten());
    }
    return cleanupListeners;
}




function $e2f8619e108b5746$export$bd9e94318d9c1a25() {
    function getIsDarkMode() {
        return localStorage.getItem("dark-mode") === "true";
    }
    function setIsDarkMode(value) {
        localStorage.setItem("dark-mode", JSON.stringify(value));
    }
    function onToggleDarkMode() {
        setIsDarkMode(!getIsDarkMode());
        updateUI();
    }
    function updateUI() {
        if (getIsDarkMode()) document.documentElement.classList.add("dark");
        else document.documentElement.classList.remove("dark");
    }
    updateUI();
    const unlisteners = [];
    (0, $2477b0e0305ba15a$export$d32deb6b670bc3a1)("[data-toggle-dark-mode]").forEach((element)=>{
        const [listen, unlisten] = (0, $f9fc0a4307b9ed89$export$90fc3a17d93f704c)(element, "click", onToggleDarkMode);
        listen();
        unlisteners.push(unlisten);
    });
    function cleanupListeners() {
        unlisteners.forEach((unlisten)=>unlisten());
    }
    return cleanupListeners;
}




function $a2f62d377d42522b$var$easeOut(currentFrame, start, distanceToTravelFromStart, totalFrames) {
    return Math.round(-distanceToTravelFromStart * (currentFrame /= totalFrames) * (currentFrame - 2) + start);
}
function $a2f62d377d42522b$var$smoothScroll(options = {}, callback) {
    const { totalFrames: _totalFrames , offset: _offset , targetSelector: targetSelector  } = options;
    // There could be multiple elements that match selector or classname 'scroll-target' on the page.
    // Select the first one.
    const target = (0, $2477b0e0305ba15a$export$836aee6bce45247)(targetSelector ?? ".scroll-target");
    if (!target) return;
    const offset = _offset ?? 0;
    const totalFrames = _totalFrames ?? 20;
    const start = window.scrollY;
    const final = target.getBoundingClientRect().top + start + offset;
    const distanceToTravelFromStart = final - start;
    let currentFrame = 0;
    let animationY = $a2f62d377d42522b$var$easeOut(currentFrame, start, distanceToTravelFromStart, totalFrames);
    let animationHandle;
    // // Disabling This seems to always immediately cancel scroll on iPhone :(
    // const [listenWindowScroll, forgetWindowScroll] = useEvent(window, "scroll", () => {
    //   // if (animationY !== window.scrollY) {
    //   //   cancelSroll(false);
    //   //   alert("HUMAN SCROLLED!")
    //   // }
    // });
    // listenWindowScroll();
    function cancelSroll(didComplete) {
        cancelAnimationFrame(animationHandle);
        // forgetWindowScroll();
        callback(didComplete);
    }
    // if (prefersReducedMotion()) {
    //   window.scrollTo(0, final);
    //   return;
    // }
    (function animateScroll() {
        if (currentFrame === totalFrames) {
            window.scrollTo(0, final);
            cancelSroll(true);
            return;
        }
        animationY = $a2f62d377d42522b$var$easeOut(currentFrame, start, distanceToTravelFromStart, totalFrames);
        window.scrollTo(0, animationY);
        currentFrame += 1;
        animationHandle = requestAnimationFrame(animateScroll);
    })();
}
function $a2f62d377d42522b$export$2a68c09ab2626bad() {
    const scrollPromptButton = (0, $2477b0e0305ba15a$export$836aee6bce45247)("#btn-scroll-prompt");
    if (!scrollPromptButton) console.warn("[setupScrollPromptButton] Couldn't find element using selector '#btn-scroll-prompt'");
    const [listenClick, forgetClick] = (0, $f9fc0a4307b9ed89$export$90fc3a17d93f704c)(scrollPromptButton, "click", ()=>{
        $a2f62d377d42522b$var$smoothScroll({
            targetSelector: ".scroll-target",
            offset: -80,
            totalFrames: 40
        }, (didComplete)=>{
            console.log("[SmoothScroll::didComplete]", didComplete);
        });
    });
    listenClick();
    return forgetClick;
}


const $1ab88a2c134b3f01$var$navbar = (0, $2477b0e0305ba15a$export$836aee6bce45247)("#navbar");
const $1ab88a2c134b3f01$var$cleanupMobileMenuListeners = (0, $777da45f9e4654b7$export$933baf54561e84b4)($1ab88a2c134b3f01$var$navbar);
const $1ab88a2c134b3f01$var$cleanupToggleDarkmodeListeners = (0, $e2f8619e108b5746$export$bd9e94318d9c1a25)();
const $1ab88a2c134b3f01$var$cleanupScrollPromptButton = (0, $a2f62d377d42522b$export$2a68c09ab2626bad)();
window.addEventListener("beforeunload", ()=>{
    $1ab88a2c134b3f01$var$cleanupMobileMenuListeners();
    $1ab88a2c134b3f01$var$cleanupToggleDarkmodeListeners();
    $1ab88a2c134b3f01$var$cleanupScrollPromptButton();
});


//# sourceMappingURL=main.js.map
