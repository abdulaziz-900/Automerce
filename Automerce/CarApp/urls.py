from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.login_view, name="login"),
    path("home", views.allDisplayItems, name="home"),
    path("signup",views.signup_view,name="signup"),
    path("<int:carid>",views.displaySpecificItem, name="specific"),
    path("orders", views.displayUserOrders, name="orders"),
    path('update_car/<int:carid>/', views.updateCar, name='update_car'),
    path('delete/<int:carid>', views.delete, name='delete'),
    path('addcar',views.addCar,name='addcar')
]