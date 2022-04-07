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

_UTHSCSA_BRANDING = [
    "uthscsa",
    "brainmap-cms/img/org_logos/uthscsa-logo-white.png",
    "branding-logo--short",
    "https://www.uthscsa.edu/",
    "_blank",
    "UTHSC-SA Logo",
    "anonymous",
    "True",
]

_SGCI_BRANDING = [
    "sgci",
    "brainmap-cms/img/org_logos/sgci-logo-sans-text.svg",
    "branding-logo--short",
    "https://sciencegateways.org/",
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

BRANDING = [ _SGCI_BRANDING, _TACC_BRANDING, _UTEXAS_BRANDING, _UTHSCSA_BRANDING ]

########################
# LOGOS
########################

LOGO = [
    "brainmap",
    "brainmap-cms/img/org_logos/brainmap-logo.png",
    "",
    "https://brainmap.org",
    "_self",
    "BrainMap Logo",
    "anonymous",
    "True"
]

########################
# FAVICON
########################

FAVICON = {
    "img_file_src": "brainmap-cms/img/org_logos/favicon.ico"
}
