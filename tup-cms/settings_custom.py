# CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# *.TUP.TACC.UTEXAS.EDU

########################
# DJANGO SETTINGS
########################

LDAP_ENABLED = False

########################
# DJANGO CMS SETTINGS
########################

CMS_TEMPLATES = (
    ('tup-cms/templates/fullwidth.html', 'Fullwidth')
)

########################
# GOOGLE ANALYTICS
########################

GOOGLE_ANALYTICS_PROPERTY_ID = "UA-96034853-2"

########################
# LOGOS.
########################

PORTAL_LOGO = [
    "tup",
    "tup-cms/img/org_logos/tacc-logo.svg",
    "",
    "/",
    "_self",
    "TACC Logo",
    "anonymous",
    "True"
]

LOGO = PORTAL_LOGO

########################
# PORTAL
########################

INCLUDES_CORE_PORTAL = False
