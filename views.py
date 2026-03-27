from django.shortcuts import render, redirect, HttpResponse
from .forms import item

# Create your views here.

def home(request):
    form = item()

    if "tasks" not in request.session:
        request.session["tasks"] = []
    if request.method == "POST":
        form = item(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            task = task.capitalize()
            request.session["tasks"] += [task]

            return redirect("todo:home")
        else:
            return  HttpResponse("Something went wrong")
        
    
    return render(request, "todo/home.html", {"form":form, "tasks":request.session["tasks"]})
