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



function $2863376820e24a25$export$24c208de4fde1b2a() {
    var _a;
    var isBreadcrumbs = Boolean((_a = window.CMS_NAVBAR_DATA) === null || _a === void 0 ? void 0 : _a.isBreadcrumbs);
    var wasBreadcrumbs = function() {
        try {
            return JSON.parse(localStorage.wasBreadcrumbs || false);
        } catch (error) {
            console.error(error);
            return false;
        }
    }();
    localStorage.wasBreadcrumbs = isBreadcrumbs;
    var bc = (0, $ad7d1ff078b161d2$export$836aee6bce45247)(".navbar-breadcrumbs");
    var bcListWrapper = (0, $ad7d1ff078b161d2$export$836aee6bce45247)(".navbar-breadcrumbs-list-wrapper");
    if (isBreadcrumbs) bc.classList.add("h-6");
    if (isBreadcrumbs && !wasBreadcrumbs) {
        bcListWrapper.classList.add("h-0", "overflow-hidden", "transition-all", "duration-300");
        setTimeout(function() {
            bcListWrapper.classList.remove("h-0", "opacity-0");
            bcListWrapper.classList.add("h-6");
        });
    }
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


var $65e27a733c7607bf$var$navbar = (0, $ad7d1ff078b161d2$export$836aee6bce45247)("#navbar");
(0, $2863376820e24a25$export$24c208de4fde1b2a)();
var $65e27a733c7607bf$var$cleanupMobileMenuListeners = (0, $41ec8bf5c226cc99$export$933baf54561e84b4)($65e27a733c7607bf$var$navbar);
var $65e27a733c7607bf$var$cleanupToggleDarkmodeListeners = (0, $0266d94240c51ce7$export$bd9e94318d9c1a25)();
window.addEventListener("beforeunload", function() {
    $65e27a733c7607bf$var$cleanupMobileMenuListeners();
    $65e27a733c7607bf$var$cleanupToggleDarkmodeListeners();
});


//# sourceMappingURL=main.js.map
