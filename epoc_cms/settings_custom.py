# CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# *.EPOC.TACC.UTEXAS.EDU

########################
# DJANGO: AUTH
########################

AUTH_LDAP_SERVER_URI = "ldap://cluster.ldap.tacc.utexas.edu"

########################
# TACC: PORTAL
########################

INCLUDES_CORE_PORTAL = False
INCLUDES_PORTAL_NAV = False
INCLUDES_SEARCH_BAR = False

########################
# DJANGO_CMS
########################

CMS_TEMPLATES = (
    ('standard.html', 'Standard'),
    ('fullwidth.html', 'Full Width'),
)

########################
# TACC: BRANDING
########################

# NOTE: Variables NSF_BRANDING, TACC_BRANDING, and UTEXAS_BRANDING are duplicated from Core-CMS cuz current infrastructure lacks ability to reference default values.

TACC_BRANDING = [
    "tacc",
    "epoc_cms/img/org_logos/tacc-white.png",
    "branding-tacc",
    "https://www.tacc.utexas.edu/",
    "_blank",
    "TACC Logo",
    "anonymous",
    "True"
]

UTEXAS_BRANDING = [
    "utexas",
    "epoc_cms/img/org_logos/utaustin-white.png",
    "branding-utaustin",
    "https://www.utexas.edu/",
    "_blank",
    "University of Texas at Austin Logo",
    "anonymous",
    "True"
]

NSF_BRANDING = [
    "nsf",
    "epoc_cms/img/org_logos/nsf-white.png",
    "branding-nsf",
    "https://www.nsf.gov/",
    "_blank",
    "NSF Logo",
    "anonymous",
    "True"
]

CUSTOM_BRANDING = [
    "epoc",
    "epoc_cms/img/org_logos/esnet-white-logo.png",
    "branding-logo--short",
    "https://www.es.net/",
    "_blank",
    "ESnet Logo",
    "anonymous",
    "True",
]

BRANDING = [ TACC_BRANDING, UTEXAS_BRANDING, CUSTOM_BRANDING ]

########################
# TACC: LOGO & FAVICON
########################

LOGO = [
    "epoc",
    "epoc_cms/img/org_logos/epoc-color-logo.png",
    "",
    "/",
    "_self",
    "Logo or EPOC Global Portal",
    "anonymous",
    "True"
]

FAVICON = {
    "img_file_src": "epoc_cms/img/org_logos/favicon.ico"
}
