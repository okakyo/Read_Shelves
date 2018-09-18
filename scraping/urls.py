from django.urls import path
from .views import Create_Article,Update_Article,Delete_Article,Index_Article

urlpatterns=(
    path('',Index_Article.as_view(),name='index'),
    path('create/',Create_Article.as_view(),name='create'),
    path('update/<int:pk>',Update_Article.as_view(),name='update'),
    path('delete/<int:pk>',Delete_Article.as_view(),name='delete')
)