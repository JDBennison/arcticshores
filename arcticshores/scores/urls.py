from django.urls import path

from . import views

urlpatterns = [
    path('create-candidate', views.create_candidate, name='create_candidate'),
    path('create-score', views.create_score, name='create_score'),
    path('get-candidate/<candidate_ref>', views.get_candidate, name='get_candidate'),
]
