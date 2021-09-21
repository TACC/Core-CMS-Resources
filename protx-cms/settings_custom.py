# CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# *.PROTX.TACC.UTEXAS.EDU

# FAQ: Some _VARIABLES are duplicated from settings.py (but prefixed with "_")
#      because current infrastructure lacks ability to reference default values

########################
# DJANGO CMS SETTINGS
########################

CMS_TEMPLATES = (
    ('protx-cms/templates/standard.html', 'Standard'),
    ('protx-cms/templates/fullwidth.html', 'Full Width'),
    ('guide.html', 'Guide'),
    ('guides/getting_started.html', 'Guide: Getting Started'),
    ('guides/data_transfer.html', 'Guide: Data Transfer'),
    ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
    ('guides/portal_technology.html', 'Guide: Portal Technology Stack')
)

########################
# BRANDING
########################

COOKS_BRANDING = [
    "cooks",
    "protx-cms/img/org_logos/CClogo_Standard_White_Transparent.png",
    "branding-tacc",
    "https://cookchildrens.org",
    "_blank",
    "Cooks Childrens Logo",
    "anonymous",
    "True"
]

_TACC_BRANDING = [
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

BRANDING = [ COOKS_BRANDING, _TACC_BRANDING, _UTEXAS_BRANDING ]

########################
# LOGOS
########################

LOGO = [
    "protx",
    "protx-cms/img/org_logos/ProTx-logo-nobg.png",
    "",
    "/",
    "_self",
    "ProTX Logo",
    "anonymous",
    "True"
]
