# TACC CMS Per-Site Resources - Example

All custom resources (assets, templates, configuration) specific to this project __must__ be placed in this directory. Failure to do so will make them unavailable via [Core CMS][core-cms-repo].

[core-cms-repo]: https://gitlab.tacc.utexas.edu/wma-cms/cms-site-template

## Configuration

### `__init__.py`

Treat directory as an app so that it can overwrite other apps. See `INSTALLED_APPS` in [`/taccsite_cms/settings.py`](/taccsite_cms/settings.py).

### `secrets.py`

Store custom configuration for this project. See [project `README.md` at "Custom Configuration"](/README.md#Custom%20Configuration).
