from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'), name='api'),   
    path('', include('main.urls'), name='main')   

]