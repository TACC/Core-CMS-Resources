# …

########################
# DJANGO CMS SETTINGS
########################

# …

_CMS_TEMPLATES_LIST = list(_CMS_TEMPLATES)
_CMS_TEMPLATES_LIST.insert(0, ('frontera-cms/templates/fullwidth.html', 'Frontera Fullwidth'))
_CMS_TEMPLATES = tuple(_CMS_TEMPLATES_LIST)

# …

########################
# LOGOS.

_FRONTERA_LOGO =  [
    "frontera",
    "frontera-cms/images/org_logos/frontera-white-solo.png",
    "",
    "/",
    "_self",
    "Frontera Logo",
    "anonymous",
    "True"
]

_LOGO = _FRONTERA_LOGO

# …
