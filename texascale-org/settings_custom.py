import os

# …

########################
# DJANGO CMS SETTINGS
########################

# …
CMS_TEMPLATES = (
    ('texascale-org/templates/fullwidth.html', 'Fullwidth'),
    ('texascale-org/templates/category.html', 'Category'),
    ('texascale-org/templates/article.html', 'Article'),
    ('texascale-org/templates/article.freeform.html', 'Article (Free-Form)'),
    ('texascale-org/templates/article.sidebar-right.html', 'Article (Right Sidebar)'),
    ('texascale-org/templates/article.visual.html', 'Article (Full-Size Visual)'),
    ('texascale-org/templates/article.image-map.html', 'Article (Image Map)'),
)

########################
# GOOGLE ANALYTICS
########################

GOOGLE_ANALYTICS_PROPERTY_ID = "UA-125525035-18"
GOOGLE_ANALYTICS_PRELOAD = True

########################
# BRANDING & LOGOS
########################

# …

########################
# LOGOS.

TEXASCALE_LOGO =  [
    "texascale",
    "texascale-org/img/org_logos/texascale-wordmark.png",
    "",
    "/",
    "_self",
    "Texascale Logo",
    "anonymous",
    "True"
]

LOGO = _TEXASCALE_LOGO
