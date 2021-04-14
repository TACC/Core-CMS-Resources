# TACC CMS Per-Site Resources - Configuration

# In a project-specific configuration file like this, edit existing configuration values from `cms-site-template:/taccsite_cms/default_secrets.py` that must change to suit this project.

# Until this custom configuration is automatically applied, to use it one must copy the content of it and append it to `cms-site-template:/taccsite_cms/secrets.py`

# EXAMPLE CONFIGURATION

########################
# DJANGO SETTINGS
########################

_LDAP_ENABLED = False

########################
# DJANGO CMS SETTINGS
########################

_CMS_TEMPLATES = (
    ('example-cms/templates/fullwidth.html', 'Fullwidth'),
    # Support standard template for demo purposes
    ('fullwidth.html', 'Standard Fullwidth'),

    # Support Portal pages for demo purposes
    ('home_portal.html', 'Standard Portal Homepage'),
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
# BRANDING SETTINGS
########################

# …

########################
# BRANDING.

_BRANDING = [_NSF_BRANDING, _TACC_BRANDING, _UTEXAS_BRANDING]

########################
# LOGOS.

_PORTAL_LOGO = [
    "portal",
    "example-cms/img/org_logos/portal.png",
    "",
    "/",
    "_self",
    "Portal Logo",
    "anonymous",
    "True"
]

_LOGO = _PORTAL_LOGO

########################
# PORTAL
########################

_PORTAL = False
