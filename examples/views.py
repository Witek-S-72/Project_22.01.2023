from django.core.exceptions import ObjectDoesNotExist
#from django.http import Http404
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import PersonalData

# Create your views here.
def test_view(request):
    return render(request, 'examples/base.html')

def exercise(request):
    return render(request,'examples/exercise.html')

# def personal_data_detail(request, id):
#     try:
#         personal_data = PersonalData.objects.get(id=id)
#     except ObjectDoesNotExist:
#         raise Http404
#
#     ctx = {'personal_data': personal_data}
#     return render(request, 'examples/personal_data_detail.html', ctx)

def personal_data_detail(request, id):
    personal_data = get_object_or_404(PersonalData, id=id)
    ctx = {'personal_data':personal_data}
    return render (request, 'examples/personal_data_detail.html', ctx)

def personal_data_list(request):
    personal_data = PersonalData.objects.all()
    ctx = {'personal_data': personal_data}
    return render(request, 'examples/personal_data_list.html', ctx)










