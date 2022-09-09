from app.models import Paste

from app.services import SharePasteService
from rest_framework.generics import CreateAPIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from app.services import MakePasteExpiredService
from .serializers import PasteSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.viewsets import ViewSet

# Create your views here.


class PasteCreateAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (
        SessionAuthentication,
        JWTAuthentication,
    )
    queryset = Paste.objects.all()
    serializer_class = PasteSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.instance = SharePasteService().execute(
            expired_at=request.data.get("expired_at"),
            content=request.data.get("content"),
            permanent_delete=request.data.get("permanent_delete") == "on",
            user=request.user,
            name=request.data.get("name"),
        )

        return Response(
            status=201,
            data=serializer.data,
        )


class PasteRenderAPIView(ViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (
        SessionAuthentication,
        JWTAuthentication,
    )
    queryset = Paste.objects.all()
    serializer_class = PasteSerializer

    def retrieve(self, request, short_url):
        paste = get_object_or_404(Paste.active_records, short_url=short_url)
        MakePasteExpiredService().execute(paste, request.user)
        serializer = PasteSerializer(paste)

        return Response(serializer.data)
