## CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# SCIVISCOLOR.ORG

########################
# DJANGO CMS SETTINGS
########################

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
# BRANDING & LOGOS
########################

########################
# LOGOS

LOGO =  [
    "texascale",
    "texascale-org/img/org_logos/texascale-wordmark.png",
    "",
    "/",
    "_self",
    "Texascale Logo",
    "anonymous",
    "True"
]

########################
# PORTAL
########################

INCLUDES_CORE_PORTAL = False
