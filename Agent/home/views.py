from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import TeacherRegistrationForm, CustomerRegistrationForm, LoginForm
from .models import Teacher, Customer, Rating


def teacher_signup(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_login')
    else:
        form = TeacherRegistrationForm()
    
    return render(request, 'teacher_signup.html', {'form': form})


def customer_signup(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_login')
    else:
        form = CustomerRegistrationForm()
    
    return render(request, 'customer_signup.html', {'form': form})


def teacher_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            phone_number = form.cleaned_data['phone_number']
            try:
                teacher = Teacher.objects.get(full_name=full_name, phone_number=phone_number)
                return redirect('teacher_profile', teacher.id)
            except Teacher.DoesNotExist:
                pass

    form = LoginForm()
    return render(request, 'teacher_login.html', {'form': form})


def customer_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            phone_number = form.cleaned_data['phone_number']
            try:
                customer = Customer.objects.get(full_name=full_name, phone_number=phone_number)
                return redirect('customer_profile', customer.id)
            except Customer.DoesNotExist:
                pass

    form = LoginForm()
    return render(request, 'customer_login.html', {'form': form})


def home(request):
    teachers = Teacher.objects.all()
    return render(request, 'home.html', {'teachers': teachers})

def intro(request):
    return render(request,'intro.html')

def about(request):
    return render(request,'about.html')

def teacher_profile(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    ratings = Rating.objects.filter(teacher=teacher)
    return render(request, 'teacher_profile.html', {'teacher': teacher, 'ratings': ratings})


def customer_profile(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    return render(request, 'customer_profile.html', {'customer': customer})


def rate_teacher(request, teacher_id):
    if request.method == 'POST':
        teacher = Teacher.objects.get(id=teacher_id)
        customer = Customer.objects.get(id=request.POST['customer_id'])
        comment = request.POST['comment']
        rating = int(request.POST['rating'])

        Rating.objects.create(teacher=teacher, customer=customer, comment=comment, rating=rating)
        return redirect('teacher_profile', teacher_id)


def comment_teacher(request, teacher_id):
    if request.method == 'POST':
        teacher = Teacher.objects.get(id=teacher_id)
        customer = Customer.objects.get(id=request.POST['customer_id'])
        comment = request.POST['comment']

        Rating.objects.create(teacher=teacher, customer=customer, comment=comment)
        return redirect('teacher_profile', teacher_id)