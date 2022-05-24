from django.urls import path
from .SparkApp.Views.vw_SparkUser import (authentificationRegister,)


app_name = "sparkUser"

urlpatterns = [
    path('register', authentificationRegister, name="register"),
    ]