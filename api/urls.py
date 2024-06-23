from django.urls import path
from .views.routes import getRoutes
from .views.user_auth_views import *
from .views.Task_view import *

from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('',getRoutes.as_view()),
    path('token/',TokenObtainPairView.as_view(),name='token_obtain_pair'), #generate token
    
    path('refresh_token/',TokenRefreshView.as_view(),name='token_refresh'),
    
    path('register/',newuserRegistrationView.as_view()),
    path('login/',newuserLoginView.as_view()),
    path('upload/',DocumentUploadView.as_view()),
     path('download/<int:pk>/', DocumentDownloadView.as_view(), name='document-download'),
    
]


