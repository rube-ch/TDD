from django.shortcuts import redirect, render
from django.http import HttpResponse

from lists.models import Item

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])  #2
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})

