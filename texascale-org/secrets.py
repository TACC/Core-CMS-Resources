import os

# …

########################
# DJANGO CMS SETTINGS
########################

# …
_CMS_TEMPLATES = (
    # ('fullwidth.html', 'Fullwidth'),
    # ('sidebar_left.html', 'Sidebar Left'),
    ('texascale-org/templates/fullwidth.html', 'Fullwidth'),
    ('texascale-org/templates/category.html', 'Category'),
    ('texascale-org/templates/article.html', 'Article'),
    ('texascale-org/templates/article.freeform.html', 'Article (Free-Form)'),
    ('texascale-org/templates/article.sidebar-right.html', 'Article (Right Sidebar)'),
    ('texascale-org/templates/article.image.html', 'Article (Full-Size Image)'),
    ('texascale-org/templates/article.image-map.html', 'Article (Image Map)'),
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
