from django.urls import path

from . import views


app_name = 'test_form'
urlpatterns = [
	path('', views.index, name='index'),
	#path('<int:question_id>/', views.testing, name='testing'),
	path('group/<int:group_id>/', views.testing, name='testing'),

	path('results/', views.results, name='results'),
#    path('', views.IndexView.as_view(), name='index'),
#    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#    path('<int:question_id>/vote/', views.vote, name='vote'),
]
