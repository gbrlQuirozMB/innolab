from django.shortcuts import render

from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="INNOLAB API",
        default_version='v1',
        description="Proyecto INNOLAB",
        # terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="gabriel@mb.company"),
        # license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
