# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from server.views import NgFormValidationView, NgFormValidationViewWithNgModel


urlpatterns = patterns('',
    url(r'^simple_form/$', NgFormValidationView.as_view(), name='djng_form_validation'),
    url(r'^model_form/$', NgFormValidationViewWithNgModel.as_view(), name='djng_model_form_validation'),
)
