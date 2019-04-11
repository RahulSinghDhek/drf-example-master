from django.conf.urls import url
from action_jobs.views import ViewSetCRUD, ViewSetList
#
# urlpatterns = [
#     url(r'^$', ViewSetList.as_view(), name='list-actions'),
#     url(r'^(?P<pk>[0-9]+)/?$', ViewSetCRUD.as_view(), name='crud-action')
#    ]

from django.conf.urls import url
from action_jobs.views import ViewSetCRUD, ViewSetList
urlpatterns = [
    url(r'^$', ViewSetList.as_view(), name='album-list'),
    url(r'^(?P<pk>[0-9]+)/?$', ViewSetCRUD.as_view(), name='track-list'),
]