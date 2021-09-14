
# Until this custom configuration is automatically applied, to use it one must copy the content of it and append it to `cms-site-template:/taccsite_cms/secrets.py`

# EXAMPLE CONFIGURATION

########################
# DJANGO SETTINGS
########################

LDAP_ENABLED = True

########################
# DJANGO CMS SETTINGS
########################

CMS_TEMPLATES = (
    ('neuronex-cms/templates/fullwidth.html', 'Fullwidth'),
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

GOOGLE_ANALYTICS_PROPERTY_ID = "UA-125525035-1"
GOOGLE_ANALYTICS_PRELOAD = True

########################
# BRANDING & LOGOS
########################

########################
# BRANDING.

BRANDING = [NSF_BRANDING, TACC_BRANDING, UTEXAS_BRANDING]

########################
# LOGOS.

PORTAL_LOGO = [
    "portal",
    "neuronex-cms/img/org_logos/logo.3dem.png",
    "",
    "/",
    "_self",
    "3Dem Logo",
    "anonymous",
    "True"
]

LOGO = PORTAL_LOGO

########################
# FAVICON

FAVICON = {
    "img_file_src": "neuronex-cms/img/org_logos/favicon.ico"
}

########################
# PORTAL
########################

INCLUDES_CORE_PORTAL = True
