/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */
/** @type {import("tailwindcss").Config} */
module.exports = {
    darkMode: "class",
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        "./templates/**/*.html",

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        extend: {
            typography: ({ theme }) => ({
                DEFAULT: {
                    css: {
                        maxWidth: theme("maxWidth.2xl"),
                        a: {
                            transition: "box-shadow .1s ease",
                            color: theme("colors.slate.700"),
                            textDecoration: "none",
                            boxShadow: `inset 0 -2px ${theme("colors.green.400")}`,
                            "&:hover": {
                                boxShadow: `inset 0 -6px ${theme("colors.green.400")}`
                            },
                            "&:focus": {
                                outline: "none",
                                boxShadow: `inset 0 -6px ${theme("colors.green.400")}`
                            },
                        }
                    }
                },
                invert: {
                    css: {
                        a: {
                            transition: "box-shadow .1s ease",
                            color: theme("colors.slate.200"),
                            textDecoration: "none",
                            boxShadow: `inset 0 -2px ${theme("colors.green.600")}`,
                            "&:hover": {
                                boxShadow: `inset 0 -6px ${theme("colors.green.600")}`
                            },
                            "&:focus": {
                                outline: "none",
                                boxShadow: `inset 0 -6px ${theme("colors.green.600")}`
                            },
                        }
                    }
                }
            })
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
