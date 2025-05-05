from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Room,Furniture
import cv2
import numpy as np

def get_wall_mask_simple(image_path):
    # Load the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect edges using Canny edge detector
    edges = cv2.Canny(blurred, 50, 150)

    return edges

def change_wall_color_simple(image_path, mask, new_color=(0, 255, 0)):
    image = cv2.imread(image_path)

    # Apply the color change to the regions identified by the edge mask
    image[mask != 0] = new_color  # Change only the detected edges

    # Save and show the modified image
    modified_image_path = 'modified_room_image_simple.jpg'
    # cv2.imwrite(modified_image_path, image)
    # cv2.imshow('Modified Room', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return modified_image_path  # Return the image path


mask = get_wall_mask_simple("room31.jpg")
print(mask)
# Create your views here.

def home(request):
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
    furniture_list = Furniture.objects.all()
    print(furniture_list.first().model_file)
    return render(request,"decor2.html",{"image":image,"furniture_list":furniture_list})