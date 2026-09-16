from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . models import Category, Item
from core.forms import ReportItemForm
from django.db.models import Q

# Create your views here.
@login_required
def ReportItemView(request):
    if request.method == 'POST':
        form = ReportItemForm(request.POST,request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.reported_by = request.user
            item.status = 'open'
            item.save()
            return redirect('home')

    else:
        form = ReportItemForm()

    return render(request,'reportitem.html', {'form':form})


from django.shortcuts import render, get_object_or_404
from .models import Item


def ItemDetailsView(request, pk):
    item = get_object_or_404(Item, pk=pk)

    return render(request, 'details.html', {'item': item})

def ItemSearchView(request):
    items = Item.objects.all()

    search = request.GET.get('search','')
    category = request.GET.get('category','')
    status = request.GET.get('status','')
    item_type = request.GET.get('item_type','')


    if search:
        items = items.filter(Q(name__icontains=search)|
                             Q(description__icontains=search)|
                             Q(location__icontains=search)
                             )

    if category:
        items = items.filter(category_id = category)

    if status:
        items = items.filter(status = status)

    if item_type:
        items = items.filter(item_type = item_type)

    categories = Category.objects.all()


    context = {
        'items':items,
        'categories':categories,
        'search':search,
        'selected_category':category,
        'selected_status':status,
        'selected_item_type':item_type
    }

    return render(request,'items.html',context)