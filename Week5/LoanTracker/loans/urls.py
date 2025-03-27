from django.urls import path
from . import views


urlpatterns = [
    path('list', views.LoanListView.as_view(), name='listview'),
    path('detail/<int:pk>', views.LoanDetailView.as_view(), name='detailview'),
    path('create', views.LoanCreateView.as_view(), name='createview'),
    path('update/<int:pk>', views.LoanUpdateView.as_view(), name='updateview'),
]
