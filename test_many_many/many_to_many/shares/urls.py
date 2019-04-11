from django.conf.urls import url
from shares.views import ShareRetrieveUpdateDeleteView, ShareList



urlpatterns = [
    url(r'^$', ShareList.as_view(), name='list-shares'),
    url(r'^(?P<pk>[0-9]+)/?$', ShareRetrieveUpdateDeleteView.as_view(), name='crud-action')
   ]