# CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# …3DEM…TACC.UTEXAS.EDU

########################
# DJANGO_CMS
########################

CMS_TEMPLATES = (
    ('_3dem_cms/templates/fullwidth.html', 'Fullwidth'),
    ('home_portal.html', 'Standard Portal Homepage'),
    ('guide.html', 'Guide'),
    ('_3dem_cms/templates/guides/getting_started.v2.html', 'Guide: Getting Started (v2)'),
    ('_3dem_cms/templates/guides/getting_started.tam.html', 'Guide: Getting Started (TAM)'),
    ('_3dem_cms/templates/guides/data_transfer.html', 'Guide: Data Transfer'),
    ('_3dem_cms/templates/guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
    # DEPRECATED
    ('neuronex-cms/templates/fullwidth.html', 'DEPRECATED Fullwidth'),
    # CORE-CMS v3.11 (used by 3Dem before it ran on Core-CMS v3.12)
    ('guides/getting_started.html', 'CORE-CMS Guide: Getting Started'),
    ('guides/data_transfer.html', 'CORE-CMS Guide: Data Transfer'),
    ('guides/data_transfer.globus.html', 'CORE-CMS Guide: Globus Data Transfer'),
)

########################
# TACC: BRANDING
########################

# NOTE: Variables NSF_BRANDING, TACC_BRANDING, and UTEXAS_BRANDING are duplicated from Core-CMS cuz current infrastructure lacks ability to reference default values.

NSF_BRANDING = [
    "nsf",
    "site_cms/img/org_logos/nsf-white.png",
    "branding-nsf",
    "https://www.nsf.gov/",
    "_blank",
    "NSF Logo",
    "anonymous",
    "True"
]

FRONTERA_TACC_BRANDING = [
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

BRANDING = [ NSF_BRANDING, FRONTERA_TACC_BRANDING, UTEXAS_BRANDING ]

########################
# TACC: LOGO & FAVICON
########################

LOGO = [
    "portal",
    "_3dem_cms/img/org_logos/logo.3dem.png",
    "",
    "/",
    "_self",
    "3Dem Logo",
    "anonymous",
    "True"
]

FAVICON = {
    "img_file_src": "_3dem_cms/img/org_logos/favicon.ico"
}
