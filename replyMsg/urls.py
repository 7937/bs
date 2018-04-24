from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.question, name='question'),
    url(r'^mutualFriends$', views.mutualFriends, name='mutualFriends'),
]
