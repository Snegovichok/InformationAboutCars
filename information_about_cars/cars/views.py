from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Car, Comment
from .forms import CarForm, CommentForm
from .serializers import CarSerializer, CommentSerializer

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CarListCreateAPIView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CarRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CommentListCreateAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, car_id):
        car = Car.objects.get(id=car_id)
        comments = car.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, car_id):
        car = Car.objects.get(id=car_id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(car=car, author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def information_about_cars(request):
    cars = Car.objects.all()
    return render(request, 'information_about_cars.html', {'cars': cars})

@login_required
def admin_panel(request):
    return render(request, 'admin.html')

def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Пароли не совпадают!')
            return render(request, 'cars/registration.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Такой логин занят!')
            return render(request, 'cars/registration.html')

        User.objects.create_user(username=username, password=password)
        messages.success(request, 'Вы успешно зарегистрировались!')
        return redirect('information_about_cars')

    return render(request, 'cars/registration.html')

def authorization(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Вы успешно вошли в систему!')
            return redirect('information_about_cars')
        else:
            messages.error(request, 'Вы неправильно ввели логин или пароль!')

    return render(request, 'cars/authorization.html')

def user_logout(request):
    logout(request)
    return redirect('information_about_cars')

@login_required
def user_dashboard(request):
    user_cars = Car.objects.filter(owner=request.user)
    return render(request, 'cars/user.html', {'user_cars': user_cars})

@login_required
def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user
            car.save()
            return redirect('user_dashboard')
    else:
        form = CarForm()
    return render(request, 'cars/create_car.html', {'form': form})

@login_required
def edit_car(request, car_id):
    car = get_object_or_404(Car, id=car_id, owner=request.user)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('user_dashboard')
    else:
        form = CarForm(instance=car)
    return render(request, 'cars/edit_car.html', {'form': form, 'car': car})

@login_required
def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id, owner=request.user)
    car.delete()
    return redirect('user_dashboard')

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    comments = car.comments.all()

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.car = car
                comment.author = request.user
                comment.save()
                return redirect('car_detail', car_id=car.id)
        else:
            return redirect('authorization')
    else:
        form = CommentForm()

    return render(request, 'cars/car_detail.html', {'car': car, 'comments': comments, 'form': form})
