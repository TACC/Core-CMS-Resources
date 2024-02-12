# CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# *.UTRC.TACC.UTEXAS.EDU

########################
# DJANGO_CMS
########################

CMS_TEMPLATES = (
    ('standard.html', 'Standard'),
    ('fullwidth.html', 'Full Width'),

    ('utrc_cms/templates/home.html', 'Home'),
    ('utrc-cms/templates/home.html', 'DEPRECATED Home'),

    ('guide.html', 'Guide'),
    ('guides/getting_started.html', 'Guide: Getting Started'),
    ('guides/data_transfer.html', 'Guide: Data Transfer'),
    ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
    ('guides/portal_technology.html', 'Guide: Portal Technology Stack')
)

########################
# TACC: LOGO & FAVICON
########################

LOGO = [
    "portal",
    "utrc_cms/img/org_logos/utrc-horizontal-logo-white-simple.svg",
    "",
    "/",
    "_self",
    "UTRC Logo",
    "anonymous",
    "True"
]

FAVICON = {
    "img_file_src": "utrc_cms/img/org_logos/favicon.ico"
}
