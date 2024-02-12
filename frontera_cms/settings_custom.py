# CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# *.FRONTERA-PORTAL.TACC.UTEXAS.EDU

########################
# DJANGO_CMS
########################

CMS_TEMPLATES = (
    ('frontera_cms/templates/standard.html', 'Standard'),
    ('frontera_cms/templates/fullwidth.html', 'Full Width'),
    ('frontera_cms/templates/home.html', 'Homepage'),
    ('frontera-cms/templates/standard.html', 'DEPRECATED Standard'),
    ('frontera-cms/templates/fullwidth.html', 'DEPRECATED Full Width'),
    ('frontera-cms/templates/home.html', 'DEPRECATED Homepage'),

    ('guide.html', 'Guide'),
    ('guides/getting_started.html', 'Guide: Getting Started'),
    ('guides/data_transfer.html', 'Guide: Data Transfer'),
    ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
    ('guides/portal_technology.html', 'Guide: Portal Technology Stack')
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
    "frontera_cms/img/org_logos/tacc-white.png", # TACC/Core-CMS#283 & #284
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
    "frontera",
    "frontera_cms/img/org_logos/frontera-white-solo.png",
    "",
    "/",
    "_self",
    "Frontera Logo",
    "anonymous",
    "True"
]

FAVICON = {
    "img_file_src": "frontera_cms/img/org_logos/favicon.ico"
}
