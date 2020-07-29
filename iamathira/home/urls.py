from django.conf.urls import url
from .views import (
    home, intro,)

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^', intro, name='intro')
]