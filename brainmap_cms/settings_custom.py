# CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# *.BRAINMAP.TACC.UTEXAS.EDU

########################
# DJANGO_CMS
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
# TACC: BRANDING
########################

# NOTE: Variables NSF_BRANDING, TACC_BRANDING, and UTEXAS_BRANDING are duplicated from Core-CMS cuz current infrastructure lacks ability to reference default values.

UTHSCSA_BRANDING = [
    "uthscsa",
    "brainmap_cms/img/org_logos/uthscsa-logo-white.png",
    "branding-logo--short",
    "https://www.uthscsa.edu/",
    "_blank",
    "UTHSC-SA Logo",
    "anonymous",
    "True",
]

SGCI_BRANDING = [
    "sgci",
    "brainmap_cms/img/org_logos/sgci-logo-sans-text.svg",
    "branding-logo--short",
    "https://sciencegateways.org/",
    "_blank",
    "SGCI Logo",
    "anonymous",
    "True",
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

BRANDING = [ SGCI_BRANDING, TACC_BRANDING, UTEXAS_BRANDING, UTHSCSA_BRANDING ]

########################
# TACC: LOGO & FAVICON
########################

LOGO = [
    "brainmap",
    "brainmap_cms/img/org_logos/brainmap-logo--light-text-trans-bkgd--large-text.svg",
    "",
    "/",
    "_self",
    "BrainMap Logo",
    "anonymous",
    "True"
]

FAVICON = {
    "img_file_src": "brainmap_cms/img/org_logos/brainmap-logo--dark-text-trans-bkgd--icon-only.png"
}
