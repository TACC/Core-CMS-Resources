# Port Project

Port an existing CMS project:

- [For a Core CMS with Custom Assets](#for-a-core-cms-with-custom-assets)
- [For a Core CMS with Custom Functionality](#for-a-core-cms-with-custom-functionality)

| from | to |
| - | - |
| [Core CMS Resources]<br><sup>built **into** [Core CMS] image</sup> | [Core CMS Custom]<br><sup>built **atop** [Core CMS] image</sup> |

## For a Core CMS with Custom Assets

["Create Project" via TACC/Core-CMS-Custom.](https://github.com/TACC/Core-CMS-Custom/blob/main/README.md#create-project)

## For a Core CMS with Custom Functionality

["Create Project" via TACC/Core-CMS-Template.](https://github.com/TACC/Core-CMS-Template/blob/main/docs/create-project.md)

### Quick Guide

| move | content |
| - | - |
| from | [Core CMS Resources]:<br><sup>`/taccsite_custom/custom_project_dir`</sup> |
| to | <sub>`/custom_project_dir/src/taccsite_custom/custom_project_dir`</sub> |

| copy | settings |
| - | - |
| from | [Core Portal Deployments]:<br><sup>`/project_dir/camino/settings_custom.py`</sup> |
| to | <sub>`/custom_project_dir/src/taccsite_cms/settings_custom.py`[^1]</sub> |

| use | not |
| - | - |
| `custom`**`_`**`project`**`_`**`dir` | `custom`**`-`**`project`**`-`**`dir` |

> [!IMPORTANT]
> A valid Python application uses underscores.

[^1]: The `cms.settings_custom.py` is committed in [Core Portal Deployments]. A `settings_custom.py` in [Core CMS Custom] is `.gitignore`'d.

### Known Gotchas

#### Project Expects CSS Build Step

##### to Import [Core Styles] CSS

**If** the custom project directory expects CSS build step e.g. has

- `css/src/*.css` with `@import` of a `@tacc/core-styles/` path

Then:

1. Contact https://github.com/wesleyboar.

> **Note**
> Those `@import`s assume:
>
> - Node
> - NPM package `@tacc/core-styles`
> - a CSS build script
>
> Whether to support those here, and how to port without support for those, has not been decided.

##### to Import Internal Stylesheets

**If** the custom project directory expects CSS concatenation e.g. has

- `css/src/*.css` with `@import` of a relative path

Then:

1. Rename import paths appended with comment `Core-CMS:/taccsite_cms/…/`:
    - from `**/*.css`
    - to `/static/site_cms/css/build/*.css`
2. Rename relative import paths (e.g. `./**/*.css`):
    - from `**/*.css`
    - to `/static/custom_project_dir/css/**/*.css`
3. Add UI test steps to initial deploy of ported custom project.

#### Uses Custom CSS

**If** the custom project directory expects any CSS at all i.e. has

- a template with `<link rel="stylesheet" href="{% static`

Then:

1. Move CSS tree:
    - from `.../custom_project_dir/static/css/src/`
    - to `.../custom_project_dir/static/css/`
2. Rename `href` paths:
    - from `custom_project_dir/css/build/**/*.css`
    - to `custom_project_dir/css/**/*.css`
3. Add UI test steps to initial deploy of ported custom project.

<!-- Link Aliases -->

[Core CMS]: https://github.com/TACC/Core-CMS
[Core Styles]: https://github.com/TACC/Core-Styles
[Core CMS Custom]: https://github.com/TACC/Core-CMS-Custom
[Core CMS Resources]: https://github.com/TACC/Core-CMS-Resources
[Core Portal Deployments]: https://github.com/TACC/Core-Portal-Deployments
