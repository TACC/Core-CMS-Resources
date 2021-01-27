# TACC CMS Per-Site Resources - Example - Templates

All templates specific to this CMS project __must__ be placed in this directory. Failure to do so will make them unavailable via [Core CMS][core-cms-repo].

[core-cms-repo]: https://gitlab.tacc.utexas.edu/wma-cms/cms-site-template

## Page Templates

Projects may make templates available as page templates for CMS editors, via this directory, _similar_ to the Core. See [Core `templates/README.md` at "Page Templates"](/taccsite_cms/templates/README.md#Page%20Templates).

### Template Path

To register or load (extend, include, etc) project-specific templates, you must use the path `__PROJECT__/templates/__TEMPLATE__.html`.

### Overwrite Core Templates

To overwrite Core templates, you may create a template of the same name template here, but must register it with the project-specific template path.

> __Important__: A project can __not__ overwrite the Core CMS `base.html`.

## Overwrite Apps or Plugins

Projects may overwrite apps/plugins, via this directory, just like the Core. See [Core `templates/README.md` at "Overwrite Plugins"](/taccsite_cms/templates/README.md#Overwrite%20or%20Plugins).
