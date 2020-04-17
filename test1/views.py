from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics
from .serializers import StatusSerializer
from .models import Status


class StatusView(generics.ListAPIView):
    serializer_class = StatusSerializer

    def get_queryset(self):
        queryset = Status.objects.all()
        return queryset

def homepage(request):
    mymod = Status.objects.all()

    if 'submit1' in request.POST :
        nam = request.POST['nam']
        shp = request.POST['shp']
        sts = request.POST['sts']

        try:
            io = Status()
            io.Status = str(sts)
            io.Name = str(nam)
            io.Shop_Name = str(shp)
            io.save()

        except:
            print('problem in db')

        if 'submit2' in request.POST :
            nam = request.POST['nam']
            shp = request.POST['shp']
            sts = request.POST['sts']

        try:
            io = Status.objects.get(Name=nam)
            io.Status = str(sts)
            io.Name = str(nam)
            io.Shop_Name = str(shp)
            io.save()

        except:
            print('problem in db')

    context = {
        'tablelist':mymod
    }
    return render(request,'home.html',context)


@csrf_exempt
def edit_val(request):
    myid = request.GET['id']
    myid = int(myid)
    mysta = Status.objects.get(id=myid)
    data = {
        'Message': 'Successfully Updated',
        'Name': mysta.Name,
        'dev_id': mysta.Status,
        'Vehicle_Number': mysta.Shop_Name,
    }
    return JsonResponse(data)

@csrf_exempt
def delete_device(request):
    myid = request.POST['id']
    myid = int(myid)
    print(myid)
    mydevices = Status.objects.get(id=myid)
    mydevices.delete()
    print(myid)
    data = {
        'Message': 'Successfully Deleted'
    }
    print(data)
    return JsonResponse(data)