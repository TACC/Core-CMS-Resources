# CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
#   ENV.PROJECT-DOMAIN.TACC.UTEXAS.EDU

# EXAMPLE CONFIGURATION

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
# BRANDING
########################

BRANDING = [NSF_BRANDING, TACC_BRANDING, UTEXAS_BRANDING]

########################
# LOGOS.
########################

LOGO = [
    "portal",
    "example-cms/img/org_logos/portal.png",
    "",
    "/",
    "_self",
    "Portal Logo",
    "anonymous",
    "True"
]

########################
# PORTAL
########################

INCLUDES_CORE_PORTAL = False
