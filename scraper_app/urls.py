from django.contrib import admin
from django.urls import path
from scraper_app.views import index,Anjita

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('Anjita/',Anjita),
    
    path('',index)
]
