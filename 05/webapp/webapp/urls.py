from django.contrib import admin
from django.urls import path
from marks.views import index, SaveMarks, ShowData, Result

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),        
    path('SaveMarks/', SaveMarks),
    path('ShowData/', ShowData),   
    path('result/', Result),  
]
