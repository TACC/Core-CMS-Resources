# CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# *.PROJECT_DOMAIN.TACC.UTEXAS.EDU

########################
# DJANGO CMS SETTINGS
########################

# CMS_TEMPLATES = (
#     ('standard.html', 'Standard'),
#     ('fullwidth.html', 'Full Width'),

#     # Portal homepage placeholder
#     ('home_portal.html', 'Standard Portal Homepage'),

#     # Portal guide pages
#     ('guide.html', 'Guide'),
#     ('guides/getting_started.tam.html', 'Guide: Getting Started'),
#     # ('guides/getting_started.v2.html', 'Guide: Getting Started'),
#     ('guides/data_transfer.html', 'Guide: Data Transfer'),
#     ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
#     ('guides/portal_technology.html', 'Guide: Portal Technology Stack'),
# )

########################
# TACC: BRANDING
########################

# from taccsite_cms.settings import TACC_BRANDING, UTEXAS_BRANDING, NSF_BRANDING
#
# _CUSTOM_BRANDING = [
#     "example",
#     "example-cms/img/org_logos/example-logo.png",
#     "",
#     "https://example.com",
#     "_blank",
#     "Example Logo",
#     "anonymous",
#     "True"
# ]

# BRANDING = [ TACC_BRANDING, UTEXAS_BRANDING, NSF_BRANDING, _CUSTOM_BRANDING ]

########################
# TACC: LOGOS
########################

LOGO =  [
    "example",
    "example-cms/img/org_logos/portal.png",
    "",
    "/",
    "_self",
    "Placeholder Logo for CMS/Portal",
    "anonymous",
    "True"
]

########################
# TACC: PORTAL
########################

# Should a user be able to see link to Portal? (default value: True)
# INCLUDES_CORE_PORTAL = False # True to show login link, False to hide login link
