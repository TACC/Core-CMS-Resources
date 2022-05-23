## CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# 3DEM[...]

from taccsite_cms.settings import *

########################
# DJANGO CMS SETTINGS
########################

CMS_TEMPLATES = (
    ('fullwidth.html', 'Fullwidth'),

    ('home_portal.html', 'Standard Portal Homepage'),

    ('guide.html', 'Guide'),
    ('guides/getting_started.html', 'Guide: Getting Started'),
    ('guides/data_transfer.html', 'Guide: Data Transfer'),
    ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
    ('guides/portal_technology.html', 'Guide: Portal Technology Stack')
)

# Deprecated Templates
# TODO: FP-1645: Remove
CMS_TEMPLATES += (
    ('neuronex-cms/templates/fullwidth.html', 'DEPRECATED Fullwidth'),
)

########################
# TACC: BRANDING
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
# TACC: LOGOS
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

FAVICON = {
    "img_file_src": "neuronex-cms/img/org_logos/favicon.ico"
}

########################
# IMPORT & EXPORT
########################

try:
    from taccsite_cms.settings_local import *
except ModuleNotFoundError:
    pass
