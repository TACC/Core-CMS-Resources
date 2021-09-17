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
# LOGOS.
########################

LOGO = [
    "tup",
    "tup-cms/img/org_logos/tacc-logo.svg",
    "",
    "/",
    "_self",
    "TACC Logo",
    "anonymous",
    "True"
]

########################
# PORTAL
########################

INCLUDES_CORE_PORTAL = False
