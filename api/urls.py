from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.healthcheck),
    path('upload-file/', views.upload_file),
    path('upload-file-fail/', views.upload_file_fail),

]