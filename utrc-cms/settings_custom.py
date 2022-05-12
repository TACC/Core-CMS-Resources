# CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# *.UTRC.TACC.UTEXAS.EDU


########################
# DJANGO CMS SETTINGS
########################

CMS_TEMPLATES = (
    ('standard.html', 'Standard'),
    ('fullwidth.html', 'Full Width'),

    ('home.html', 'Home'),

    ('guide.html', 'Guide'),
    ('guides/getting_started.html', 'Guide: Getting Started'),
    ('guides/data_transfer.html', 'Guide: Data Transfer'),
    ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
    ('guides/portal_technology.html', 'Guide: Portal Technology Stack')
)

# FP-1645: Remove CMS_TEMPLATES_DEPRECATED
CMS_TEMPLATES_DEPRECATED = (
    ('utrc-cms/templates/home.html', 'DEPRECATED Home'),
)
CMS_TEMPLATES = CMS_TEMPLATES + CMS_TEMPLATES_DEPRECATED

########################
# TACC: LOGOS
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

FAVICON = {
    "img_file_src": "utrc-cms/img/org_logos/favicon.ico"
}
