# CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# _*.EPOC.TACC.UTEXAS.EDU
# https:///epoc.global

'''
A `settings_custom.py` file can override default values in `settings.py`.

The file is loaded after default settings but before settings assignment is complete, so we can override settings in:
- _either_ `settings_custom.py` (usually set in custom sites)
- _or_ in `settings_local.py` (usually used in a local dev environment)

To override a setting:
1. Copy/Paste the default settings.
2. Set the new/custom values.

If a setting override is for a custom CMS Project, the change is made in the `settings_custom.py` file of that project's directory and (if not a secret) can be committed.

Unless modifying default behavior for the CMS Core (and thus all custom Projects) (which probably means that setting should be in the `settings.py` file), the `settings_custom.py` file that should be modified is the one in the appropriate CMS Project directory.
'''

########################
# WALKTHROUGH
########################

# To change LDAP auth settings for a custom CMS Project (e.g. `epoc_cms`):
# 1. Copy the setting from `settings.py`
# 2. Assign the new value in `Core-CMS/taccsite_custom/epoc_cms/settings_custom.py`.
AUTH_LDAP_SERVER_URI = "ldap://cluster.ldap.tacc.utexas.edu"

# The same goes for other more commonly customized values like below.

########################
# TACC: PORTAL
########################

# Does this CMS site have a portal?
INCLUDES_CORE_PORTAL = False
INCLUDES_PORTAL_NAV = False
INCLUDES_SEARCH_BAR = False

########################
# DJANGO CMS SETTINGS
########################

CMS_TEMPLATES = (
    ('standard.html', 'Standard'),
    ('fullwidth.html', 'Full Width'),

    # # Portal homepage placeholder
    # ('home_portal.html', 'Standard Portal Homepage'),

    # # Portal guide pages
    # ('guide.html', 'Guide'),
    # ('guides/getting_started.tam.html', 'Guide: Getting Started'),
    # # ('guides/getting_started.v2.html', 'Guide: Getting Started'),
    # ('guides/data_transfer.html', 'Guide: Data Transfer'),
    # ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
    # ('guides/portal_technology.html', 'Guide: Portal Technology Stack'),
)

########################
# TACC: BRANDING
########################

# LOOK INTO THIS SOLUTION.
# from taccsite_cms.settings import TACC_BRANDING, UTEXAS_BRANDING, NSF_BRANDING

TACC_BRANDING = [
    "tacc",
    "epoc_cms/img/org_logos/tacc-white.png",
    "branding-tacc",
    "https://www.tacc.utexas.edu/",
    "_blank",
    "TACC Logo",
    "anonymous",
    "True"
]

UTEXAS_BRANDING = [
    "utexas",
    "epoc_cms/img/org_logos/utaustin-white.png",
    "branding-utaustin",
    "https://www.utexas.edu/",
    "_blank",
    "University of Texas at Austin Logo",
    "anonymous",
    "True"
]

NSF_BRANDING = [
    "nsf",
    "epoc_cms/img/org_logos/nsf-white.png",
    "branding-nsf",
    "https://www.nsf.gov/",
    "_blank",
    "NSF Logo",
    "anonymous",
    "True"
]

CUSTOM_BRANDING = [
    "epoc",
    "epoc_cms/img/org_logos/esnet-white-logo.png",
    "branding-logo--short",
    "https://www.es.net/",
    "_blank",
    "ESnet Logo",
    "anonymous",
    "True",
]

BRANDING = [ TACC_BRANDING, UTEXAS_BRANDING, CUSTOM_BRANDING ]

########################
# TACC: LOGOS
########################

LOGO =  [
    "epoc",
    "epoc_cms/img/org_logos/epoc-color-logo.png",
    "",
    "/",
    "_self",
    "Logo or EPOC Global Portal",
    "anonymous",
    "True"
]

FAVICON = {
    "img_file_src": "epoc_cms/img/org_logos/favicon.ico"
}