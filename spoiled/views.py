from django.shortcuts import render, redirect, get_object_or_404
from spoiled.models import Spoiled, Nomenclature
from django.db.models import Q
from spoiled.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from django.views.generic import TemplateView
from spoiled.forms import SpoiledForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseBadRequest

class SpoiledListView(OwnerListView):
    model = Spoiled
    template_name = 'spoiled/spoiled_list.html'

    def get(self, request, pk_shop):
        spoileds = self.model.objects.filter(shop=pk_shop)
        context = {}
        context['spoiled_list'] = spoileds
        context['shop'] = pk_shop
        create_file = self.request.GET.get('create_file_spoiled')
        if create_file:
            print(create_file)
        return render(request, self.template_name, context)


class SpoiledDetailView(OwnerDetailView):
    model = Spoiled
    template_name = "spoiled/detail.html"

class SpoiledCreateView(LoginRequiredMixin, View):
    template_name = "spoiled/spoiled_form.html"

    def get(self, request, pk_shop):
        try:
            barcode = request.GET['barcode']
            nomen = Nomenclature.objects.filter(Q(barcode=barcode) & Q(shop=pk_shop))
            data = {
                'nomenclature': nomen[0].pk,
                'shop': pk_shop
            }
            form = SpoiledForm(data)
            ctx = {'form': form}
            ctx['shop'] = pk_shop

        except IndexError:
            return redirect(reverse_lazy("spoiled:all", kwargs={'pk_shop': pk_shop}))

        return render(request, self.template_name, ctx)

    def post(self, request, pk_shop):
        form = SpoiledForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form }
            ctx['shop'] = pk_shop
            return render(request, self.template_name, ctx)

        spoil = form.save(commit=False)
        spoil.owner = self.request.user
        spoil.save()

        return redirect(reverse_lazy("spoiled:all", kwargs={'pk_shop': pk_shop}))

class SpoiledUpdateView(LoginRequiredMixin, View):
    template_name = "spoiled/spoiled_form.html"

    def get(self, request, pk):
        spoiled = get_object_or_404(Spoiled, id=pk, owner=self.request.user)
        form = SpoiledForm(instance=spoiled)
        ctx = {'form': form}
        ctx['shop'] = spoiled.shop.id
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        spoiled = get_object_or_404(Spoiled, id=pk, owner=self.request.user)
        form = SpoiledForm(request.POST, request.FILES or None, instance=spoiled)

        if not form.is_valid():
            ctx = {'form': form }
            return render(request, self.template_name, ctx)

        spoiled = form.save(commit=False)
        spoiled.save()
        print(spoiled)
        pk_shop = spoiled.shop.id

        return redirect(reverse_lazy("spoiled:all", kwargs={'pk_shop': pk_shop}))


class SpoiledDeleteView(OwnerDeleteView):
    model = Spoiled
    template_name = "spoiled/delete.html"
    def post(self, request, pk, **kwargs):
        spoiled = get_object_or_404(Spoiled, id=pk, owner=self.request.user)
        pk_shop = spoiled.shop.id
        spoiled.delete()
        return redirect(reverse_lazy("spoiled:all", kwargs={'pk_shop': pk_shop}))




def stream_file(request, pk):
    pic = get_object_or_404(Spoiled, pk=pk)
    response = HttpResponse()
    response['Content-Type'] = pic.content_type
    response['Content-Length'] = len(pic.picture)
    response.write(pic.picture)
    print(response)
    return response

































