from django.urls import path
from . import views


app_name = 'test_form'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/answer/', views.answer, name='answer'),
    path('<int:group_id>/results/', views.results, name='results'),
]
