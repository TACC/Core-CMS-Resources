# TACC CMS Project

The project-specific CMS code for TACC WMA Workspace Websites.

To add resources for a new project:

1. Clone `/example_cms`.
2. Read `/_readme_cms`.

To build such a CMS project, use [TACC/Core-CMS](https://github.com/TACC/Core-CMS).

> **Warning**
> Do **not** deploy these websites via this repository with [TACC/Core-CMS#v3.12.0](https://github.com/TACC/Core-CMS/releases/tag/v3.12.0) or greater. **Instead**, migrate them to [Core CMS Custom].[^1]

## Related Repositories

- [Camino], a Docker container-based deployment scheme
- [Core CMS], the base CMS code for TACC WMA CMS Websites
- [Core CMS Custom], the custom CMS code (new solution) for TACC WMA CMS Websites


## Intended Usage

The Core CMS Resources is __not__ run independently.

[Core CMS] loads assets from this repo.

Please see the [Core CMS README].


## Websites Maintained

- https://prod.a2cps.tacc.utexas.edu/
- https://prod.apcd.tacc.utexas.edu/ a.k.a. https://txapcd.org/<br />
  <sup>code has moved to https://github.com/TACC/Core-CMS-Custom/blob/main/apcd_cms/</sup>
- https://portal.brainmap.org/
- https://democratizingdata.ai/
- https://prod.ecep.tacc.utexas.edu/ a.k.a. https://ecepalliance.org/
- https://prod.epoc.tacc.utexas.edu/
- https://frontera-portal.tacc.utexas.edu/
- https://lccf.tacc.utexas.edu/
- https://3dem.org/
- https://prod.protx.tacc.utexas.edu/
- https://prod.sciviscolor.tacc.utexas.edu/
- https://tapis-project.org/
- https://texascale.org/
- https://dev.tup.tacc.utexas.edu/<br />
  <sup>code has moved to https://github.com/TACC/tup-ui/blob/main/apps/tup-cms/</sup>
- https://utrc.tacc.utexas.edu/

<!-- Link Aliases -->

[Core CMS]: https://github.com/TACC/Core-CMS
[Core Styles]: https://github.com/TACC/Core-Styles
[Core CMS Custom]: https://github.com/TACC/Core-CMS-Custom
[Core CMS README]: https://github.com/TACC/Core-CMS/blob/main/README.md
[Camino]: https://github.com/TACC/Camino

[^1]: [Websites with custom templates will experience a major problem.](https://github.com/TACC/Core-CMS-Resources/pull/176#issuecomment-1603194690) Even though not all websites have such templates **and** there is a [tested solution](https://github.com/TACC/Core-CMS-Resources/pull/176#issuecomment-1603215969), website development benefits so much from migration, that every opportunity is taken to encourage it.
