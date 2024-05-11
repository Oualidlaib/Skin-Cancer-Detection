from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.urls import path
from .views import signup, change_email, change_username, reset_password
from django.contrib.auth.views import (
    PasswordResetDoneView,
    PasswordResetConfirmView,
)
app_name = 'account'
urlpatterns = [
    path('register/', signup),
    path('change-email/', change_email),
    path('change-username/', change_username),
    path('reset-password/', reset_password),
    path('password-reset/done/', PasswordResetDoneView.as_view(
        template_name='account/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='account/password_reset_confirm.html'), name='password_reset_confirm'),

]
