# CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# *.FRONTERA-PORTAL.TACC.UTEXAS.EDU

from taccsite_cms.settings import *

########################
# DJANGO CMS SETTINGS
########################

CMS_TEMPLATES = (
    ('standard.html', 'Standard'),
    ('fullwidth.html', 'Full Width'),

    ('home.html', 'Homepage'),

    ('guide.html', 'Guide'),
    ('guides/getting_started.html', 'Guide: Getting Started'),
    ('guides/data_transfer.html', 'Guide: Data Transfer'),
    ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
    ('guides/portal_technology.html', 'Guide: Portal Technology Stack')
)

# Deprecated Templates
# TODO: FP-1645: Remove
CMS_TEMPLATES += (
    ('frontera-cms/templates/standard.html', 'DEPRECATED Standard'),
    ('frontera-cms/templates/fullwidth.html', 'DEPRECATED Full Width'),
    ('frontera-cms/templates/home.html', 'DEPRECATED Homepage'),
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
    "frontera-cms/img/org_logos/tacc-white.png", # TACC/Core-CMS#283 & #284
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

LOGO =  [
    "frontera",
    "frontera-cms/img/org_logos/frontera-white-solo.png",
    "",
    "/",
    "_self",
    "Frontera Logo",
    "anonymous",
    "True"
]

FAVICON = {
    "img_file_src": "frontera-cms/img/org_logos/favicon.ico"
}

########################
# IMPORT & EXPORT
########################

try:
    from taccsite_cms.settings_local import *
except ModuleNotFoundError:
    pass
