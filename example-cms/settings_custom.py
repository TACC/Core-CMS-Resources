# CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# *.PROJECT_DOMAIN.TACC.UTEXAS.EDU

########################
# DJANGO CMS SETTINGS
########################

# CMS_TEMPLATES = (
#     ('standard.html', 'Standard'),
#     ('fullwidth.html', 'Full Width'),

#     # Support placeholder Portal homepage
#     ('home_portal.html', 'Standard Portal Homepage'),

#     # Support temporary Portal guide pages
#     ('guide.html', 'Guide'),
#     ('guides/getting_started.html', 'Guide: Getting Started'),
#     ('guides/data_transfer.html', 'Guide: Data Transfer'),
#     ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
#     ('guides/portal_technology.html', 'Guide: Portal Technology Stack'),
# )

########################
# BRANDING
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
# LOGOS
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
# PORTAL
########################

# Should a user be able to see link to Portal? (default value: True)
# INCLUDES_CORE_PORTAL = False # True to show login link, False to hide login link
