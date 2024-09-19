from django.urls import path
from first_app.views import First_App_View, First_App_Second_View

urlpatterns = [
    path('first_app',First_App_View.as_view(), name='first_app'),

    path('second_app/<int:pk>', First_App_Second_View.as_view(), name='second_app')
]
