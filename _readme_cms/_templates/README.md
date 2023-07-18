# TACC CMS Project - Example - Templates

Templates specific to this project __must__ be in this directory.
Otherwise, they will be unavailable to [Core CMS] loading this project.

The directory structure here __should__ mirror [Core CMS]:
  [`/taccsite_cms/templates`][core-tpl-dir]

This consistency lets us override templates in Django fashion.

[Core CMS]: https://github.com/TACC/Core-CMS
[core-tpl-dir]: https://github.com/TACC/Core-CMS/blob/main/taccsite_cms/static/site_cms

## How to Write Template Path

Where `name_of_project` is a CMS projects with custom templates:

- `/name_of_project/templates/___.html`

### How to Overwrite Core Templates

1. Create a template of the same name here.
2. Reference the template (where needed) with the correct path.

⚠️ A project __must not__ overwrite the Core CMS `base.html`.

## Overwrite Apps or Plugins

You may overwrite apps [like Core][core-overwrite-doc].
But you msut do so relative to this directory.

[core-overwrite-doc]: https://github.com/TACC/Core-CMS/tree/main/taccsite_cms/templates/README.md#overwrite-apps-or-plugins
