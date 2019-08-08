from django.shortcuts import render,
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', {'error': 'Username is take'})
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, 'register.html', {'error': 'Email already exists'})
                else:
                    user = User.objects.create_user (
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name
                    )
                    user.save()
                    return redirect('login')
        else:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
    
    else:
        return render(request, 'register.html')




