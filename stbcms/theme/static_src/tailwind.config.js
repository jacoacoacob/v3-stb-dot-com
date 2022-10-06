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
                        "--tw-prose-body": theme("colors.slate[900]"),
                        "--tw-prose-headings": theme("colors.slate[800]"),
                        "--tw-prose-counters": theme("colors.slate[700]"),
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
                white: {
                    css: {
                        "--tw-prose-body": theme("colors.white"),
                        "--tw-prose-headings": theme("colors.white"),
                        // "--tw-prose-lead": theme("colors.pink[700]"),
                        // "--tw-prose-links": theme("colors.pink[900]"),
                        // "--tw-prose-bold": theme("colors.pink[900]"),
                        "--tw-prose-counters": theme("colors.slate[200]"),
                        "--tw-prose-bullets": theme("colors.pink[200]"),
                        "--tw-prose-hr": theme("colors.pink[300]"),
                        "--tw-prose-quotes": theme("colors.pink[900]"),
                        "--tw-prose-quote-borders": theme("colors.pink[300]"),
                        "--tw-prose-captions": theme("colors.pink[700]"),
                        "--tw-prose-code": theme("colors.pink[900]"),
                        "--tw-prose-pre-code": theme("colors.pink[100]"),
                        "--tw-prose-pre-bg": theme("colors.pink[900]"),
                        "--tw-prose-th-borders": theme("colors.pink[300]"),
                        "--tw-prose-td-borders": theme("colors.pink[200]"),
                        "--tw-prose-invert-body": theme("colors.pink[200]"),
                        "--tw-prose-invert-headings": theme("colors.white"),
                        "--tw-prose-invert-lead": theme("colors.pink[300]"),
                        "--tw-prose-invert-links": theme("colors.white"),
                        "--tw-prose-invert-bold": theme("colors.white"),
                        "--tw-prose-invert-counters": theme("colors.pink[400]"),
                        "--tw-prose-invert-bullets": theme("colors.pink[600]"),
                        "--tw-prose-invert-hr": theme("colors.pink[700]"),
                        "--tw-prose-invert-quotes": theme("colors.pink[100]"),
                        "--tw-prose-invert-quote-borders": theme("colors.pink[700]"),
                        "--tw-prose-invert-captions": theme("colors.pink[400]"),
                        "--tw-prose-invert-code": theme("colors.white"),
                        "--tw-prose-invert-pre-code": theme("colors.pink[300]"),
                        "--tw-prose-invert-pre-bg": "rgb(0 0 0 / 50%)",
                        "--tw-prose-invert-th-borders": theme("colors.pink[600]"),
                        "--tw-prose-invert-td-borders": theme("colors.pink[700]"),
                        a: {
                            transition: "box-shadow .1s ease",
                            color: theme("colors.slate.100"),
                            textDecoration: "none",
                            boxShadow: `inset 0 -2px ${theme("colors.teal.300")}`,
                            "&:hover": {
                                boxShadow: `inset 0 -6px ${theme("colors.teal.300")}`
                            },
                            "&:focus": {
                                outline: "none",
                                boxShadow: `inset 0 -6px ${theme("colors.teal.300")}`
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
