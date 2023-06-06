from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http.response import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Cars

#Login
def login_view(request):
 if request.method =="POST":
    username= request.POST["username"]
    password=request.POST["password"]

    user = authenticate(request,username=username ,password=password)
    
    if user:
        login(request,user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render (request,"CarApp/login.html", { 
            "message":"Invalid Credentials"})
 return render (request,"CarApp/login.html")


def allDisplayItems(request):
   return render(request,"CarApp/displayAll.html", {"cars": Cars.objects.all()})
    


def displaySpecificItem(request, carid):
   if request.method=="POST":
      car= Cars.objects.get(pk=carid)
      user = request.user
      car.customer.add(user)  
      return HttpResponseRedirect(reverse("home"))     
   return render(request,"CarApp/specificItem.html", {"car": Cars.objects.get(id=carid)})
    


def signup_view(request):
    if request.method =="POST":
        Username= request.POST["username"]
        password= request.POST["password"]
        email = request.POST["email"]
        try:
            user = User.objects.get(username=Username)
        except: 
            user = User.objects.create_user(username=Username, password=password, email=email)
            return render (request,"CarApp/login.html")
        else:
           return render (request,"CarApp/signup.html", { 
                "message":"Username is already taken. Please try another."})  
    return render (request,"CarApp/signup.html")


def displayUserOrders(request):
   user = request.user                        
   return render(request,"CarApp/orders.html", {"cars": user.cars.all()})




def updateCar(request, carid):
    car = Cars.objects.get(id=carid)
    
    if request.method == "POST":
        car.Model=request.POST["Model"]
        try:
            car.price =float( request.POST["price"])
        except:
            error_message = "Please enter a valid price."
            return render(request, "CarApp/updatecar.html", {"car": car, "error_message": error_message})
        car.type = request.POST["type"]
        car.Cname = request.POST["Cname"]
        car.ModelYear =request.POST["ModelYear"]
        car.colour =request.POST["colour"]
        car.engineType=request.POST["engineType"]
        car.save()
        return HttpResponseRedirect(reverse("home"))
        
    return render(request, "CarApp/updatecar.html", {"car": car})



def delete(request, carid):
    car = Cars.objects.get(id=carid)
    car.delete()
    return HttpResponseRedirect(reverse("home"))
    
   


        