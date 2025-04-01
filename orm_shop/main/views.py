from django.http import Http404
from django.shortcuts import render

from main.models import Car, Sale


def cars_list_view(request):
    # получите список авто
    all_cars = Car.objects.all()
    context = { 'cars': all_cars }
    template_name = 'main/list.html'
    return render(request, template_name, context)  # передайте необходимый контекст


def car_details_view(request, car_id):
    # получите авто, если же его нет, выбросьте ошибку 404
    try:
        car = Car.objects.get(pk=car_id) # to get a certain car
    except Car.DoesNotExist:
        raise Http404()
    template_name = 'main/details.html'
    return render(request, template_name, {'car': car})  # передайте необходимый контекст


def sales_by_car(request, car_id):
    try:
        # получите авто и его продажи
        car = Car.objects.get(pk=car_id)
        sales = Sale.objects.filter(car=car_id)
        template_name = 'main/sales.html'
        return render(request, template_name, {'car': car, 'sales': sales})  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')
    except Sale.DoesNotExist:
        raise Http404('Sale not found')
