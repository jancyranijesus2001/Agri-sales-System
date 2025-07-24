from django.shortcuts import render, redirect, get_object_or_404
from store.models.waste import Waste
from store.forms import WasteForm

def waste_list(request):
    wastes = Waste.objects.all()
    return render(request, 'waste_list.html', {'wastes': wastes})

def waste_create(request):
    if request.method == 'POST':
        form = WasteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('waste_list')
    else:
        form = WasteForm()
    return render(request, 'waste_form.html', {'form': form})

def waste_update(request, id):
    waste = get_object_or_404(Waste, id=id)
    if request.method == 'POST':
        form = WasteForm(request.POST, request.FILES, instance=waste)
        if form.is_valid():
            form.save()
            return redirect('waste_list')
    else:
        form = WasteForm(instance=waste)
    return render(request, 'waste_form.html', {'form': form})

def waste_delete(request, id):
    waste = get_object_or_404(Waste, id=id)
    if request.method == 'POST':
        waste.delete()
        return redirect('waste_list')
    return render(request, 'waste_confirm_delete.html', {'waste': waste})

def waste_purchase(request, id):
    waste = get_object_or_404(Waste, id=id)
    waste.status = 'Purchased'
    waste.save()
    return redirect('waste_list')
