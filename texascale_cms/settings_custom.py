# CUSTOM SETTINGS VALUES.
# TACC WMA (SAD) CMS SITE:
# *.TEXASCALE.TACC.UTEXAS.EDU

########################
# DJANGO_CMS
########################

CMS_TEMPLATES = (
    ('texascale_cms/templates/fullwidth.html', 'Fullwidth'),
    ('texascale_cms/templates/category.html', 'Category'),
    ('texascale_cms/templates/article.html', 'Article'),
    ('texascale_cms/templates/article.freeform.html', 'Article (Free-Form)'),
    ('texascale_cms/templates/article.sidebar-right.html', 'Article (Right Sidebar)'),
    ('texascale_cms/templates/article.visual.html', 'Article (Full-Size Visual)'),
    ('texascale_cms/templates/article.image-map.html', 'Article (Image Map)'),

    # DEPRECATED
    ('texascale-org/templates/fullwidth.html', 'DEPRECATED Fullwidth'),
    ('texascale-org/templates/category.html', 'DEPRECATED Category'),
    ('texascale-org/templates/article.html', 'DEPRECATED Article'),
    ('texascale-org/templates/article.freeform.html', 'DEPRECATED Article (Free-Form)'),
    ('texascale-org/templates/article.sidebar-right.html', 'DEPRECATED Article (Right Sidebar)'),
    ('texascale-org/templates/article.visual.html', 'DEPRECATED Article (Full-Size Visual)'),
    ('texascale-org/templates/article.image-map.html', 'DEPRECATED Article (Image Map)'),
)

########################
# TACC: LOGO & FAVICON
########################

LOGO = [
    "texascale",
    "texascale_cms/img/org_logos/texascale-wordmark.png",
    "",
    "/",
    "_self",
    "Texascale Logo",
    "anonymous",
    "True"
]

########################
# TACC: PORTAL
########################

INCLUDES_CORE_PORTAL = False
INCLUDES_PORTAL_NAV = False
INCLUDES_SEARCH_BAR = False

########################
# DJANGOCMS_BLOG
########################

from taccsite_cms.settings import INSTALLED_APPS

tacc_app_index = INSTALLED_APPS.index('taccsite_cms')
INSTALLED_APPS[tacc_app_index:tacc_app_index] = [
    # 'filer',              # already in Core
    # 'easy_thumbnails',    # already in Core
    'parler',
    'taggit',
    'taggit_autosuggest',
    # 'meta',               # already in Core
    'sortedm2m',
    'djangocms_blog',
]
# REQ: 'taggit_autosuggest' requires the following is added to `urls.py`
"""
urlpatterns += [
    # Support `taggit_autosuggest` (from `djangocms-blog`)
    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
]
"""

# Paths for alternate templates that user can choose for blog-specific plugin
# - Devs can customize core templates at `templates/djangocms_blog/`.
# - Users can choose alt. templates from `templates/djangocms_blog/plugins/*`.
# - Devs can customize alt. templates at `templates/djangocms_blog/plugins/*`.
BLOG_PLUGIN_TEMPLATE_FOLDERS = (
    ('plugins', 'Default'),
    # ('plugins/alternate', 'Alternate'),
)

# Change default values for the auto-setup of one `BlogConfig`
# SEE: https://github.com/nephila/djangocms-blog/issues/629
BLOG_AUTO_SETUP = False # Set to False after setup (to minimize server overhead)
BLOG_AUTO_HOME_TITLE ='Home'
BLOG_AUTO_BLOG_TITLE = 'News'
BLOG_AUTO_APP_TITLE = 'News'
BLOG_AUTO_NAMESPACE = 'News'

# Miscellaneous settings
BLOG_ENABLE_COMMENTS = False

########################
# DJANGOCMS_BLOG: DJANGO
########################

# TACC/Core-CMS-Resources#75: Load custom urls.py so we can add urlpatterns for taggit_autosuggest
ROOT_URLCONF = 'taccsite_custom.texascale_cms.urls'

########################
# TACC: SOCIAL MEDIA
########################

TACC_SOCIAL_SHARE_PLATFORMS = ['facebook', 'linkedin', 'email']
