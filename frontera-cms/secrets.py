########################
# DJANGO SETTINGS
########################

# …

_LDAP_ENABLED = True

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
# GOOGLE ANALYTICS
########################

_GOOGLE_ANALYTICS_PROPERTY_ID = "UA-125525035-13"
_GOOGLE_ANALYTICS_PRELOAD = True

# …

########################
# BRANDING & LOGOS
########################

# …

########################
# BRANDING.

# …

_BRANDING = [ _NSF_BRANDING, _TACC_BRANDING, _UTEXAS_BRANDING ]

########################
# LOGOS.

_FRONTERA_LOGO =  [
    "frontera",
    "frontera-cms/img/org_logos/frontera-white-solo.png",
    "",
    "/",
    "_self",
    "Frontera Logo",
    "anonymous",
    "True"
]

_LOGO = _FRONTERA_LOGO

# …
