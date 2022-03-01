# TACC Example CMS

All custom resources (assets, templates, configuration) specific to this project __must__ be placed in this directory. Failure to do so will make them unavailable to [Core CMS].

## Configuration

### `__init__.py`

Treat directory as an app so that it can overwrite other apps. See `INSTALLED_APPS` in [`/taccsite_cms/settings.py`](/taccsite_cms/settings.py).

### `settings_custom.py`

Store custom configuration for this project. See [project `README.md` at "Code Configuration"](/README.md#code-configuration).


<!-- Link Aliases -->

[Core CMS]: https://github.com/TACC/Core-CMS
