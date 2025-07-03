from django.urls import path, re_path, include
from django.views.generic import TemplateView

from quotehub import views
from . import api

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('storage/', views.storage_page, name='storage-page'),
    path('api/', include([
        path('like_add/', api.like_add, name='like_add'),
        path('like_remove/', api.like_remove, name='like_remove'),
        path('dislike_add/', api.dislike_add, name='dislike_add'),
        path('dislike_remove/', api.dislike_remove, name='dislike_remove'),
        path('view_add/', api.view_add, name='view_add'),
        path('user_activity/', api.user_activity, name='user_activity'),
        path('get_quote/', api.get_quote, name='get_quote'),
        path('quote_list/', api.quote_list, name='quote_list'),
    ])),
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html'))
]

