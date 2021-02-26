from django.urls import path
from app import views as core_views
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('home/', core_views.home, name='home'),
    path('login/', LoginView.as_view(template_name='MyApp/login.html', redirect_authenticated_user=True),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='signup'), name='logout'),
    path('', core_views.signup, name='signup'),
    path('add/', core_views.add, name='add'),
    path('show/', core_views.show_add_form, name='show_add_form')
]