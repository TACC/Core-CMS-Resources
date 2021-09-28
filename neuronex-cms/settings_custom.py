## CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# 3DEM[...]

# FAQ: Some _VARIABLES are duplicated from settings.py (but prefixed with "_")
#      because current infrastructure lacks ability to reference default values

########################
# DJANGO CMS SETTINGS
########################

CMS_TEMPLATES = (
    ('neuronex-cms/templates/fullwidth.html', 'Fullwidth'),
    ('home_portal.html', 'Standard Portal Homepage'),
    ('guide.html', 'Guide'),
    ('guides/getting_started.html', 'Guide: Getting Started'),
    ('guides/data_transfer.html', 'Guide: Data Transfer'),
    ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
    ('guides/portal_technology.html', 'Guide: Portal Technology Stack')
)

########################
# BRANDING
########################

_NSF_BRANDING = [
    "nsf",
    "site_cms/img/org_logos/nsf-white.png",
    "branding-nsf",
    "https://www.nsf.gov/",
    "_blank",
    "NSF Logo",
    "anonymous",
    "True"
]

_FRONTERA_TACC_BRANDING = [
    "tacc",
    "site_cms/img/org_logos/tacc-white.png",
    "branding-tacc",
    "https://www.tacc.utexas.edu/",
    "_blank",
    "TACC Logo",
    "anonymous",
    "True"
]

_UTEXAS_BRANDING = [
    "utexas",
    "site_cms/img/org_logos/utaustin-white.png",
    "branding-utaustin",
    "https://www.utexas.edu/",
    "_blank",
    "University of Texas at Austin Logo",
    "anonymous",
    "True"
]

BRANDING = [ _NSF_BRANDING, _FRONTERA_TACC_BRANDING, _UTEXAS_BRANDING ]

########################
# LOGOS
########################

LOGO = [
    "portal",
    "neuronex-cms/img/org_logos/logo.3dem.png",
    "",
    "/",
    "_self",
    "3Dem Logo",
    "anonymous",
    "True"
]

########################
# FAVICON
########################

FAVICON = {
    "img_file_src": "neuronex-cms/img/org_logos/favicon.ico"
}
