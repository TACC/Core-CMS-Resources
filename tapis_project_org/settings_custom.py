# CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# *.TAPIS-PROJECT.ORG

# FAQ: Some _VARIABLES are duplicated from settings.py (but prefixed with "_")
#      because current infrastructure lacks ability to reference default values

########################
# TACC: BRANDING
########################

UHAWAII_BRANDING = [
    "uhawaii",
    "tapis_project_org/img/org_logos/hawaii-header-trimmed.png",
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
# TACC: LOGOS
########################

LOGO =  [
    "tapis",
    "tapis_project_org/img/org_logos/tapis-logo-navbar.png",
    "",
    "/",
    "_self",
    "Tapis Logo",
    "anonymous",
    "True"
]

########################
# TACC: PORTAL
########################

INCLUDES_CORE_PORTAL = False
INCLUDES_PORTAL_NAV = False
INCLUDES_SEARCH_BAR = False

########################
# TACC: GOOGLE ANALYTICS
########################

GOOGLE_ANALYTICS_PROPERTY_ID = "UA-125525035-17"
