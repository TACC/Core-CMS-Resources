# TACC CMS Per-Site Resources - Configuration

# In a project-specific configuration file like this, edit existing configuration values from `cms-site-template:/taccsite_cms/default_secrets.py` that must change to suit this project.

# Until this custom configuration is automatically applied, to use it one must copy the content of it and append it to `cms-site-template:/taccsite_cms/secrets.py`

# EXAMPLE CONFIGURATION

########################
# DJANGO SETTINGS
########################

_LDAP_ENABLED = True

########################
# DJANGO CMS SETTINGS
########################

_CMS_TEMPLATES = (
    ('3dem-org/templates/fullwidth.html', 'Fullwidth'),
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
# BRANDING & LOGOS & FAVICONS
########################

########################
# BRANDING

_BRANDING = [_NSF_BRANDING, _TACC_BRANDING, _UTEXAS_BRANDING]

########################
# LOGOS

_PORTAL_LOGO = [
    "3Dem",
    "3dem-org/img/org_logos/3dem.png",
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

_PORTAL_FAVICON = {
    "img_file_src": "3dem-org/img/favicons/favicon.ico"
}

_FAVICON = _PORTAL_FAVICON                # Default Favicon.

########################
# PORTAL
########################

_PORTAL = False
