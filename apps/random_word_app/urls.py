from django.conf.urls import url
from . import views

urlpatterns = [
    # Continuing the route to our index
    url(r'^$', views.index)
]