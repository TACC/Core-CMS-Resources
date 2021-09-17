# CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
#   ENV.PROJECT-DOMAIN.TACC.UTEXAS.EDU

########################
# DJANGO CMS SETTINGS
########################

CMS_TEMPLATES = (
    ('project-cms/templates/standard.html', 'Standard'),
    ('project-cms/templates/fullwidth.html', 'Full Width'),

    # May or may not be used; we can remove them when that is confirmed
    ('guide.html', 'Guide'),
    ('guides/getting_started.html', 'Guide: Getting Started'),
    ('guides/data_transfer.html', 'Guide: Data Transfer'),
    ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
    ('guides/portal_technology.html', 'Guide: Portal Technology Stack')
)

########################
# BRANDING
########################

TACC_BRANDING = [
    "tacc",
    "site_cms/img/org_logos/tacc-white.png",
    "branding-tacc",
    "https://www.tacc.utexas.edu/",
    "_blank",
    "TACC Logo",
    "anonymous",
    "True"
]

UTEXAS_BRANDING = [
    "utexas",
    "site_cms/img/org_logos/utaustin-white.png",
    "branding-utaustin",
    "https://www.utexas.edu/",
    "_blank",
    "University of Texas at Austin Logo",
    "anonymous",
    "True"
]

NSF_BRANDING = [
    "nsf",
    "site_cms/img/org_logos/nsf-white.png",
    "branding-nsf",
    "https://www.nsf.gov/",
    "_blank",
    "NSF Logo",
    "anonymous",
    "True"
]

# Add custom sponsor branding assets here.
# One unique entry per asset.

# Assign branding selection.
BRANDING = [TACC_BRANDING, UTEXAS_BRANDING]

########################
# LOGOS
########################

LOGO = [
    "portal",
    "site_cms/img/org_logos/portal.png",
    "",
    "/",
    "_self",
    "Portal Logo",
    "anonymous",
    "True"
]
