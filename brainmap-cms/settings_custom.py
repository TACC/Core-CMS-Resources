# CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# *.BRAINMAP.TACC.UTEXAS.EDU

########################
# DJANGO CMS SETTINGS
########################

CMS_TEMPLATES = (
    ('standard.html', 'Standard'),
    ('fullwidth.html', 'Full Width'),

    ('home_portal.html', 'Standard Portal Homepage'),

    ('guide.html', 'Guide'),
    ('guides/getting_started.html', 'Guide: Getting Started'),
    ('guides/data_transfer.html', 'Guide: Data Transfer'),
    ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
    ('guides/portal_technology.html', 'Guide: Portal Technology Stack'),
)

########################
# BRANDING
########################

_SGCI_BRANDING = [
    "sgci",
    "brainmap-cms/img/org_logos/sgci-logo.png",
    "branding-logo--tall",
    "https://www.nsf.gov/",
    "_blank",
    "SGCI Logo",
    "anonymous",
    "True",
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

BRANDING = [ _SGCI_BRANDING, _TACC_BRANDING, _UTEXAS_BRANDING ]

########################
# LOGOS
########################

LOGO = [
    "brainmap",
    "brainmap-cms/img/org_logos/brainmap-logo.png",
    "",
    "/",
    "_self",
    "BrainMap Logo",
    "anonymous",
    "True"
]
