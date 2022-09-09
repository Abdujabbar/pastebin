from django.urls import path
from .views import PasteView, PasteRendererView

# from .views import HelloView, PasteCreateAPIView, PasteRetriveAPIView


urlpatterns = [
    path("", PasteView.as_view(), name="new-paste"),
    path("<str:short_url>", PasteRendererView.as_view(), name="paste_detail"),
]
