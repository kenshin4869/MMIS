from django.shortcuts import render
from youxian import models


# Create your views here.
def add_goods(request):
    if request.method == "POST":
        publisher_name = request.POST.get("name")
        publisher_address = request.POST.get("address")
        models.Publisher.objects.create(name=publisher_name, address=publisher_address)
        return redirect('/youxian/goods_list')
    return render(request, 'add_publisher.html')
