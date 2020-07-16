from django.contrib import admin
from django.urls import path,include
from users import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('signin/',auth_views.LoginView.as_view(template_name='login.html'),name='signin'),
    
    path('signout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='signout'),
    path('signup/',views.signup,name='signup'),
    path('profile_update/',views.profile,name='profile_update'),

    path('',include('frontend.urls')),
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)



