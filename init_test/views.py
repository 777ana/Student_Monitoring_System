from django.shortcuts import render
from .models import test


# Create your views here.
def take_test(request):
    # if request.method=='POST':
    #
    # else:
    if request.method == 'GET':
        exam = test.objects.all()
        return render(request, 'take_test.html', {'exam': exam})
