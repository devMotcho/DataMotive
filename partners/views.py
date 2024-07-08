from django.shortcuts import render, redirect , get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Partner
from .forms import PartnerForm


def partnersTable(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    partners = Partner.objects.filter(
        Q(name__icontains=q) |
        Q(address__icontains=q) |
        Q(email__icontains=q)
    )

    form = PartnerForm()
    if request.method == 'POST':
        form = PartnerForm(request.POST)
        if form.is_valid():
            partner = form.save()
            if partner.is_client == True:
                messages.success(request, " Added a new Cliente.")
                return redirect()
            elif partner.is_supplier == True:
                messages.success(request, " Added a new Supplier.")
            else:
                messages.info(request, "Don't forget to say if is a Client or a Supplier.")
        else:
            messages.error(request, f'{form.errors}')
            

    context = {
        'objs':partners,
    }
    return render(request, 'partners/table.html', context)


def partnersDetail(request, pk):
    partner = get_object_or_404(Partner, id=pk)

    context = {
        'obj':partner,
    }
    return render(request, "partners/detail.html", context)


def partnersDelete(request, pk):
    partner = get_object_or_404(Partner, id=pk)
    if request.method == 'POST':
        partner.delete()
        messages.success(request, f"Partner {partner.name} deleted!")
        return redirect('partners:table')
    return render(request, "delete.html", {"obj":partner})