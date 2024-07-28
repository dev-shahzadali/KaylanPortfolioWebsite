from projects import views
from django.urls import path

urlpatterns = [
    path('', views.projects, name='projects'),
    path('category/<slug:category_slug>/', views.projects, name='projects_by_category'),
    path('category/<slug:category_slug>/<slug:project_slug>/', views.project_detail, name='project_detail'),
]
