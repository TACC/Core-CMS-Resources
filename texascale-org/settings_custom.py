## CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# SCIVISCOLOR.ORG

########################
# DJANGO CMS SETTINGS
########################

CMS_TEMPLATES = (
    ('texascale-org/templates/fullwidth.html', 'Fullwidth'),
    ('texascale-org/templates/category.html', 'Category'),
    ('texascale-org/templates/article.html', 'Article'),
    ('texascale-org/templates/article.freeform.html', 'Article (Free-Form)'),
    ('texascale-org/templates/article.sidebar-right.html', 'Article (Right Sidebar)'),
    ('texascale-org/templates/article.visual.html', 'Article (Full-Size Visual)'),
    ('texascale-org/templates/article.image-map.html', 'Article (Image Map)'),
)

########################
# LOGOS
########################

LOGO =  [
    "texascale",
    "texascale-org/img/org_logos/texascale-wordmark.png",
    "",
    "/",
    "_self",
    "Texascale Logo",
    "anonymous",
    "True"
]

########################
# PORTAL
########################

INCLUDES_CORE_PORTAL = False




########################
# FEATURES
########################

from taccsite_cms.settings import INSTALLED_APPS

FEATURES = {
    # Blog/News & Social Media Metadata
    # SEE: https://confluence.tacc.utexas.edu/x/EwDeCg
    # SEE: https://confluence.tacc.utexas.edu/x/FAA9Cw
    "blog": True,
}





########################
# BLOG
########################

# Install required apps
INSTALLED_APPS += [
    # Blog/News
    # 'filer',              # already added
    # 'easy_thumbnails',    # already added
    'parler',
    'taggit',
    'taggit_autosuggest',
    'meta',                 # also supports `djangocms_page_meta`
    'sortedm2m',
    'djangocms_blog',

    # Metadata
    'djangocms_page_meta',
]
# CAVEAT: 'taggit_autosuggest' requires the following is added to `urls.py`
"""
urlpatterns += [
    # Support `taggit_autosuggest` (from `djangocms-blog`)
    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
]
"""

# Metadata: Configure
META_SITE_PROTOCOL = 'http'
META_USE_SITES = True
META_USE_OG_PROPERTIES = True
META_USE_TWITTER_PROPERTIES = True
META_USE_GOOGLEPLUS_PROPERTIES = True # django-meta 1.x+
# META_USE_SCHEMAORG_PROPERTIES=True  # django-meta 2.x+

# Blog/News: Set custom paths for templates
BLOG_PLUGIN_TEMPLATE_FOLDERS = (
    ('plugins/default', 'Default template'),    # i.e. `templates/djangocms_blog/plugins/default/`
    ('plugins/default-clone', 'Clone of default template'),  # i.e. `templates/djangocms_blog/plugins/default-clone/`
)

# Blog/News: Change default values for the auto-setup of one `BlogConfig`
# SEE: https://github.com/nephila/djangocms-blog/issues/629
BLOG_AUTO_SETUP = True
BLOG_AUTO_HOME_TITLE ='Home'
BLOG_AUTO_BLOG_TITLE = 'News'
BLOG_AUTO_APP_TITLE = 'News'

########################
# CLIENT BUILD SETTINGS
########################

# TACC/Core-CMS-Resources#75: Load custom urls.py so we can add urlpatterns for taggit_autosuggest
ROOT_URLCONF = 'taccsite_custom.texascale-org.urls'
