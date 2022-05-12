# TACC CMS Project - Example - Templates

You may overwrite Core CMS templates and 3rd-party apps/plugin templates.

## Page Templates

To make new templates available as page templates for CMS editors, replace or add to `CMS_TEMPLATES` setting.

## Overwrite Core

1. Create a template of the same name as the [Core CMS template][core-tpl-dir] to overwrite.
2. Replace or extend the content of the overwritten template.

## Overwrite Apps or Plugins

Follow [Core CMS instructions][core-tpl-doc], but within _this_ directory instead.

[core-tpl-dir]: https://github.com/TACC/Core-CMS/blob/main/taccsite_cms/static/site_cms
[core-tpl-doc]: https://github.com/TACC/Core-CMS/tree/main/taccsite_cms/templates
