from django.urls import path
from ..Views.vw_SparkUser import authentificationRegister


app_name = "SparkUser"

urlpatterns = [
    path('register', authentificationRegister, name="register"),
    ]