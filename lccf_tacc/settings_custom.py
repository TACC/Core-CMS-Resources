# CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# *.LCCF.TACC.UTEXAS.EDU

########################
# TACC: BRANDING
########################

# FAQ: Some _VARIABLES are duplicated from settings.py (but prefixed with "_") cuz current infrastructure lacks ability to reference default values

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

BRANDING = [ NSF_BRANDING, TACC_BRANDING, UTEXAS_BRANDING ]

########################
# TACC: LOGO & FAVICON
########################

LOGO = [
    "lccf",
    "lccf-tacc/img/org_logos/lccf-white.png",
    "",
    "/",
    "_self",
    "LCCF Logo",
    "anonymous",
    "True"
]

########################
# TACC: PORTAL
########################

INCLUDES_CORE_PORTAL = False
INCLUDES_PORTAL_NAV = False
INCLUDES_SEARCH_BAR = False
