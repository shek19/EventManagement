# users/urls.py


from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtain tokens
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh tokens
]




# from django.urls import path
# from .views import RegisterView, LoginView

# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='register'),
#     path('login/', LoginView.as_view(), name='login'),
# ]
