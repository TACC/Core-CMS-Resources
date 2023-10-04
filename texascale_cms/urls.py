# -*- coding: utf-8 -*-
from taccsite_cms.urls import *

from django.urls import include, re_path

urlpatterns += [
    # Support `taggit_autosuggest` (from `djangocms-blog`)
    re_path(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
]
