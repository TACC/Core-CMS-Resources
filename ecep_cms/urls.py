# -*- coding: utf-8 -*-
from taccsite_cms.urls import *

from django.conf.urls import include, url

urlpatterns += [
    # Support `taggit_autosuggest` (from `djangocms-blog`)
    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
]
