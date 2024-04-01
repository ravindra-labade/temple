from django.shortcuts import render, redirect
from .forms import TempleForm
from .models import Temple



def add_temple(request):
    template_name = 'temple/add.html'
    form = TempleForm()
    if request.method == 'POST':
        form = TempleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)


def show_temple(request):
    template_name = 'temple/show.html'
    temples = Temple.objects.all()
    context = {'temples': temples}
    return render(request, template_name, context)


def update_temple(request, pk):
    template_name = 'temple/add.html'
    obj = Temple.objects.get(id=pk)
    form = TempleForm(instance=obj)
    if request.method == 'POST':
        form = TempleForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)



def delete_temple(request, pk):
    obj = Temple.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    return render(request, 'temple/confirm.html')