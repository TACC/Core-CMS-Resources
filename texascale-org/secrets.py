import os

# …

########################
# DJANGO CMS SETTINGS
########################

# …
_CMS_TEMPLATES = (
    # ('fullwidth.html', 'Fullwidth'),
    ('texascale-org/templates/fullwidth.html', 'Fullwidth'),
    ('texascale-org/templates/category.html', 'Category'),
    # ('sidebar_left.html', 'Sidebar Left'),
    # ('sidebar_right.html', 'Sidebar Right')
)

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
