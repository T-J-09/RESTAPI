from django.urls import path
from .views import *
urlpatterns = [
    path('client/', clientapi.as_view(), name="client"),
    path('clientdel/<int:pk>/',clientdtl.as_view(),),
    path('project/',projapi.as_view(),name='project'),

]