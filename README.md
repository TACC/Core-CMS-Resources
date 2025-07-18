# Core-CMS-Resources

Project-specific code _that had been_ built into the [Core CMS] project

> [!CAUTION]
> This repository is **unmaintained**. [Learn how to develop a custom Core-CMS project](https://github.com/TACC/Core-CMS/blob/main/docs/develop-custom-project.md).[^1]

[^1]: Deploying websites that are still in Core-CMS-Resources **and** have [old custom templates will trigger a major problem](https://github.com/TACC/Core-CMS-Resources/pull/176#issuecomment-1603194690). The prefered solution is [migration](#port-project). If you must deploy without migration, then [upgrade the website for Core-CMS v3.12](./docs/upgrade-project.md#for-core-cms-v312).

## Table of Contents

- [Related Repositories](#related-repositories)
- [Project Websites](#project-websites)
- [Project Architecture](#project-architecture)
- [Prerequisites](#prerequisites)
- [Start Project](#start-project)
- [Update Project](#update-project)
- [Run Multiple Projects](#run-multiple-projects)
- [Debug Project](#debug-project)
- [Build & Deploy Project](#build--deploy-project)
- [Port Project](#port-project)

## Related Repositories

- [Core CMS], the base CMS code for TACC WMA CMS Websites
- [Core CMS Custom], for custom assets of TACC WMA CMS Websites
- [Core CMS Template], to build a custom TACC WMA CMS Website

## Project Websites

> [!IMPORTANT]
> No more websites exist in this repository. All were moved to [Core CMS Custom] or a repository built from [Core-CMS-Template](https://github.com/TACC/Core-CMS-Template).

## Project Architecture

Within a `/custom_project_dir` can be:

| directory | contents |
| - | - |
| `static` | static assets, organized as Django CMS expects |
| `templates` | templates and saved snippets |
| `settings_custom.py`[^3] | project-specific values for [Core CMS] settings |

[^3]: The `cms.settings_custom.py` is committed in [Core Portal Deployments]. A `settings_custom.py` in [Core CMS] is `.gitignore`'d.

## Prerequisites

- [Git Submodules]
- [Core CMS]

A CMS project is run within [Core CMS]. Also, [Git Submodules] must be pre-installed on the system on which you will run the CMS project.

> **Note**
> The [Core CMS] has its own prerequisites.

## Start Project

Set up a new local CMS instance.

0. Set up [Core CMS] to run a local [Core CMS Resources]:

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

    4. Create `/taccsite_cms/settings_custom.py`[^3] and populate it with respective `cms.settings_custom.py` from [Core Portal Deployments] e.g. [`/lccf/camino/cms.settings_custom.py`](https://github.com/TACC/Core-Portal-Deployments/blob/d8e31d9/lccf/camino/cms.settings_custom.py).

1. Enter the CMS Docker Container:

    ```sh
    docker exec -it core_cms /bin/bash
    # This opens a command prompt within the container
    ```

2. Update the Django Application:

    (Run these commands within the container.)

    ```sh
    python manage.py migrate
    python manage.py createsuperuser
    # To use default "Username" and skip "Email address", press Enter at both prompts.
    # At "Password" prompts, you may use an easy-to-remember password.
    python manage.py collectstatic --no-input

    ```

3. Open Django CMS:
    1. Open http://localhost:8000/.
    2. Verify anything specific to the custom project is present e.g.
        - logo
        - custom applications
        - custom global colors
        - custom styles (may require specific markup)

> **Note**
> A local machine CMS will be empty. It will **not** have content from staging nor production. To have that, follow and adapt instructions to [copy a database](https://tacc-main.atlassian.net/wiki/x/GwBJAg).

> **Note**
> A local machine CMS does **not** include **nor** integrate with an instance of [Core Portal]. To attempt to do that, follow [How to Use a Custom Docker Compose File](https://github.com/TACC/Core-CMS/wiki/How-to-Use-a-Custom-Docker-Compose-File) and [Locally Develop CMS Portal Docs](https://github.com/TACC/Core-CMS/wiki/Locally-Develop-CMS---Portal---Docs). **Help welcome.**

## Update Project

Follow [Core CMS: Update Project](https://github.com/TACC/Core-CMS/blob/main/README.md#update-project) instructions.

## Develop Project

Follow "via [Core CMS Resources]" section of [Core CMS: Develop Custom Project](https://github.com/TACC/Core-CMS/blob/main/docs/develop-custom-project.md#via-core-cms-resources).

## Debug Project

Read [Debug Project](./docs/debug-project.md) for miscellaneous tips.

## Build & Deploy Project

Follow "Core-CMS-Resources" section of [How To Build & Deploy][Build & Deploy Project].

## Run Multiple Projects

Read [Run Multiple Projects](./docs/run-multiple-projects.md).

## Port Project

To port a project to [Core CMS Custom], read [Port Project].

<!-- Link Aliases -->

[Core CMS]: https://github.com/TACC/Core-CMS
[Core Portal]: https://github.com/TACC/Core-Portal
[Core CMS Custom]: https://github.com/TACC/Core-CMS-Custom
[Core CMS Template]: https://github.com/TACC/Core-CMS-Template
[Core CMS Resources]: https://github.com/TACC/Core-CMS-Resources
[Core Portal Deployments]: https://github.com/TACC/Core-Portal-Deployments

[Git Submodules]: https://git-scm.com/book/en/v2/Git-Tools-Submodules

[Build & Deploy Project]: https://tacc-main.atlassian.net/l/cp/3U2WHbVB
[Port Project]: https://github.com/TACC/Core-CMS-Custom/blob/main/docs/port-project.md
[Upgrade Project]: https://github.com/TACC/Core-CMS/blob/main/docs/upgrade-project.md
