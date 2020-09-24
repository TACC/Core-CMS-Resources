import os

# …

########################
# DJANGO CMS SETTINGS
########################

# …

_CMS_TEMPLATES_LIST = list(_CMS_TEMPLATES)
_CMS_TEMPLATES_LIST.insert(0, ('texascale-org/templates/fullwidth.html', 'Texascale Fullwidth'))
_CMS_TEMPLATES = tuple(_CMS_TEMPLATES_LIST)

########################
# GOOGLE ANALYTICS
########################

_GOOGLE_ANALYTICS_PROPERTY_ID = "UA-125525035-18"
_GOOGLE_ANALYTICS_PRELOAD = True

########################
# BRANDING & LOGOS
########################

# …

########################
# LOGOS.

_TEXASCALE_LOGO =  [
    "texascale",
    "texascale-org/img/org_logos/texascale-wordmark.png",
    "",
    "/",
    "_self",
    "Texascale Logo",
    "anonymous",
    "True"
]

_LOGO = _TEXASCALE_LOGO

# …
