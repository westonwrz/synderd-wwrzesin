from django.urls import path
from . import views

app_name='courses' #CHANGE ME

urlpatterns = [
    path('subjects/', views.SubjectListView.as_view(), name='subject_list'),
    path('subjects/<pk>/', views.SubjectDetailView.as_view(),
    name='subject_detail'),
]