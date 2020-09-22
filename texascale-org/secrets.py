import os

# …

########################
# ASSETS.

# Specify from which directory in `taccsite_custom` to pull custom assets
_CUSTOM_ASSET_DIR = "texascale-org"

# …

########################
# DJANGO CMS SETTINGS
########################

# …

_CMS_TEMPLATES_LIST = list(_CMS_TEMPLATES)
_CMS_TEMPLATES_LIST.insert(0, ('texascale-org/templates/fullwidth.html', 'Frontera Fullwidth'))
_CMS_TEMPLATES = tuple(_CMS_TEMPLATES_LIST)

# …

########################
# LOGOS.

_TEXASCALE_LOGO =  [
    "texascale",
    "site_cms/images/org_logos/texascale-wordmark.png",
    "",
    "/",
    "_self",
    "Texascale Logo",
    "anonymous",
    "True"
]

_LOGO = _TEXASCALE_LOGO

# …
