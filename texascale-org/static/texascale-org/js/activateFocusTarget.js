/**
 * Focus on target (by ID) on click of `data-focus-target`-attribute elements
 *
 * On click (or touch, or keypress) of element:
 * - If value matches ID of an element, then focus is moved to element with matching ID.
 * - If value is "none" or empty, then page focus is unset.
 *
 * WARNING: Do NOT use this on `<a>` (anchor) elements to link to section of a page. Instead use `<a href="#some-heading">Some Heading</a>`.
 * @example
 * <!-- Remove hash-based focus -->
 * <button data-focus-target="none">Close</button>
 * @example
 * <!-- Set/Change hash-based focus -->
 * <button data-focus-target="relevant-field">Skip to "Relevant Field"</button>
 * ...
 * <label for="relevant-field">Relevant Field</label>
 * <input id="relevant-field" ... />
 */
function activateFocusTarget() {
    const focusTargeterElements = document.querySelectorAll('[data-focus-target]');

    focusTargeterElements.forEach( el => {
        /* TODO: For `<a>` (anchor) elements, abort and log error or warning */
        el.addEventListener('click', ( event ) => {
            const focusTarget = event.currentTarget.dataset.focusTarget;

            if (focusTarget === 'none' || focusTarget === '') {
                document.activeElement.blur();
                // Unset target via URL hash, but do not let page scroll
                // If anyone complains about the ugly URL, then [hide the hash](https://gist.github.com/azu/36ba5a80feb857c77a3a)
                // SEE: https://makandracards.com/makandra/17147-howto-remove-the-location-hash-without-causing-the-page-to-scroll
                window.location.hash = "_";
            } else {
                window.location.hash = focusTarget
            }
        });
    });
}
activateFocusTarget();
