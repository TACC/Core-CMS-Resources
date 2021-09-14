
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


# Add custom sponsor branding assets here.
# One unique entry per asset.

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

# Add custom _SPONSOR_BRANDING assets here.
CUSTOM_BRANDING = [COOKS_BRANDING, TACC_BRANDING, UTEXAS_BRANDING]

# NSF Funded TACC Portal.
NSF_SPONSORED_BRANDING = [NSF_BRANDING, TACC_BRANDING, UTEXAS_BRANDING]

# Default TACC Portal.
DEFAULT_BRANDING = [TACC_BRANDING, UTEXAS_BRANDING]

# Assign branding selection.
BRANDING = CUSTOM_BRANDING

########################
# LOGOS.
########################

PORTAL_LOGO = [
    "protx",
    "protx-cms/img/org_logos/protx-logo-temp.png",
    "",
    "/",
    "_self",
    "ProTX Logo",
    "anonymous",
    "True"
]

LOGO = PORTAL_LOGO

########################
# PORTAL
########################

INCLUDES_CORE_PORTAL = True
