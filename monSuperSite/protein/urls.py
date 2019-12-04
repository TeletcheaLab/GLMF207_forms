from django.conf.urls import include,url

from protein.views import *

urlpatterns = [
    url(r'(?P<identifiant>\d+)', one_protein, name="one_protein"),
    url('add/', add, name="add"),
    url('add_boostrap/', add_boostrap, name="add_boostrap"),
]
