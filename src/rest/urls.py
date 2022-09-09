from django.urls import path
from .views import PasteRenderAPIView, PasteCreateAPIView

# from .views import HelloView, PasteCreateAPIView, PasteRetriveAPIView


urlpatterns = [
    path("", PasteCreateAPIView.as_view()),
    path(
        "<str:short_url>",
        PasteRenderAPIView.as_view({"get": "retrieve"}),
        name="api_paste_detail",
    ),
]
