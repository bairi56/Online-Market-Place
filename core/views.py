from django.shortcuts import render,redirect

# Create your views here.
from item.models import Category,Item
from .forms import SignupForm
def index(request):
    items=Item.objects.filter(is_sold=False)[0:6]
    print(items)
    categories=Category.objects.all()
    return render(request,'core/index.html',
                  {
                    'categories' :categories,
                     'items':items,
                  })

def contact(request):
    return render(request,'core/contact.html')

def signup(request):
    # form=SignupForm()
    if request.method == 'POST':
        form=SignupForm(request.POST)
        # print(form)
        if form.is_valid():
            print("jeo")
            form.save()
            return redirect('/login/')
       
    else:
        form=SignupForm()

    return render(request,'core/signup.html',{
        'form':form
    })