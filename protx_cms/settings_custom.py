# CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# *.PROTX.TACC.UTEXAS.EDU

########################
# DJANGO_CMS
########################

CMS_TEMPLATES = (
    ('standard.html', 'Standard'),
    ('fullwidth.html', 'Full Width'),

    ('guide.html', 'Guide'),
    ('protx_cms/templates/getting_started.html', 'Guide: Getting Started'),
    ('protx-cms/templates/getting_started.html', 'DEPRECATED Guide: Getting Started'),
    ('guides/data_transfer.html', 'Guide: Data Transfer'),
    ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
    ('guides/portal_technology.html', 'Guide: Portal Technology Stack')
)

########################
# TACC: BRANDING
########################

# NOTE: Variables NSF_BRANDING, TACC_BRANDING, and UTEXAS_BRANDING are duplicated from Core-CMS cuz current infrastructure lacks ability to reference default values.

COOKS_BRANDING = [
    "cooks",
    "protx_cms/img/org_logos/CClogo_Standard_White_Transparent.png",
    "branding-tacc",
    "https://cookchildrens.org",
    "_blank",
    "Cooks Childrens Logo",
    "anonymous",
    "True"
]

TACC_BRANDING = [
    "tacc",
    "site_cms/img/org_logos/tacc-white.png",
    "branding-tacc",
    "https://www.tacc.utexas.edu/",
    "_blank",
    "TACC Logo",
    "anonymous",
    "True"
]

UTEXAS_BRANDING = [
    "utexas",
    "site_cms/img/org_logos/utaustin-white.png",
    "branding-utaustin",
    "https://www.utexas.edu/",
    "_blank",
    "University of Texas at Austin Logo",
    "anonymous",
    "True"
]

BRANDING = [ COOKS_BRANDING, TACC_BRANDING, UTEXAS_BRANDING ]

########################
# TACC: LOGO & FAVICON
########################

LOGO = [
    "protx",
    "protx_cms/img/org_logos/ProTx-logo-nobg.png",
    "",
    "/",
    "_self",
    "ProTX Logo",
    "anonymous",
    "True"
]
