/* IMPORTANT: This is required for close button of "Image Map" component, but is an independent re-usable feature */
/**
 * Activate functionality of elements with `data-focus-target` attribute
 *
 * On click (or touch) of element:
 * - If value matches ID of an element, then focus is moved to element with matching ID.
 * - If value is "none" or empty, then page focus is unset.
 */
function activateFocusTarget() {
    const focusTargeterElements = document.querySelectorAll('[data-focus-target]');

    focusTargeterElements.forEach( el => {
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
