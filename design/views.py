from django.shortcuts import render,redirect
from .models import Room,Furniture
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserFurniture
from .forms import UserFurnitureForm
from django.contrib.auth.decorators import login_required


def home(request):
    bg_img = Room.objects.filter(image = "room/bg.jpg")
    print(bg_img)
    return render(request,'home.html')


def upload(request):
    
    print(request.FILES.get("image"))
    if request.method == "POST" and request.FILES.get("image"):
        print("if")
        uploaded_image = request.FILES["image"]
        room_image = Room.objects.create(image = uploaded_image)
        
        print("uploaded")
    else:
        print("not upload")

    return  redirect(design)




def design(request):
    image = Room.objects.last()
    form = UserFurnitureForm()

    furniture_list = []
    furniture_list += Furniture.objects.all() 
    if request.user.is_authenticated:
        furniture_list += UserFurniture.objects.filter(user=request.user)

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = UserFurnitureForm(request.POST, request.FILES)
            if form.is_valid():
                furniture = form.save(commit=False)
                furniture.user = request.user
                furniture.save()
                return redirect('design')
        else:
            print("Anonymous users cannot upload furniture.")

    return render(request, "decor.html", {
        "image": image,
        "furniture_list": furniture_list,
        "form": form,
    })




def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, 'Account created successfully!')
        return redirect('login')

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            
            # Handle redirect to previous page (next param)
            next_url = request.GET.get('next') or request.POST.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    # GET request — render login form
    return render(request, 'login.html', {
        'next': request.GET.get('next', '')
    })


def logout_view(request):
    logout(request)
    return redirect('login')



