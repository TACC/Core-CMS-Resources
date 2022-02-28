# TACC CMS Per-Site Resources

The custom CMS code for TACC WMA Workspace Portals & Websites


## Related Repositories

- [Core CMS], the base CMS code for TACC WMA CMS Websites


## Intended Usage

The Core CMS Resources is __not__ run independently. [Core CMS] loads assets from this repo.

### Quick Start

1. _(optional)_ Make changes to `/**/static/…/src` files.
2. [Build static files][build-files] from source files via `yarn build --project=example-cms`.
3. _(to debug)_ Review respective `/**/static/…/build` files' content.
4. Use files in [Core CMS].

### How to Build Static Files

1. Clone this repo (already part of [Core CMS] setup).
2. Build static resources:

    ```bash
    yarn build --project=example-cms
    ```

    Where `example-cms` is the project to be run.

    (The built assets should be in `/**/static/…/build`.)


## Linting and Formatting Conventions

Not standardized. See [(internal) Formatting & Linting](https://confluence.tacc.utexas.edu/x/HoBGCw).


## Testing

Pattern testing is done manually. The process is not documented. See [Pattern Library research].


## Deployment Steps

1. Update version in `package.json`.
2. Run `yarn update-version`.
3. Commit and push the change.
4. Deploy with CMS (see [Core-CMS README] deployment steps).


## Contributing

### Development Workflow

We use a modifed version of [GitFlow](https://datasift.github.io/gitflow/IntroducingGitFlow.html) as our development workflow. Our [development site](https://dev.cep.tacc.utexas.edu) (accessible behind the TACC Network) is always up-to-date with `main`, while the [production site](https://prod.cep.tacc.utexas.edu) is built to a hashed commit tag.
- Feature branches contain major updates, bug fixes, and hot fixes with respective branch prefixes:
    - `task/` for features and updates
    - `bug/` for bugfixes
    - `fix/` for hotfixes

### Best Practices

Sign your commits ([see this link](https://help.github.com/en/github/authenticating-to-github/managing-commit-signature-verification) for help)

### Resources

- [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)


<!-- Link Aliases -->

[build-files]: ./README.md#how-to-build-static-files

[Pattern Library research]: https://confluence.tacc.utexas.edu/x/FADMBQ

[Core CMS]: https://github.com/TACC/Core-CMS
[Core-CMS README]: https://github.com/TACC/Core-CMS/blob/main/README.md
