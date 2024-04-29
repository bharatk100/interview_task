from django.urls import path
from .views import RegisterAPI, MyTokenObtainPairView, ChangePasswordView, ProfileSettingView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/", RegisterAPI.as_view(), name="register"),
    path("token", MyTokenObtainPairView.as_view(), name="token_obtain"),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path("password/change", ChangePasswordView.as_view(), name="change_password"),
    path("profile/", ProfileSettingView.as_view(), name="profile"),
    path("profile/<int:pk>", ProfileSettingView.as_view(), name="profile"),
]
