# TACC WMA CMS SITE: *.PROTX.TACC.UTEXAS.EDU
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
    ('protx-cms/templates/standard.html', 'Standard'),
    ('protx-cms/templates/fullwidth.html', 'Full Width'),

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
# BRANDING.
########################

COOKS_BRANDING = [
    "cooks",
    "protx-cms/img/org_logos/CClogo_Standard_White_Transparent.png",
    "branding-tacc",
    "https://cookchildrens.org",
    "_blank",
    "Cooks Childrens Logo",
    "anonymous",
    "True"
]

CUSTOM_BRANDING = [COOKS_BRANDING, TACC_BRANDING, UTEXAS_BRANDING]

########################
# LOGOS.
########################

LOGO = [
    "protx",
    "protx-cms/img/org_logos/ProTx-logo-nobg.png",
    "",
    "/",
    "_self",
    "ProTX Logo",
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
