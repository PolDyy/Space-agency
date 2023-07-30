from django.urls import path

from app_landing.views import MainPageView

urlpatterns = [
    path("",
         MainPageView.as_view(), ),
]