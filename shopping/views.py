from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
 
# def index(request):
#     return render(request,"index.html")
 


def signup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)    
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return render(request,'index.html')
        else:
            return render(request, 'signup.html')
    return render(request, 'signup.html')
                            
