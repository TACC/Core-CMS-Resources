
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

GOOGLE_ANALYTICS_PROPERTY_ID = "UA-125525035-##"
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
    "example-cms/img/org_logos/portal.png",
    "",
    "/",
    "_self",
    "Portal Logo",
    "anonymous",
    "True"
]

LOGO = PORTAL_LOGO

########################
# PORTAL
########################

INCLUDES_CORE_PORTAL = False
