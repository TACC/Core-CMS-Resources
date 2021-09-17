# TACC CMS Per-Site Resources - Configuration

# In a project-specific configuration file like this, edit existing configuration values from `cms-site-template:/taccsite_cms/default_secrets.py` that must change to suit this project.

# Until this custom configuration is automatically applied, to use it one must copy the content of it and append it to `cms-site-template:/taccsite_cms/secrets.py`

# UTRC CONFIGURATION

########################
# DJANGO SETTINGS
########################

_LDAP_ENABLED = True

########################
# DJANGO CMS SETTINGS
########################

_CMS_TEMPLATES = (
    ('utrc-cms/templates/standard.html', 'Standard'),
    ('utrc-cms/templates/fullwidth.html', 'Full Width'),

    # NOTE: v1 did not have data_transfer nor portal_technology
    ('guide.html', 'Guide'),
    ('guides/getting_started.html', 'Guide: Getting Started'),
    ('guides/data_transfer.html', 'Guide: Data Transfer'),
    ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
    ('guides/portal_technology.html', 'Guide: Portal Technology Stack')
)

########################
# GOOGLE ANALYTICS
########################

_GOOGLE_ANALYTICS_PROPERTY_ID = "UA-125525035-4"
_GOOGLE_ANALYTICS_PRELOAD = True

########################
# BRANDING
########################

########################
# LOGOS

_UTRC_LOGO = [
    "utrc",
    "utrc-cms/img/org_logos/tacc-white.png",
    "",
    "/",
    "_self",
    "UTRC Logo",
    "anonymous",
    "True"
]

_LOGO = _PORTAL_LOGO

########################
# FAVICON

_FAVICON = {
    "img_file_src": "utrc-cms/img/org_logos/favicon.ico"
}

########################
# PORTAL
########################

_PORTAL = True
