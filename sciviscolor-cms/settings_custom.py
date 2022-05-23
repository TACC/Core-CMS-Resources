# CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# SCIVISCOLOR.ORG

from taccsite_cms.settings import *

########################
# TACC: LOGOS
########################

LOGO = [
    "sciviscolor",
    "sciviscolor-cms/img/org_logos/sciviscolor-logo-white.png",
    "",
    "/",
    "_self",
    "SciVisColor Logo",
    "anonymous",
    "True"
]

FAVICON = {
    "img_file_src": "sciviscolor-cms/img/org_logos/favicon.ico"
}

########################
# TACC: PORTAL
########################

INCLUDES_CORE_PORTAL = False

########################
# IMPORT & EXPORT
########################

try:
    from taccsite_cms.settings_local import *
except ModuleNotFoundError:
    pass
