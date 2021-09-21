# CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# *.TAPIS-PROJECT.ORG

# FAQ: Some _VARIABLES are duplicated from settings.py (but prefixed with "_")
#      because current infrastructure lacks ability to reference default values

########################
# DJANGO CMS SETTINGS
########################

# CMS_TEMPLATES = (
#     ('tapis-project-org/templates/standard.html', 'Standard'),
#     ('tapis-project-org/templates/fullwidth.html', 'Full Width'),
#     ('guide.html', 'Guide'),
#     ('guides/getting_started.html', 'Guide: Getting Started'),
#     ('guides/data_transfer.html', 'Guide: Data Transfer'),
#     ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
#     ('guides/portal_technology.html', 'Guide: Portal Technology Stack')
# )

########################
# BRANDING
########################

UHAWAII_BRANDING = [
    "uhawaii",
    "tapis-project-org/img/org_logos/hawaii-header-trimmed.png",
    "branding-uhawaii",
    "https://www.hawaii.edu/",
    "_blank",
    "University of Hawaii Logo",
    "anonymous",
    "True"
]

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

BRANDING = [ _NSF_BRANDING, _TACC_BRANDING, _UTEXAS_BRANDING, UHAWAII_BRANDING ]

########################
# LOGOS
########################

LOGO =  [
    "tapis",
    "tapis-project-org/img/org_logos/tapis-logo-navbar.png",
    "",
    "/",
    "_self",
    "Tapis Logo",
    "anonymous",
    "True"
]

########################
# PORTAL
########################

INCLUDES_CORE_PORTAL = False

########################
# GOOGLE ANALYTICS
########################

GOOGLE_ANALYTICS_PROPERTY_ID = "UA-125525035-17"