## CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# TEXASCALE(-DEV).TACC.UTEXAS.EDU

from taccsite_cms.settings import *

########################
# DJANGO CMS SETTINGS
########################

CMS_TEMPLATES = (
    ('fullwidth.html', 'Fullwidth'),
    ('category.html', 'Category'),
    ('article.html', 'Article'),
    ('article.freeform.html', 'Article (Free-Form)'),
    ('article.sidebar-right.html', 'Article (Right Sidebar)'),
    ('article.visual.html', 'Article (Full-Size Visual)'),
    ('article.image-map.html', 'Article (Image Map)'),
)

# FP-1645: Remove CMS_TEMPLATES_DEPRECATED
CMS_TEMPLATES_DEPRECATED = (
    ('texascale-org/templates/fullwidth.html', 'DEPRECATED Fullwidth'),
    ('texascale-org/templates/category.html', 'DEPRECATED Category'),
    ('texascale-org/templates/article.html', 'DEPRECATED Article'),
    ('texascale-org/templates/article.freeform.html', 'DEPRECATED Article (Free-Form)'),
    ('texascale-org/templates/article.sidebar-right.html', 'DEPRECATED Article (Right Sidebar)'),
    ('texascale-org/templates/article.visual.html', 'DEPRECATED Article (Full-Size Visual)'),
    ('texascale-org/templates/article.image-map.html', 'DEPRECATED Article (Image Map)'),
)
CMS_TEMPLATES += CMS_TEMPLATES_DEPRECATED

########################
# TACC: LOGOS
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
# TACC: PORTAL
########################

INCLUDES_CORE_PORTAL = False

########################
# NEWS / BLOG
########################

INSTALLED_APPS += [
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
# CLIENT BUILD SETTINGS
########################

# TACC/Core-CMS-Resources#75: Load custom urls.py so we can add urlpatterns for taggit_autosuggest
ROOT_URLCONF = TACC_CUSTOM_ROOT + '.texascale-org.urls'

########################
# IMPORT & EXPORT
########################

try:
    from taccsite_cms.settings_local import *
except ModuleNotFoundError:
    pass
