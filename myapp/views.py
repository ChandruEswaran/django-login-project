from django.shortcuts import render, redirect
from .forms import ApplicationForm
from .models import Application
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse   

def form_page(request):
    # You can reuse app_form.html or create a new template
    return render(request, "app_form.html")

def app_form_view(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_data')  # go to the display page
    else:
        form = ApplicationForm()
    return render(request, 'app_form.html', {'form': form})

def show_data_view(request):
    applications = Application.objects.all()
    return render(request, 'show_data.html', {'applications': applications})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Hardcoded check
        if username == "Admin" and password == "Admin@connect123":
            return redirect("form_page")  # Go to your form page
        else:
            messages.error(request, "❌ Invalid username or password! Please try again.")
            return redirect("login")

    return render(request, "login.html")  # show login page by default

def app_form(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_data')  # Redirect to the show data page
    else:
        form = ApplicationForm()
    return render(request, 'app_form.html', {'form': form})