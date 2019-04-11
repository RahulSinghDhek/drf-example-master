from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^action_job/', include('action_jobs.urls')),
    url(r'^shares/', include('shares.urls')),
]
