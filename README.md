# Core-CMS-Resources

Project-specific code built into the [Core CMS] project

> **Note**
> You need not clone this repo to work on a CMS project. Work on it directly within [Core CMS] as a [Git submodule][Git Submodules].

> **Warning**
> This repository is deprecated. To work on these projects further, first [migrate them to Core CMS Custom](#port-project).[^1]

[^1]: Deploying websites that are still in Core-CMS-Resources **and** have [old custom templates will trigger a major problem](https://github.com/TACC/Core-CMS-Resources/pull/176#issuecomment-1603194690). The prefered solution is [migration](#port-project). If you must deploy without migration, then [upgrade the website for Core-CMS v3.12](./docs/upgrade-project.md#for-core-cms-v312).

## Table of Contents

- [Related Repositories](#related-repositories)
- [Project Websites](#project-websites)
- [Project Architecture](#project-architecture)
- [Prerequisites](#prerequisites)
- [Start Project](#start-project)
- [Update Project](#update-project)
- [Run Project](#run-project)
- [Debug Project](#debug-project)
- [Build & Deploy Project](#build--deploy-project)
- [Port Project](#port-project)

## Related Repositories

- [Core CMS], the base CMS code for TACC WMA CMS Websites
- [Core CMS Custom], the custom CMS code (new solution) for TACC WMA CMS Websites

## Project Websites

| Abbr. | URL | Version[^2] |
| - | - | - |
| 3dem | https://3dem.org/ | v3.**12** |
| brainmap | https://portal.brainmap.org/ | v3.**11** |
| epoc | https://prod.epoc.tacc.utexas.edu/ | v3.**11** |
| frontera | https://frontera-portal.tacc.utexas.edu/ | v3.**11** |
| lccf | https://lccf.tacc.utexas.edu/ | v3.**11** |
| protx | https://ccprotx.org/ | v3.**12** |
| sciviscolor | https://sciviscolor.org/ | v3.**12** |
| texascale | https://texascale.org/ | v3.**12** |
| utrc | https://utrc.tacc.utexas.edu/ | v3.**11** |

[^2]: The version of https://github.com/TACC/Core-CMS that each requires.

## Project Architecture

Within a `/custom_project_dir` can be:

| directory | contents |
| - | - |
| `static` | static assets, organized as Django CMS expects |
| `templates` | templates and saved snippets |
| `settings_custom.py` | project-specific values for [Core CMS] settings |

## Prerequisites

- [Git Submodules]
- [Core CMS]

A CMS project is run within [Core CMS]. Also, [Git Submodules] must be pre-installed on the system on which you will run the CMS project.

> **Note**
> The [Core CMS] has its own prerequisites.

## Start Project

Set up a new local CMS instance.

0. Core CMS:

    1. If not already done:
        1. Clone [Core CMS] repository.
        2. [Set up Core CMS](https://github.com/TACC/Core-CMS#readme) completely.
    2. Be in your [Core CMS] clone:

        ```sh
        cd Core-CMS
        ```

    3. Register and populate `/taccsite-custom`.

        ```sh
        git submodule init
        # This registers this repository at `/taccsite_custom`.
        git submodule update
        # This populates from this repository into `/taccsite_custom`.
        ```

    4. Create a symlink from `taccsite_cms/settings_custom.py` to `taccsite_custom/custom_project_dir/settings_custom.py`, e.g.

        ```sh
        ln -s '../taccsite_custom/custom_project_dir/settings_custom.py' 'taccsite_cms/settings_custom.py'
        ```

1. Docker Containers:

    ```sh
    docker exec -it core_cms /bin/bash
    # This opens a command prompt within the container.
    ```

2. Django Application:

    (Run these commands within the container.)

    ```sh
    python manage.py migrate
    # For projects that install apps
    # e.g. ECEP installs News/Blog
    npm ci
    npm run build:css --project="custom_project_dir"
    # If output includes
    # "Input Error: You must pass a valid"
    # then double check you have the directory
    # `taccsite_cms/…/static/…/css/src`
    python manage.py collectstatic --no-input
    ```

3. Django CMS:
    1. Open http://localhost:8000/.
    2. Verify anything specific to the custom project is present e.g.
        - logo
        - custom applications
        - custom global colors
        - custom styles (may require specific markup)

> **Note**
> A local machine CMS will be empty. It will **not** have content from staging nor production. To have that, follow and adapt instructions to [copy a database](https://confluence.tacc.utexas.edu/x/W4DZDg).

> **Note**
> A local machine CMS does **not** include **nor** integrate with an instance of [Core Portal]. There are no reliable instructions to do either. **Help welcome.**

## Update Project

To update an existing CMS instance.

### New Major [Core CMS] Version (or v3.12)

Read [Upgrade Project] for developer instructions.

### New Branch (or Minor or Patch [Core CMS] Version)

1. If CMS Docker files changed, rebuild Docker Containers:

    ```sh
    cd custom_project_dir
    make stop
    make build
    make start
    ```

2. If static assets or database models changed, update the Django Application:

    ```sh
    docker exec -it core_cms /bin/bash
    # That opens a command prompt within the container.
        python manage.py migrate
        python manage.py collectstatic --no-input
        # If the project has no new/changed assets,
        # then expect output of "0 static files […]"
    ```

## Run Project

No developer instruction beyond those for Core CMS.

To run multiple projects, first read [Multiple Projects](./docs/run-project.md#multiple-projects).

## Debug Project

Read [Debug Project](./docs/debug-project.md) for miscellaneous tips.

## Build & Deploy Project

Follow "Core-CMS-Resources" section of [How To Build & Deploy][Build & Deploy Project].

## Port Project

To port a project to [Core CMS Custom], read [Port Project].

<!-- Link Aliases -->

[Core CMS]: https://github.com/TACC/Core-CMS
[Core CMS Custom]: https://github.com/TACC/Core-CMS-Custom

[Git Submodules]: https://git-scm.com/book/en/v2/Git-Tools-Submodules

[Build & Deploy Project]: https://confluence.tacc.utexas.edu/x/Lo99E
[Port Project]: https://github.com/TACC/Core-CMS-Custom/blob/main/docs/port-project.md
[Upgrade Project]: https://github.com/TACC/Core-CMS/blob/main/docs/upgrade-project.md
