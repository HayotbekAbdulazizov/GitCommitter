from unicodedata import name
from django.urls import path,include
from .import views
from django.utils.translation import gettext as _
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog


app_name = 'main'

urlpatterns = [
	path('',views.HomePageView.as_view(), name='home'),
]