# CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# *.FRONTERA-PORTAL.TACC.UTEXAS.EDU

# FAQ: Some _VARIABLES are duplicated from settings.py (but prefixed with "_")
#      because current infrastructure lacks ability to reference default values

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

# FP-1645: Remove CMS_TEMPLATES_DEPRECATED
CMS_TEMPLATES_DEPRECATED = (
    ('frontera-cms/templates/standard.html', 'DEPRECATED Standard'),
    ('frontera-cms/templates/fullwidth.html', 'DEPRECATED Full Width'),
    ('frontera-cms/templates/home.html', 'DEPRECATED Homepage'),
)
CMS_TEMPLATES += CMS_TEMPLATES_DEPRECATED

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
