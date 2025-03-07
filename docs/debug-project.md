# Debug Project

## Verify Images Are Collected

1. Review content of `/taccsite_custom/custom_project_dir/static/custom_project_dir/img`.
2. Verify that content is also _in the container_ at `/static/custom_project_dir/img`.

## Verify CSS Build Output

1. Review content of `/taccsite_custom/custom_project_dir/static/custom_project_dir/css/build`.
2. Verify that content is also _in the container_ at `/static/custom_project_dir/css/build`.

> **Note**
> You will never see `/static/*/css/src`, because [this app ignores `src/`][ignore-src-dirs] when [collecting static files](#collect-static-files). This is done so templates can **not** load load source files.

[ignore-src-dirs]: https://github.com/TACC/Core-CMS/blob/7b62db1/taccsite_cms/django/contrib/staticfiles_custom/apps.py

## Restart CMS Server

See [How to Restart the CMS Server](https://github.com/TACC/Core-CMS/wiki/How-to-Restart-the-CMS-Server).

## Build Search Index

See [How to Build Search Index](https://github.com/TACC/Core-CMS/wiki/How-to-Build-Search-Index).
