# CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# *.UTRC.TACC.UTEXAS.EDU


########################
# DJANGO CMS SETTINGS
########################

CMS_TEMPLATES = (
    ('utrc-cms/templates/standard.html', 'Standard'),
    ('utrc-cms/templates/fullwidth.html', 'Full Width'),
    ('guide.html', 'Guide'),
    ('guides/getting_started.html', 'Guide: Getting Started'),
    ('guides/data_transfer.html', 'Guide: Data Transfer'),
    ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
    ('guides/portal_technology.html', 'Guide: Portal Technology Stack')
)

########################
# LOGOS
########################

LOGO = [
    "portal",
    "utrc-cms/img/org_logos/utrc-horizontal-logo-white-simple.svg",
    "",
    "/",
    "_self",
    "UTRC Logo",
    "anonymous",
    "True"
]

########################
# FAVICON
########################

FAVICON = {
    "img_file_src": "utrc-cms/img/org_logos/favicon.ico"
}
