# CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# *.UTRC.TACC.UTEXAS.EDU

from taccsite_cms.settings import *

########################
# DJANGO CMS SETTINGS
########################

CMS_TEMPLATES = (
    ('standard.html', 'Standard'),
    ('fullwidth.html', 'Full Width'),

    ('home.html', 'Home'),

    ('guide.html', 'Guide'),
    ('guides/getting_started.html', 'Guide: Getting Started'),
    ('guides/data_transfer.html', 'Guide: Data Transfer'),
    ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
    ('guides/portal_technology.html', 'Guide: Portal Technology Stack')
)

# Deprecated Templates
# TODO: FP-1645: Remove
CMS_TEMPLATES += (
    ('utrc-cms/templates/home.html', 'DEPRECATED Home'),
)

########################
# TACC: LOGOS
########################

LOGO = [
    "portal",
    "utrc-cms/img/org_logos/utrc-horizontal-logo-white-simple.svg",
    "",
    "/",
    "_self",
    "UTRC Logo",
    "anonymous",
    "True"
]

FAVICON = {
    "img_file_src": "utrc-cms/img/org_logos/favicon.ico"
}

########################
# IMPORT & EXPORT
########################

try:
    from taccsite_cms.settings_local import *
except ModuleNotFoundError:
    pass
