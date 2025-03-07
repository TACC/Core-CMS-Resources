# TACC Texascale CMS Robots.txt

As of 2022-02-28, [texascale.org](https://texascale.org) is the only stand-alone Django CMS website to use a `robots.txt`.

It is loaded by Nginx because of import of an extra Nginx config file.

## To Do

- Learn whether [djangocms-page-meta] allows setting `noindex` for many pages at once.[^1]
- Allow extending and/or overwriting `robots.txt` per site.

[djangocms-page-meta]: https://github.com/nephila/djangocms-page-meta

[^1]: To set `noindex` for one page, read [Django CMS - Admin Guide - Do Not Let Google Index/Crawl a Page](https://tacc-main.atlassian.net/wiki/x/6Ahv).
