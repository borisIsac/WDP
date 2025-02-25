from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import *
from rest_framework_simplejwt.views import  TokenVerifyView

app_name = 'users'

urlpatterns = [
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CustomRefreshTokenView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView().as_view(), name="token_verify"),
    path('api/notes/', get_notes, name='get_notes'),
    path('api/logout/', logout, name = 'logout'),
    path('api/is_authenticated/', is_authenticated, name="is_authenticated"),
    path('api/signup/', RegisterView.as_view(), name='user_register'),
    path('api/profile/', UserProfileView.as_view(), name='user_profile'),

    path('password_change/', auth_views.PasswordChangeView.as_view(success_url='/users/password_change/done/'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # PASSWORD RESET
    path('password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name="users/password_reset_form.html",
            email_template_name="users/password_reset_email.html",
            success_url=reverse_lazy("users:password_reset_done")
        ),
        name='password_reset'
    ),

    path('password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html"
        ),
        name='password_reset_done'),

    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="users/password_reset_confirm.html",
        success_url=reverse_lazy("users:password_reset_complete")
        ),
         name='password_reset_confirm'
    ),

    path('password-reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name='password_reset_complete'),    

    path('activation_sended/', activation_sended, name='activation_sended'),
]
