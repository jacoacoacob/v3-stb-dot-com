function $ad7d1ff078b161d2$export$836aee6bce45247(selector, element) {
    return element ? element.querySelector(selector) : document.querySelector(selector);
}
function $ad7d1ff078b161d2$export$d32deb6b670bc3a1(selector, element) {
    return element ? element.querySelectorAll(selector) : document.querySelectorAll(selector);
}



function $e0f7025c70ae0285$export$90fc3a17d93f704c(elem, type, listener) {
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
function $e0f7025c70ae0285$export$57aaedcb6bd3df60(element, type, listener) {
    return $e0f7025c70ae0285$export$90fc3a17d93f704c(element, type, listener);
}




function $fb83284f3c7078af$export$206640e88214a215(container, selector) {
    var focusableElements = (0, $ad7d1ff078b161d2$export$d32deb6b670bc3a1)(selector);
    var focusCursor = 0;
    function increment() {
        focusCursor = focusCursor + 1 > focusableElements.length - 1 ? 0 : focusCursor + 1;
    }
    function decrement() {
        focusCursor = focusCursor - 1 < 0 ? focusableElements.length - 1 : focusCursor - 1;
    }
    return (0, $e0f7025c70ae0285$export$57aaedcb6bd3df60)(container, "keydown", function(event) {
        if (event.key === "Tab") {
            event.shiftKey ? decrement() : increment();
            focusableElements[focusCursor].focus();
            event.preventDefault();
        }
    });
}


function $41ec8bf5c226cc99$export$933baf54561e84b4(navbar) {
    var btnMenuOpen = (0, $ad7d1ff078b161d2$export$836aee6bce45247)("#mobile-menu-open");
    var btnMenuClose = (0, $ad7d1ff078b161d2$export$836aee6bce45247)("#mobile-menu-close");
    var _a = (0, $fb83284f3c7078af$export$206640e88214a215)(navbar, "[data-mobile-menu-focusable]"), trapFocus = _a[0], releaseFocus = _a[1];
    var menuMachine = {
        state: "closed",
        toggleState: function() {
            this.state = this.state === "closed" ? "open" : "closed";
            this.tick();
        },
        setState: function(newState) {
            this.state = newState;
            this.tick();
        },
        actions: {
            closed: function() {
                document.documentElement.classList.remove("mobile-menu-open");
                releaseFocus();
            },
            open: function() {
                document.documentElement.classList.add("mobile-menu-open");
                btnMenuClose.focus();
                trapFocus();
            }
        },
        tick: function() {
            this.actions[this.state]();
        }
    };
    var unlisteners = [];
    var _b = (0, $e0f7025c70ae0285$export$90fc3a17d93f704c)(window, "focus", closeMenu), listenWindowFocus = _b[0], unlistenWindowFocus = _b[1];
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
    ].forEach(function(_a) {
        var element = _a[0], state = _a[1];
        var _b = (0, $e0f7025c70ae0285$export$90fc3a17d93f704c)(element, "click", function() {
            menuMachine.setState(state);
        }), listen = _b[0], unlisten = _b[1];
        listen();
        unlisteners.push(unlisten);
    });
    function cleanupListeners() {
        unlisteners.forEach(function(unlisten) {
            return unlisten();
        });
    }
    return cleanupListeners;
}




function $0266d94240c51ce7$export$bd9e94318d9c1a25() {
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
    var unlisteners = [];
    (0, $ad7d1ff078b161d2$export$d32deb6b670bc3a1)("[data-toggle-dark-mode]").forEach(function(element) {
        var _a = (0, $e0f7025c70ae0285$export$90fc3a17d93f704c)(element, "click", onToggleDarkMode), listen = _a[0], unlisten = _a[1];
        listen();
        unlisteners.push(unlisten);
    });
    function cleanupListeners() {
        unlisteners.forEach(function(unlisten) {
            return unlisten();
        });
    }
    return cleanupListeners;
}




function $e22c93a6ed734f5d$export$ff7706047246b98b() {
    return window.matchMedia("(prefers-reduced-motion: reduce)").matches;
}


function $55c867f00d864efb$var$easeOut(currentFrame, start, distanceToTravelFromStart, totalFrames) {
    return Math.round(-distanceToTravelFromStart * (currentFrame /= totalFrames) * (currentFrame - 2) + start);
}
function $55c867f00d864efb$var$smoothScroll(options, callback) {
    if (options === void 0) options = {};
    var _totalFrames = options.totalFrames, _offset = options.offset, targetSelector = options.targetSelector;
    // There could be multiple elements that match selector or classname 'scroll-target' on the page.
    // Select the first one.
    var target = (0, $ad7d1ff078b161d2$export$836aee6bce45247)(targetSelector !== null && targetSelector !== void 0 ? targetSelector : ".scroll-target");
    if (!target) return;
    var offset = _offset !== null && _offset !== void 0 ? _offset : 0;
    var totalFrames = _totalFrames !== null && _totalFrames !== void 0 ? _totalFrames : 20;
    var start = window.scrollY;
    var final = target.getBoundingClientRect().top + start + offset;
    var distanceToTravelFromStart = final - start;
    var currentFrame = 0;
    var animationY = $55c867f00d864efb$var$easeOut(currentFrame, start, distanceToTravelFromStart, totalFrames);
    var animationHandle;
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
    if ((0, $e22c93a6ed734f5d$export$ff7706047246b98b)()) {
        window.scrollTo(0, final);
        return;
    }
    (function animateScroll() {
        if (currentFrame === totalFrames) {
            window.scrollTo(0, final);
            cancelSroll(true);
            return;
        }
        animationY = $55c867f00d864efb$var$easeOut(currentFrame, start, distanceToTravelFromStart, totalFrames);
        window.scrollTo(0, animationY);
        currentFrame += 1;
        animationHandle = requestAnimationFrame(animateScroll);
    })();
}
function $55c867f00d864efb$export$2a68c09ab2626bad() {
    var scrollPromptButton = (0, $ad7d1ff078b161d2$export$836aee6bce45247)("#btn-scroll-prompt");
    if (!scrollPromptButton) console.warn("[setupScrollPromptButton] Couldn't find element using selector '#btn-scroll-prompt'");
    var _a = (0, $e0f7025c70ae0285$export$90fc3a17d93f704c)(scrollPromptButton, "click", function() {
        $55c867f00d864efb$var$smoothScroll({
            targetSelector: ".scroll-target",
            offset: -80,
            totalFrames: 40
        }, function(didComplete) {
            console.log("[SmoothScroll::didComplete]", didComplete);
        });
    }), listenClick = _a[0], forgetClick = _a[1];
    listenClick();
    return forgetClick;
}


var $65e27a733c7607bf$var$navbar = (0, $ad7d1ff078b161d2$export$836aee6bce45247)("#navbar");
var $65e27a733c7607bf$var$cleanupMobileMenuListeners = (0, $41ec8bf5c226cc99$export$933baf54561e84b4)($65e27a733c7607bf$var$navbar);
var $65e27a733c7607bf$var$cleanupToggleDarkmodeListeners = (0, $0266d94240c51ce7$export$bd9e94318d9c1a25)();
var $65e27a733c7607bf$var$cleanupScrollPromptButton = (0, $55c867f00d864efb$export$2a68c09ab2626bad)();
window.addEventListener("beforeunload", function() {
    $65e27a733c7607bf$var$cleanupMobileMenuListeners();
    $65e27a733c7607bf$var$cleanupToggleDarkmodeListeners();
    $65e27a733c7607bf$var$cleanupScrollPromptButton();
});


//# sourceMappingURL=main.js.map
