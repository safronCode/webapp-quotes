from django.urls import path


from . import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('storage/', views.storage_page, name='storage-page'),
]