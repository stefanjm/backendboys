from django.urls import path
from . import views

urlpatterns = [
    # /parkalot/
    path("", views.index, name="index"),

    # /parkalot/customer/5
    path('customer/<int:customer_id>/', views.customer, name="customer"),

    # /parkalot/manager
    path("manager/", views.manager, name="manager"),

    # /parklot/parked
    path("parked/", views.parked, name="parked"),
]
