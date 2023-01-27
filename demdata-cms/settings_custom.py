# CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# *.DEMOCTRATIZING-SITE.TACC.UTEXAS.EDU

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

# To change LDAP auth settings for a custom CMS Project (e.g. `epoc-cms`):
# 1. Copy the setting from `settings.py`
# 2. Assign the new value in `Core-CMS/taccsite_custom/epoc-cms/settings_custom.py`.
AUTH_LDAP_SERVER_URI = "ldap://cluster.ldap.tacc.utexas.edu"

# The same goes for other more commonly customized values like below.

########################
# TACC: PORTAL
########################

# Does this CMS site have a portal (default value: True)?
INCLUDES_CORE_PORTAL = False 
INCLUDES_PORTAL_NAV = False
INCLUDES_SEARCH_BAR = False

########################
# DJANGO CMS SETTINGS
########################

CMS_TEMPLATES = (
    ('standard.html', 'Standard'),
    ('fullwidth.html', 'Full Width'),
    ('guide.html', 'Guide'),
    ('guides/getting_started.tam.html', 'Guide: Getting Started'),
    ('guides/data_transfer.html', 'Guide: Data Transfer'),
    ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
    ('guides/portal_technology.html', 'Guide: Portal Technology Stack')
)

########################
# TACC: LOGOS
########################

LOGO = [ 
    "tacc",
    "demdata-cms/img/org_logos/tacc-white.png",
    "",
    "/",
    "_self",
    "TACC Logo",
    "anonymous",
    "True"
]

FAVICON = {
    "img_file_src": "demdata-cms/img/favicons/favicon.ico"
}

