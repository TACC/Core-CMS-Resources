# TACC CMS Per-Site Resources - Configuration

# In a project-specific configuration file like this, edit existing configuration values from `cms-site-template:/taccsite_cms/default_secrets.py` that must change to suit this project.

# Until this custom configuration is automatically applied, to use it one must copy the content of it and append it to `cms-site-template:/taccsite_cms/secrets.py`

# EXAMPLE CONFIGURATION

########################
# DJANGO SETTINGS
########################

_LDAP_ENABLED = True

########################
# DJANGO CMS SETTINGS
########################

_CMS_TEMPLATES = (
    ('a2cps-cms/templates/standard.html', 'Standard'),
    ('a2cps-cms/templates/fullwidth.html', 'Full Width')
)

########################
# GOOGLE ANALYTICS
########################

_GOOGLE_ANALYTICS_PROPERTY_ID = "UA-125525035-10"
_GOOGLE_ANALYTICS_PRELOAD = True

########################
# BRANDING & LOGOS
########################

########################
# BRANDING.

_BRANDING = [_TACC_BRANDING, _UTEXAS_BRANDING]

########################
# LOGOS.

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

_LOGO = _A2CPS_LOGO

########################
# PORTAL
########################

_PORTAL = True
