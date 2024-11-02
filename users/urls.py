# users/urls.py


from django.urls import path
from .views import PasswordResetRequestView, PasswordResetView, RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtain tokens
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh tokens

    path('password_reset_request/',PasswordResetRequestView.as_view(),name='password_reset_request'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
]




# from django.urls import path
# from .views import RegisterView, LoginView

# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='register'),
#     path('login/', LoginView.as_view(), name='login'),
# ]
