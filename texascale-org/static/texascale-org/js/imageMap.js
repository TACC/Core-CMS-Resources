'use strict';

const FEATURE_CLASS_DICT = {
  hasCaptionToggleAlignement: 'c-image-map--has-caption-toggle-alignment',
  hasItemCounters: 'c-image-map--has-item-counters',
  hasToggleCounters: 'c-image-map--has-toggle-counters',
};

// TODO: Support `PropTypes`
// const ImageMapCaptionPropType = PropTypes.shape({
//   /** Unique identifier for the caption */
//   id: PropTypes.string.isRequired,
//   /** Heading for the caption */
//   title: PropTypes.string.isRequired,
//   /** Brief textual preview or summary of content */
//   summary: PropTypes.string,
//   /** Caption text or markup */
//   content: PropTypes.string.isRequired,
//   /** Whether caption value is markup */
//   contentIsMarkup: PropTypes.bool
// });

/**
 * Return array of class names for features matched in given dictionaries
 * @param {Object.<*, String>} featureClassDict - Dictionary of classNames for features
 * @param {Object.<*, Boolean>} featureToggleDict - Dictionary of features and whether each is active
 */
function getFeatureClassNames(featureClassDict, featureToggleDict) {
  const classNames = [];

  Object.keys(featureClassDict).forEach(property => {
    if (featureToggleDict[ property ]) {
      classNames.push(featureClassDict[ property ]);
    }
  });

  return classNames;
}

/**
 * An image map with nodes; click nodes to show or highlight captions
 *
 * @example
 * // A minimal-requirements "Sample Widget" image map
 * const captions: [
 *   { id, title, summary, content }
 * }];
 * <ImageMap
 *   id="sample-widget"
 *   captions={captions}
 *   image="/path/file.ext"
 * >
 * @example
 * // A "Sample Widget" image map with all features
 * const captions: [
 *   { id, title, summary, content },
 *   { id, title, summary, content },
 *   { id, title, summary, content, contentIsMarkup: true }
 * }];
 * React.render(<ImageMap
 *   id="sample-widget"
 *   image="/path/file.ext"
 *   captions={captions}
 *   hasToggleCounterAlignment
 *   hasToggleCounters
 *   hasItemCounters
 * >);
 */
function ImageMap({
  captions,
  className,
  id,
  image,
  ...props
}) {
  // TODO: Support `PropTypes`
  className = className || '';

  const classModifierNameList = getFeatureClassNames(FEATURE_CLASS_DICT, props);
  const classNames = classModifierNameList.join(' ') + ' ' + className;
  const rootClassName = 'c-image-map';

  return (
    <article
      id={id}
      className={rootClassName + ' ' + classNames}
    >
      <a
        href="#_"
        className="c-image-map__image"
      >
          <img className="c-image-map__image" src={image} />
      </a>
      {/* The `#_` un-targets all elements, and does not cause page scroll */}
      {/* If anyone complains about the ugly URL, then hide the hash */}
      {/* SEE: https://gist.github.com/azu/36ba5a80feb857c77a3a) */}
      {captions.map(caption => (
        <div
          id={caption.id}
          key={caption.id}
          className="c-image-map__item"
        >
          <a
            className="c-image-map__item-toggle"
            tabIndex="0"
          >
              <span className="sr-only">Learn about this area</span>
          </a>
          <div
            className="c-image-map__item-caption"
            tabIndex="-1"
          >
            <strong
              className="c-image-map__item-title"
              data-placeholder-text={caption.summary}
            >
              {caption.title}
            </strong>
            {(caption.contentIsMarkup) ? (
              <p className="c-image-map__item-desc" dangerouslySetInnerHTML={{
                __html: caption.content
              }} />
            ) : (
              <p className="c-image-map__item-desc">
                {caption.content}
              </p>
            )}
            <button
              className="c-image-map__item-close"
              data-focus-target="none"
            >
              <span className="sr-only">Close this description</span>
            </button>
          </div>
        </div>
      ))}
    </article>
  );
}
// TODO: Support `PropTypes`
// ImageMap.propTypes = {
//   /** Additional className for the root element */
//   className: PropTypes.string,
//   /** Caption data */
//   captions: PropTypes.arrayOf(ImageMapCaptionPropType).isRequired,
//   /** ID for the root element */
//   id: PropTypes.string.isRequired,
//   /** Whether captions and toggles should be aligned */
//   hasCaptionToggleAlignement: PropTypes.bool,
//   /** Whether items captions should have counters */
//   hasItemCounters: PropTypes.bool,
//   /** Whether toggles should have counters */
//   hasToggleCounters: PropTypes.bool,
// };
// ImageMap.defaultProps = {
//   className: '',
//   hasCaptionToggleAlignement: false,
//   hasItemCounters: false,
//   hasToggleCounters: false,
// };

/**
 * Render an Image Map into each specified placeholder
 *
 * @example
 * // A minimal-requirements "Sample Widget" image map
 * <script>
 *   window.imageMapProps['sample-data'] = {
 *     captions: [
 *       { id, title, summary, content }
 *     }],
 *     image: '/path/file.ext'
 *   };
 * </script>
 * <div data-component="image-map" data-id="sample-widget"></div>
 * @example
 * // A "Sample Widget" image map with all features
 * <script>
 *   window.imageMapProps['sample-data'] = {
 *     captions: [
 *       { id, title, summary, content },
 *       { id, title, summary, content },
 *       { id, title, summary, content, contentIsMarkup: true }
 *     }],
 *     image: '/path/file.ext',
 *     hasCaptionToggleAlignement: true,
 *     hasItemCounters: true,
 *     hasToggleCounters: true,
 *   };
 * </script>
 * <div data-component="image-map" data-id="sample-widget"></div>
 */
function populateImageMapComponents() {
  document.querySelectorAll('[data-component="image-map"]').forEach(element => {
    const id = element.dataset.id;
    const props = window.imageMapProps[id];

    window.ReactDOM.render(
      window.React.createElement(ImageMap, {id, ...props}),
      element
    );
  });
}
populateImageMapComponents();
