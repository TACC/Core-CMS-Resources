# CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# *.democemocratizing-site.TACC.UTEXAS.EDU


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

