import os

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
    "texascale-org/images/org_logos/texascale-wordmark.png",
    "",
    "/",
    "_self",
    "Texascale Logo",
    "anonymous",
    "True"
]

_LOGO = _TEXASCALE_LOGO

# …
