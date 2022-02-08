# TACC Core Styles

The custom CMS code for TACC WMA Workspace Portals & Websites


## Related Repositories

- [Core CMS], the base CMS code for TACC WMA CMS Websites


## Intended Usage

The Core CMS Resources is __not__ run independently. [Core CMS] loads assets from this repo.

### Quick Start

1. _(optional)_ Make changes to `/**/static/…/src` files.
2. [Build static files][build-files] from source files via `npm run build --project=example-cms`.
3. _(to debug)_ Review respective `/**/static/…/build` files' content.
4. Use files in [Core CMS].

[build-files]: ./README.md#how-to-build-static-files

### How to Build Static Files

1. Clone this repo (already part of [Core CMS] setup).
2. Build static resources:

    ```bash
    npm run build --project=example-cms
    ```

    Where `example-cms` is the project to be run.

    (The built assets should be in `/**/static/…/build`.)


## Linting and Formatting Conventions

Not standardized. See [(internal) Formatting & Linting](https://confluence.tacc.utexas.edu/x/HoBGCw).

[Core CMS]: https://github.com/TACC/Core-CMS
