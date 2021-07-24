from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('company.urls')),
    path('api/', include('CLPROJ.urls')),

]