# TACC WMA CMS SITE: *.A2CPS.TACC.UTEXAS.EDU
# CUSTOM SETTINGS VALUES.

########################
# DJANGO SETTINGS
########################

LDAP_ENABLED = True

########################
# DJANGO CMS SETTINGS
########################

SITE_ID = 1

CMS_TEMPLATES = (
    ('a2cps-cms/templates/standard.html', 'Standard'),
    ('a2cps-cms/templates/fullwidth.html', 'Full Width'),
    ('guide.html', 'Guide'),
    ('guides/getting_started.html', 'Guide: Getting Started'),
    ('guides/data_transfer.html', 'Guide: Data Transfer'),
    ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
    ('guides/portal_technology.html', 'Guide: Portal Technology Stack')
)

CMS_PERMISSION = True

########################
# GOOGLE ANALYTICS
########################

GOOGLE_ANALYTICS_PROPERTY_ID = "UA-125525035-##"
GOOGLE_ANALYTICS_PRELOAD = False

########################
# LOGOS
########################

LOGO = [
    "a2cps",
    "a2cps-cms/img/org_logos/a2cps.png",
    "",
    "/",
    "_self",
    "A2CPS: Acute to Chronic Pain Signatures",
    "anonymous",
    "True"
]

########################
# PORTAL
########################

INCLUDES_CORE_PORTAL = True

########################
# EXPORT
########################

SETTINGS_EXPORT = [
    'BRANDING',
    'LOGO',
    'FAVICON',
    'GOOGLE_ANALYTICS_PROPERTY_ID',
    'GOOGLE_ANALYTICS_PRELOAD'
]
