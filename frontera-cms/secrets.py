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
_CMS_TEMPLATES = (
    # ('fullwidth.html', 'Fullwidth'),
    ('fontera-cms/templates/fullwidth.html', 'Fullwidth'),
    # ('sidebar_left.html', 'Sidebar Left'),
    # ('sidebar_right.html', 'Sidebar Right')
)

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
