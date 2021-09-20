# CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# *.UTRC.TACC.UTEXAS.EDU

# FAQ: Some _VARIABLES are duplicated from settings.py (but prefixed with "_")
#      because current infrastructure lacks ability to reference default values

########################
# DJANGO CMS SETTINGS
########################

CMS_TEMPLATES = (
    ('utrc-cms/templates/standard.html', 'Standard'),
    ('utrc-cms/templates/fullwidth.html', 'Full Width'),
    ('guide.html', 'Guide'),
    ('guides/getting_started.html', 'Guide: Getting Started'),
    ('guides/data_transfer.html', 'Guide: Data Transfer'),
    ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
    ('guides/portal_technology.html', 'Guide: Portal Technology Stack')
)

########################
# BRANDING & LOGOS
########################

########################
# BRANDING

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

BRANDING = [ _UTEXAS_BRANDING ]

########################
# LOGOS

LOGO = [
    "portal",
    "utrc-cms/img/org_logos/tacc-white.png",
    "",
    "/",
    "_self",
    "TACC Logo",
    "anonymous",
    "True"
]

########################
# FAVICON

_FAVICON = {
    "img_file_src": "utrc-cms/img/org_logos/favicon.ico"
}
