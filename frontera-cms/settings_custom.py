########################
# DJANGO SETTINGS
########################

# …

LDAP_ENABLED = True

# …

########################
# DJANGO CMS SETTINGS
########################

# …
CMS_TEMPLATES = (
    ('frontera-cms/templates/fullwidth.html', 'Fullwidth'),
    ('fullwidth.html', 'DEPRECATED Fullwidth'),

    ('frontera-cms/templates/home.html', 'Homepage'),

    ('guide.html', 'Guide'),
    ('guides/getting_started.html', 'Guide: Getting Started'),
    ('guides/data_transfer.html', 'Guide: Data Transfer'),
    ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
    ('guides/portal_technology.html', 'Guide: Portal Technology Stack')
)

########################
# GOOGLE ANALYTICS
########################

GOOGLE_ANALYTICS_PROPERTY_ID = "UA-125525035-13"
GOOGLE_ANALYTICS_PRELOAD = True

# …

########################
# BRANDING & LOGOS
########################

# …

########################
# BRANDING.

# …

TACC_BRANDING = [
    # …
    "frontera-cms/img/org_logos/tacc-white.png",
    # …
]

# …

BRANDING = [ NSF_BRANDING, TACC_BRANDING, UTEXAS_BRANDING ]

########################
# LOGOS.

FRONTERA_LOGO =  [
    "frontera",
    "frontera-cms/img/org_logos/frontera-white-solo.png",
    "",
    "/",
    "_self",
    "Frontera Logo",
    "anonymous",
    "True"
]

LOGO = FRONTERA_LOGO
# …

########################
# PORTAL
########################

PORTAL = True
