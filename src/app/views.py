from .models import Paste

from .forms import PasteForm
from .services import MakePasteExpiredService, SharePasteService
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View


class PasteView(LoginRequiredMixin, View):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    template_name = "paste/form.html"

    def get(self, request):
        form = PasteForm()

        return render(request, self.template_name, {"formset": form})

    def post(self, request):
        form = PasteForm(request.POST)
        if form.is_valid():
            paste = SharePasteService().execute(
                expired_at=form.data.get("expired_at"),
                content=form.data.get("content"),
                permanent_delete=form.data.get("permanent_delete") == "on",
                user=request.user,
                name=form.data.get("name"),
            )

            return redirect("paste_detail", short_url=paste.short_url)

        return render(request, self.template_name, {"formset": form})


class PasteRendererView(View):
    template_name = "paste/show.html"

    def get(self, request, short_url):
        paste = get_object_or_404(Paste.active_records, short_url=short_url)
        MakePasteExpiredService().execute(paste, request.user)

        return render(request, self.template_name, {"paste": paste})
