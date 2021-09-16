# TACC WMA CMS SITE: *.A2CPS.TACC.UTEXAS.EDU
# CUSTOM SETTINGS VALUES.

########################
# DJANGO SETTINGS
########################

# Boolean check to see if ldap is being used by the site.
# Requires django-auth-ldap ≥ 2.0.0
LDAP_ENABLED = True

########################
# DJANGO CMS SETTINGS
########################

# CMS Site (allows for multiple sites on a single CMS)
SITE_ID = 1

CMS_TEMPLATES = (
    ('a2cps-cms/templates/standard.html', 'Standard'),
    ('a2cps-cms/templates/fullwidth.html', 'Full Width'),

    # May or may not be used; we can remove them when that is confirmed
    ('guide.html', 'Guide'),
    ('guides/getting_started.html', 'Guide: Getting Started'),
    ('guides/data_transfer.html', 'Guide: Data Transfer'),
    ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
    ('guides/portal_technology.html', 'Guide: Portal Technology Stack')
)

CMS_PERMISSION = True

########################
# FEATURES
########################

"""
Features for the CMS that can be turned either ON or OFF

Usage:

- For baked-in features, like BRANDING or PORTAL, see relevant section instead.
- For optional features, look below, and enable feature(s) via _FEATURES list.

Baked-In Feature Setting Example.

# Desctipion of feature X
# SEE: [link to user/div guide about feature]
FEATURE_A = "someValue"

Optional Feature Toggle Example.

FEATURES = {
    # Desctipion of feature X
    # SEE: [link to user/dev guide about feature]
    "X": True,

    # Desctipion of feature Y
    # SEE: [link to user/dev guide about feature]
    "Y": False,

    # Desctipion of feature Z
    # SEE: [link to user/dev guide about feature]
    "Z": True,
}

"""

FEATURES = {
    # Blog/News & Social Media Metadata
    # GL-42: Split this into two features
    # SEE: https://confluence.tacc.utexas.edu/x/EwDeCg
    # SEE: https://confluence.tacc.utexas.edu/x/FAA9Cw
    "blog": False,
}

########################
# BRANDING & LOGOS
########################
# TODO: GH-59: Use Dict Not Array for Branding Settings

# Branding settings for portal and navigation.

"""
Additional Branding and Portal Logos for Partner & Affiliate Organizations

Usage:

- For each beand used in the templating, add corresponding new settings values to this file  (see example below).
- New branding settings must be added to the BRANDING list to render in the template.
- The order of the BRANDING list determines the rendering order of the elements in the template.
- The portal logo setting must be assigned to the LOGO variable to render in the template.
- The following VALUES for new elements set in the configuration object must exist in the portal css as well:
    - Any new selectors or css styles (add to /taccsite_cms/static/site_cms/css/src/_imports/branding_logos.css)
    - Image files being references (add to /taccsite_cms/static/site_cms/img/org_logos)

Values to populate:

_SETTING_NAME = [                 # The name of the branding or logo config setting object.
    "org_name",                         # The name of the organization the branding belongs too.
    "img_file_src",                      # Path and filename relative to the static files folder.
    "img_element_classes",        # The list of selectors to apply to the rendered element, these need to exist in the css/scss.
    "a_target_url",                      # The href link to follow when clicked, use "/" for portal logos.
    "a_target_type",                    # The target to open the new link in, use _blank for external links, _self for internal links.
    "alt_text",                             # The text to read or render for web assistance standards.
    "cors_setting",                      # The CORS setting for the image, set to anonymous by default.
    "visibility"                             # Toggles wether or not to display the element in the template, use True to render, False to hide.
]

Branding Configuration Example.

_ANORG_BRANDING = [
   "anorg",
   "site_cms/img/org_logos/anorg-logo.png"
   "branding-anorg",
   "https://www.anorg.com/"
   "_blank",
   "ANORG Logo",
   "anonymous",
   "True"
]

Logo Configuration Example.

_ANORG_LOGO = [
   "anorg",
   "site_cms/img/org_logos/anorg-logo.png"
   "branding-anorg",
   "/"
   "_self",
   "ANORG Logo",
   "anonymous",
   "True"
]
"""

########################
# BRANDING
########################

_TACC_BRANDING = [
    "tacc",
    "site_cms/img/org_logos/tacc-white.png",
    "branding-tacc",
    "https://www.tacc.utexas.edu/",
    "_blank",
    "TACC Logo",
    "anonymous",
    "True"
]

_UTEXAS_BRANDING = [
    "utexas",
    "site_cms/img/org_logos/utaustin-white.png",
    "branding-utaustin",
    "https://www.utexas.edu/",
    "_blank",
    "University of Texas at Austin Logo",
    "anonymous",
    "True"
]

_NSF_BRANDING = [
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

_ANORG_BRANDING = []

# Add custom SPONSOR_BRANDING assets here.
_CUSTOM_BRANDING = [_ANORG_BRANDING, _TACC_BRANDING, _UTEXAS_BRANDING]

# NSF Funded TACC Portal.
_NSF_SPONSORED_BRANDING = [_NSF_BRANDING, _TACC_BRANDING, _UTEXAS_BRANDING]

# Default TACC Portal.
_DEFAULT_BRANDING = [_TACC_BRANDING, _UTEXAS_BRANDING]

# Assign branding selection.
BRANDING = _DEFAULT_BRANDING

########################
# LOGOS
########################

_PORTAL_LOGO = [
    "portal",
    "site_cms/img/org_logos/portal.png",
    "",
    "/",
    "_self",
    "Portal Logo",
    "anonymous",
    "True"
]

_A2CPS_LOGO = [
    "a2cps",
    "a2cps-cms/img/org_logos/a2cps.png",
    "",
    "/",
    "_self",
    "A2CPS: Acute to Chronic Pain Signatures",
    "anonymous",
    "True"
]

LOGO = _A2CPS_LOGO               # Default Portal Logo.

########################
# FAVICON
########################

_PORTAL_FAVICON = {
    "img_file_src": "site_cms/img/favicons/favicon.ico"
}

FAVICON = _PORTAL_FAVICON               # Default Favicon.

########################
# PORTAL
########################

INCLUDES_CORE_PORTAL = True     # True for any CMS that is part of a Portal.

"""
Portal Links

Usage:

- For each link used in the templating, add new links values (see example below).
- New links must be added to the PORTAL_AUTH_LINKS and PORTAL_UNAUTH_LINKS lists.
- The order of the PORTAL_[…]_LINKS lists determine the rendering order of the elements.

Values to populate:

NAMED_LINK = {                    # The name of the link object.
    "name": "…",                       # The name of the link (to distinguish it, as if for ID).
    "url": "…",                        # The URL path to which the link should navigate the user.
    "text": "…",                       # The text of the link.
    "icon": "…",                       # The icon of the link.
}

Links Configuration Example.

ANY_AUTH_LINK = {
    "name": "section-1",
    "url": "/some/section/",
    "text": "Visit Section",
    "icon": "some-section",
}

ANY_UNAUTH_LINK = {
    "name": "action-1",
    "url": "/some-action/",
    "text": "Do Action",
    "icon": "some-action",
}

"""

########################
# LINKS (for Portal).
########################

_DASH_AUTH_LINK = {
    "name": "dash",
    "url": "/workbench/dashboard/",
    "text": "My Dashboard",
    "icon": "desktop",
}

_PROFILE_AUTH_LINK = {
    "name": "profile",
    "url": "/accounts/profile/",
    "text": "My Account",
    "icon": "user-circle",
}

_LOGOUT_AUTH_LINK = {
    "name": "logout",
    "url": "/accounts/logout/",
    "text": "Log Out",
    "icon": "sign-out-alt",
}

_LOGIN_UNAUTH_LINK = {
    "name": "login",
    "url": "/login/",
    "text": "Log In",
    "icon": "sign-in-alt",
}

# Default TACC Portal.
PORTAL_AUTH_LINKS = [_DASH_AUTH_LINK, _PROFILE_AUTH_LINK, _LOGOUT_AUTH_LINK]

# Default TACC Portal.
PORTAL_UNAUTH_LINKS = [_LOGIN_UNAUTH_LINK]

# Export any overrides to the Container.
# Exported settings.
SETTINGS_EXPORT = [
    'BRANDING',
    'LOGO',
    'FAVICON',
    'GOOGLE_ANALYTICS_PROPERTY_ID',
    'GOOGLE_ANALYTICS_PRELOAD'
]
