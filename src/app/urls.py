from django.urls import path
from .views import PasteView, PasteRendererView, PasteCreateAPIView
# from .views import HelloView, PasteCreateAPIView, PasteRetriveAPIView


urlpatterns = [
    path('', PasteView.as_view()),
    path('api', PasteCreateAPIView.as_view()),
    # path('<str:short_url>', PasteRendererView.as_view(), name='paste_detail'),
]