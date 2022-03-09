# TACC CMS Project - Example - Static Files

Static assets[^1] specific to this project __must__ be in this directory.
Otherwise, they will be unavailable to [Core CMS] loading this project.

[^1]: Static assets like CSS, Images (`img`), Fonts, and JavaScript (`js`).

[Core CMS]: https://github.com/TACC/Core-CMS

## Directory Hierarchy

Where `name-of-project` is a CMS projects with custom static assets:

- `/name-of-project/static/name-of-project/...`

The redundancy is intentional:

- The high-level instance isolates per-project resources.
- The low-level instance [namespaces the custom static files and templates][1].

[1]: https://docs.djangoproject.com/en/2.2/intro/tutorial06/#customize-your-app-s-look-and-feel
