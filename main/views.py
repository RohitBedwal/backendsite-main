from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


from functools import wraps

def log_view_call(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        print(f"[LOG] View function '{{}}' called with method: {{}}".format(view_func.__name__, request.method))
        return view_func(request, *args, **kwargs)
    return wrapper


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html', {'name': 'BACK'})
@login_required(login_url='login')
def about(request):
     return render(request, 'about.html', {'name': 'BACK'})

@login_required(login_url='login')
def services(request):
    return render(request, 'services.html', {'name': 'BACK'})




@log_view_call
def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        query = request.POST.get('query')

        # Save contact form to database
        Contact.objects.create(name=name, phone=phone, email=email, query=query)

        return redirect('response_taken')  # Redirect after submission

    return render(request, 'contact.html', {'name': 'BACK'})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        query = request.POST.get('query')

        # Create and save a new Contact object
        Contact.objects.create(name=name, phone=phone, email=email, query=query)

        return redirect('contact')  # Redirect to contact page or success page after submission
    
    return render(request, 'response_taken.html')




def response_taken_view(request):
    return render(request, 'response_taken.html')


from django.views import View

from functools import wraps

def log_view_call(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        print(f"[LOG] View function '{{}}' called with method: {{}}".format(view_func.__name__, request.method))
        return view_func(request, *args, **kwargs)
    return wrapper

from django.shortcuts import render
from django.http import HttpResponse
from .models import Subscriber

class SubscribeView(View):
    def get(self, request):
        subscribers = Subscriber.objects.all()  # fetch all subscribers from DB
        return render(request, 'subscribe.html', {'subscribers': subscribers})
    
    def post(self, request):
        email = request.POST.get('email')
        Subscriber.objects.create(email=email)
        return HttpResponse("Subscription successful!")







def contact_crud_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        query = request.POST.get('query')
        Contact.objects.create(name=name, email=email, phone=phone, query=query)
        return redirect('contact_crud')

    contacts = Contact.objects.all().order_by('-submitted_at')
    return render(request, 'contact.html', {'contacts': contacts})


def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == 'POST':
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.phone = request.POST.get('phone')
        contact.query = request.POST.get('query')
        contact.save()
        return redirect('contact_crud')
    return render(request, 'edit_contact.html', {'contact': contact})


def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    return redirect('contact_crud')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Change to your homepage URL name
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout