from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, EnrollmentForm, InterventionForm
from .models import Enrollment, Intervention
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EnrollmentSerializer


# Create your views here.

def home(request):
    enrollments = Enrollment.objects.all()

    # find out if logging in
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        #Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully Logged In!")
            return redirect('home')
        else:
            messages.success(request, "Username or password is incorrect, please try again!")
            return redirect('home')
    else:
        return render(request, 'home.html', {'enrollments': enrollments})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
			# Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})
    

def reports(request):
    return render(request, 'reports.html')

@login_required
def add_enrollment(request):
    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.user = request.user
            enrollment.save()
            return redirect('enrollment_list')
        
    else:
        form = EnrollmentForm(initial={'user': request.user})
    return render(request, 'add_enrollment.html', {'form': form})

@login_required
def add_intervention(request, enrollment_id):
    enrollment = get_object_or_404(Enrollment, id=enrollment_id)
    interventions = Intervention.objects.filter(enrollment=enrollment)
    if request.method == "POST":
        form = InterventionForm(request.POST)
        if form.is_valid():
            intervention = form.save()
            intervention.updated_by = request.user
            intervention.enrollment = enrollment
            intervention.save()

            return redirect('ayp_interventions')
        
    else: 
        form = InterventionForm(initial={'enrollment': enrollment})
    return render(request, 'add_intervention.html', {'form' : form, 'interventions':interventions })

@login_required
def ayp_enrollment_record(request, enrollment_id):
    if request.user.is_authenticated:
        # find the ayp record
        ayp_enrollment_record = Enrollment.objects.get(id=enrollment_id)
        return render(request, 'enrollment_record.html', {'ayp_enrollment_record' : ayp_enrollment_record})
    else:
        messages.success(request, "You must be logged in first to view that page!")
        return redirect('home')

@login_required
def delete_ayp_enrollment_record(request, enrollment_id):
    if request.user.is_authenticated:
        delete_it = Enrollment.objects.get(id=enrollment_id)
        delete_it.delete()
        messages.success(request, "AYP Record deleted successfully!")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in first to perform this action!")
        return redirect('home')


@login_required
def update_ayp_enrollment_record(request, enrollment_id):
    if request.user.is_authenticated:
        current_record = Enrollment.objects.get(id=enrollment_id)
        form = EnrollmentForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully!")
            return redirect('home')
        return render(request, 'update_ayp_enrollment_record.html', {'form' : form})
    else:
        messages.success(request, "You must be logged in first to perform this action!")
        return redirect('home')

# API Views
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'enrollment_list': '/enrollment_list/',
        'create_enrollment': '/enrollments/add/',
    }
    return Response(api_urls)

@api_view(['GET'])
def enrollmentList(request):
    enrollments = Enrollment.objects.all()
    serializer = EnrollmentSerializer(enrollments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def enrollmentDetail(request, enrollment_id):
    enrollment = Enrollment.objects.get(id=enrollment_id)
    serializer = EnrollmentSerializer(enrollment, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def enrollmentCreate(request):
    serializer = EnrollmentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def enrollmentUpdate(request, enrollment_id):
    enrollment = Enrollment.objects.get(id=enrollment_id)
    serializer = EnrollmentSerializer(instance=enrollment, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def enrollmentDelete(request, enrollment_id):
    enrollment = Enrollment.objects.get(id=enrollment_id)
    enrollment.delete()

    return Response("AYP successfully deleted!")

@login_required
def ayp_interventions(request):
    query = request.GET.get('q', '')
    enrollment = None
    interventions = []

    if query:
        try:
            enrollment = Enrollment.objects.get(id=query)
            interventions = enrollment.interventions.all()
        except Enrollment.DoesNotExist:
            enrollment = None

    return render(request, 'ayp_interventions.html', {
        'enrollment':enrollment,
        'interventions': interventions,
        'query': query,
    })
