# CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# *.LCCF.TACC.UTEXAS.EDU

# FAQ: Some _VARIABLES are duplicated from settings.py (but prefixed with "_")
#      because current infrastructure lacks ability to reference default values

########################
# DJANGO CMS SETTINGS
########################

# CMS_TEMPLATES = (
#     ('lccf-tacc/templates/standard.html', 'Standard'),
#     ('lccf-tacc/templates/fullwidth.html', 'Full Width'),
#     ('guide.html', 'Guide'),
#     ('guides/getting_started.html', 'Guide: Getting Started'),
#     ('guides/data_transfer.html', 'Guide: Data Transfer'),
#     ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
#     ('guides/portal_technology.html', 'Guide: Portal Technology Stack')
# )

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
# LOGOS
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
# PORTAL
########################

INCLUDES_CORE_PORTAL = False
