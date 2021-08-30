# TACC CMS Per-Site Resources - Configuration

# In a project-specific configuration file like this, edit existing configuration values from `cms-site-template:/taccsite_cms/default_secrets.py` that must change to suit this project.

# Until this custom configuration is automatically applied, to use it one must copy the content of it and append it to `cms-site-template:/taccsite_cms/secrets.py`

# PROTX CONFIGURATION

########################
# DJANGO SETTINGS
########################

_LDAP_ENABLED = True

########################
# DJANGO CMS SETTINGS
########################

_CMS_TEMPLATES = (
    ('protx-cms/templates/fullwidth.html', 'Fullwidth'),

    ('guide.html', 'Guide'),
    ('guides/getting_started.html', 'Guide: Getting Started'),
    ('guides/data_transfer.html', 'Guide: Data Transfer'),
    ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
    ('guides/portal_technology.html', 'Guide: Portal Technology Stack')
)

########################
# GOOGLE ANALYTICS
########################

_GOOGLE_ANALYTICS_PROPERTY_ID = "UA-125525035-##"
_GOOGLE_ANALYTICS_PRELOAD = True

########################
# BRANDING.
########################


# Add custom sponsor branding assets here.
# One unique entry per asset.

_COOKS_BRANDING = [
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
_CUSTOM_BRANDING = [_COOKS_BRANDING, _TACC_BRANDING, _UTEXAS_BRANDING]

# NSF Funded TACC Portal.
_NSF_SPONSORED_BRANDING = [_NSF_BRANDING, _TACC_BRANDING, _UTEXAS_BRANDING]

# Default TACC Portal.
_DEFAULT_BRANDING = [_TACC_BRANDING, _UTEXAS_BRANDING]

# Assign branding selection.
_BRANDING = _CUSTOM_BRANDING

########################
# LOGOS.
########################

_PORTAL_LOGO = [
    "protx",
    "protx-cms/img/org_logos/protx-logo-temp.png",
    "",
    "/",
    "_self",
    "ProTX Logo",
    "anonymous",
    "True"
]

_LOGO = _PORTAL_LOGO

########################
# PORTAL
########################

_PORTAL = True
