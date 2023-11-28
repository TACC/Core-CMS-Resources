# Run Multiple Projects

## One at a Time

> **Note**
> By default, multiple projects can not be run simultaneously.[^1]

To stop one project, and run another:

1. Cancel any active `make start` output i.e. press <kbd>control</kbd> + <kbd>C</kbd>.

2. Take down one project.

    > **Note**
    > This is equivalent to deleting the relevant set of related containers in Docker Desktop.

    ```sh
    make stop
    ```

3. Replace existing symlink.

    Replace symlink `taccsite_cms/settings_custom.py` with one to `taccsite_custom/custom_project_dir/settings_custom.py`, e.g.

    ```sh
    rm -f 'taccsite_cms/settings_custom.py'
    ln -s '../taccsite_custom/custom_project_dir/settings_custom.py' 'taccsite_cms/settings_custom.py'
    ```

4. Start the other project.

    > **Note**
    > This retains containers and volumes e.g. database, search index.

    > **Warning**
    > With these instructions, if a project has different apps installed, and especially if you used those apps on your local CMS, you will likely encounter an error. This document can **not** help you solve such an error.[^1]

    Follow [Core CMS: Getting Started: Build & Start the Docker Containers](https://github.com/TACC/Core-CMS/blob/main/README.md#build--start-the-docker-containers) instructions.

## Simultaneous Projects

> **Warning**
> With these instructions, you will **not** be able to use the database (**nor** internal search index) of an already set up custom project (i.e. its local volumes).

To run multiple projects simultaneously:

1. Create another clone of [Core CMS].
2. Set up the CMS in that clone.
3. Set up the other project in that CMS.

[^1]: If you want to run multiple projects simultaneously, and avoid the Warning for multiple projects, see [Simultaneous Projects](#simultaneous-projects).

<!-- Link Aliases -->

[Core CMS]: https://github.com/TACC/Core-CMS
