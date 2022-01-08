from django.urls import path
from .import views

app_name='ajaxloginapp'
urlpatterns=[
	path('',views.home,name="home"),
	path('userlogin/',views.user_login,name="user_login"),
	path('userregister/',views.user_register,name="user_register"),
	path('userlogout/',views.user_logout,name="user_logout"),
	path('userdelete/',views.user_delete,name="user_delete"),
]