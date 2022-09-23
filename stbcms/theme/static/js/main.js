function $ad7d1ff078b161d2$export$836aee6bce45247(selector) {
    return document.querySelector(selector);
}
function $ad7d1ff078b161d2$export$d32deb6b670bc3a1(selector) {
    return document.querySelectorAll(selector);
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


function $65e27a733c7607bf$var$useMobileMenu(navbar) {
    var btnMenuOpen = (0, $ad7d1ff078b161d2$export$836aee6bce45247)("#mobile-menu-open");
    var btnMenuClose = (0, $ad7d1ff078b161d2$export$836aee6bce45247)("#mobile-menu-close");
    var _a = (0, $fb83284f3c7078af$export$206640e88214a215)(navbar, "[data-mobile-menu-focusable='true']"), trapFocus = _a[0], releaseFocus = _a[1];
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
    var setupCloseMenuListener = (0, $e0f7025c70ae0285$export$90fc3a17d93f704c)(window, "focus", closeMenu)[0];
    setupCloseMenuListener();
    function closeMenu() {
        if (localStorage.locationHref !== location.href) {
            menuMachine.state = "closed";
            menuMachine.tick();
        }
        localStorage.locationHref = location.href;
    }
    closeMenu();
    btnMenuOpen === null || btnMenuOpen === void 0 || btnMenuOpen.addEventListener("click", function(event) {
        menuMachine.setState("open");
    });
    btnMenuClose === null || btnMenuClose === void 0 || btnMenuClose.addEventListener("click", function(event) {
        menuMachine.setState("closed");
    });
}
function $65e27a733c7607bf$var$useNavbar() {
    var navbar = (0, $ad7d1ff078b161d2$export$836aee6bce45247)("#navbar");
    $65e27a733c7607bf$var$useMobileMenu(navbar);
}
$65e27a733c7607bf$var$useNavbar();


//# sourceMappingURL=main.js.map
