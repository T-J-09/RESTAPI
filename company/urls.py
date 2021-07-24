from django.urls import include, path

from .views import RegView

urlpatterns=[
    path('reg/',RegView.as_view())
]