from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import VaccinationSchedule, Children, Vaccination
from .forms import VaccinationScheduleForm, ChildrenForm, VaccinationForm


def index(request):
    return render(request, 'Privivki/index.html')


def children_list(request):
    queryset = Children.objects.all()
    context = {
        'queryset': queryset,
        'title': 'Дети'
    }
    return render(request, 'Privivki/children_list.html', context)


def children_create(request):
    form = ChildrenForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('/Privivki')
    context = {
        'form': form,
    }
    return render(request, 'Privivki/children_create.html', context)


def children_update(request, pk):
    children = get_object_or_404(Children, pk=pk)
    if request.method == 'POST':
        form = ChildrenForm(request.POST, instance=children)
        if form.is_valid():
            form.save()
            return redirect('Privivki/children_list')
    else:
        form = ChildrenForm(instance=children)
    return render(request, 'Privivki/children_form.html', {'form': form})


def children_delete(request, pk):
    children = get_object_or_404(Children, pk=pk)
    children.delete()
    return HttpResponseRedirect('/Privivki')


def vaccination_schedule_list(request):
    queryset = VaccinationSchedule.objects.all()
    context = {
        'queryset': queryset,
        'title': 'Журнал прививок'
    }
    return render(request, 'Privivki/vaccination_schedule_list.html', context)


def vaccination_schedule_create(request):
    form = VaccinationScheduleForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('/Privivki')
    context = {
        'form': form,
    }
    return render(request, 'Privivki/vaccination_schedule_create.html', context)


def vaccination_schedule_detail(request, pk=None):
    instance = get_object_or_404(VaccinationSchedule, pk=pk)
    context = {
        'title':'Детали',
        'instance':instance,
    }
    return render(request, 'Privivki/vaccination_schedule_detail.html', context)


def vaccination_schedule_update(request, pk=None):
    instance = get_object_or_404(VaccinationSchedule, pk=pk)
    form = VaccinationScheduleForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('/Privivki')
    context = {
        'title': "Обновить данные",
        'instance': instance,
        'form': form,
        'what_to_do': 'Обновить',
    }
    return render(request, 'Privivki/vaccination_schedule_create.html', context)


def vaccination_schedule_delete(request, pk):
    vaccination_schedule = get_object_or_404(VaccinationSchedule, pk=pk)
    vaccination_schedule.delete()
    return HttpResponseRedirect('/Privivki')
