# TACC CMS Per-Site Assets - Example - Static

All static assets specific to this project __must__ be placed in this directory within a directory whose name matches the parent directory of this directory. Failure to do so will make them unavailable via [Core CMS][core-cms-repo].

[core-cms-repo]: https://gitlab.tacc.utexas.edu/wma-cms/cms-site-template

## Clarification

Where `your-project-a` and `some-project-b` are unique projects with custom resources:

- `cms-site-assets:/your-project-a/static/your-project-a/…`
- `cms-site-assets:/some-project-b/static/some-project-b/…`

The redundancy is intentional. The high-level instance isolates per-project resources. The low-level instance [namespaces static assets][djangocms-custom-assets].

[djangocms-custom-assets]: https://docs.djangoproject.com/en/2.2/intro/tutorial06/#customize-your-app-s-look-and-feel
