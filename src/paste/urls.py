from django.urls import path
from .views import PasteRetriveAPIView, PasteCreateAPIView, index

urlpatterns = [
    path('', index),
    path('store', PasteCreateAPIView.as_view()),
    path('<int:pk>', PasteRetriveAPIView.as_view()),
]