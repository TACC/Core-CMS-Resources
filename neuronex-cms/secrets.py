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
    ('neuronex-cms/templates/fullwidth.html', 'Fullwidth'),
    ('guide.html', 'Guide'),
    ('guides/getting_started.html', 'Guide: Getting Started'),
    ('guides/data_transfer.html', 'Guide: Data Transfer'),
    ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
    ('guides/portal_technology.html', 'Guide: Portal Technology Stack')
)

########################
# GOOGLE ANALYTICS
########################

_GOOGLE_ANALYTICS_PROPERTY_ID = "UA-125525035-1"
_GOOGLE_ANALYTICS_PRELOAD = True

########################
# BRANDING & LOGOS
########################

########################
# BRANDING.

_BRANDING = [_NSF_BRANDING, _TACC_BRANDING, _UTEXAS_BRANDING]

########################
# LOGOS.

_PORTAL_LOGO = [
    "portal",
    "neuronex-cms/img/org_logos/logo.3dem.png",
    "",
    "/",
    "_self",
    "3Dem Logo",
    "anonymous",
    "True"
]

_LOGO = _PORTAL_LOGO

########################
# FAVICON

_NEURONEX_FAVICON = {
    "img_file_src": "neuronex-cms/img/org_logos/favicon.ico"
}

_FAVICON = _NEURONEX_FAVICON

########################
# PORTAL
########################

_PORTAL = True
