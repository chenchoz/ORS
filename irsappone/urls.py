from django.urls import path
from .views import IncidentList,IncidenDetail,IncidentCreate,IncidentUpdate,DeleteView,CustomLoginView,RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('login/', CustomLoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('register/', RegisterPage.as_view(),name='register'),
    path('', IncidentList.as_view(), name='incidents'),
    path('incident/<int:pk>/', IncidenDetail.as_view(), name='incident'),
    path('create-incident', IncidentCreate.as_view(), name='incident-create'),
    path('incident-update/<int:pk>/', IncidentUpdate.as_view(), name='incident-update'),
    path('incident-delete/<int:pk>/', DeleteView.as_view(), name='incident-delete'),







 
]