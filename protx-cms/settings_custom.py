
# Until this custom configuration is automatically applied, to use it one must copy the content of it and append it to `cms-site-template:/taccsite_cms/secrets.py`

# PROTX CONFIGURATION

########################
# DJANGO SETTINGS
########################

LDAP_ENABLED = True

########################
# DJANGO CMS SETTINGS
########################

CMS_TEMPLATES = (
    ('protx-cms/templates/standard.html', 'Standard'),
    ('protx-cms/templates/fullwidth.html', 'Full Width'),

    ('guide.html', 'Guide'),
    ('guides/getting_started.html', 'Guide: Getting Started'),
    ('guides/data_transfer.html', 'Guide: Data Transfer'),
    ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
    ('guides/portal_technology.html', 'Guide: Portal Technology Stack')
)

########################
# GOOGLE ANALYTICS
########################

GOOGLE_ANALYTICS_PROPERTY_ID = "UA-125525035-##"
GOOGLE_ANALYTICS_PRELOAD = True

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

# ???: Must we have this? It's in Core settings, already
_TACC_BRANDING = [
    "tacc",
    "site_cms/img/org_logos/tacc-white.png",
    "branding-tacc",
    "https://www.tacc.utexas.edu/",
    "_blank",
    "TACC Logo",
    "anonymous",
    "True"
]

# ???: Must we have this? It's in Core settings, already
_UTEXAS_BRANDING = [
    "utexas",
    "site_cms/img/org_logos/utaustin-white.png",
    "branding-utaustin",
    "https://www.utexas.edu/",
    "_blank",
    "University of Texas at Austin Logo",
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
