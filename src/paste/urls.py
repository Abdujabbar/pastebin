from django.urls import path
from .views import PasteRetriveAPIView, PasteCreateAPIView, HelloView

urlpatterns = [
    path('', HelloView.as_view()),
    path('store', PasteCreateAPIView.as_view()),
    path('<int:pk>', PasteRetriveAPIView.as_view()),
]