# Upgrade Project

## for Core-CMS v3.12

### Redirect Deprecated Templates

**If** the custom project directory:

- has any `templates/*.html` e.g.
  - `templates/standard.html`
  - `templates/fullwidth.html`
  - `templates/home.html`

Then:

1. Copy the templates to become deprecated templates:
    - from `custom_project_dir/templates`
    - to `custom-project-dir/templates`

    > **Warning**
    > The name `custom_project_dir` **must** match the old name as it was, including dashes.

2. Edit the deprecated templates to extend the new templates e.g.

    ```django
    {% extends "custom_project_dir/templates/standard.html" %}
    ```

3. Update `settings_custom.py` to support deprecated templates:

    ```diff
        ('custom_project_dir/templates/standard.html', 'Standard'),
        ('custom_project_dir/templates/fullwidth.html', 'Full Width'),
    +   ('custom-project-dir/templates/standard.html', 'DEPRECATED Standard'),
    +   ('custom-project-dir/templates/fullwidth.html', 'DEPRECATED Full Width'),
    ```

### After Deploy

1. Change template of every page on project to **not** use deprecated template.
2. Remove its deprecated templates from repository.
