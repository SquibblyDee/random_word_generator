from django.conf.urls import url
from . import views

urlpatterns = [
    # Continuing the route to our index
    url(r'^$', views.index),
    #Continuing route to reset the count
    url(r'random_word/reset$', views.reset),
    #Continuing route to generate word
    url(r'generate$', views.generate)
]