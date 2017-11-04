from django.conf.urls import url
from .views import LandingView, download_view


urlpatterns = [
    url(r'^$', LandingView.as_view(), name='view_landing'),
    url(r'^download/$', download_view, name='download_view'),
]