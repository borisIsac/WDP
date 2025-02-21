from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import *
from rest_framework_simplejwt.views import  TokenVerifyView

app_name = 'users'

urlpatterns = [
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CustomRefreshTokenView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView().as_view(), name="token_verify"),
    path('notes/', get_notes, name='get_notes'),
    path('logout/', logout, name = 'logout'),
    path('is_authenticated/', is_authenticated, name="is_authenticated"),
    path('sign_up/', sign_up, name="sign_up"),


    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register_user/', RegisterView.as_view(), name='register_user'),
    path ('profile/', ProfileView.as_view(), name='profile'),
    path('activate/<uidb64>/<token>/', RegisterView.as_view(), name='activate_account'),
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
