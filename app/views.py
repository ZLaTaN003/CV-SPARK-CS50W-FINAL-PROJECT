from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . models import User,Candidate,UserProfile,Like,Section
from  django.contrib.auth.decorators import login_required
from django import forms
from .models import UserProfile
import requests
import json
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse
from django.template import loader
from xhtml2pdf import pisa
from io import BytesIO
from django.db.models import Count



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'birthdate', 'profile_picture']
        widgets = {
            'profile_picture': forms.FileInput(),  
        }

@login_required(login_url='login')
def create(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        about = request.POST.get('about')
        skills = request.POST.get('skills')
        degree = request.POST.get('degree')
        university = request.POST.get('university')
        experience = request.POST.get('experience')


        candidate = Candidate(
            user=user,
            name=name,
            email=email,
            phone=phone,
            about=about,
            skills=skills,
            degree=degree,
            university=university,
            experience=experience
        )

        candidate.save()
    user_profile = None
    if request.user.is_authenticated:
        user_profile = request.user.userprofile
    return render(request,'app/createresume.html',{
        "user_profile": user_profile,
    })













def login_view(request):
    
    if request.method == "POST":

        
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("profile"))
        else:
            return render(request, "app/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "app/login.html")


def logout_view(request):
    
    logout(request)
    return HttpResponseRedirect(reverse("profile"))


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmation = request.POST.get("confirmation")
        
        if not username or not email or not password or not confirmation:
            return render(request, "app/register.html", {
                "message": "All fields must be filled out."
            })

        if password != confirmation:
            return render(request, "app/register.html", {
                "message": "Passwords don't match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "app/register.html", {
                "message": "Username already exists."
            })

        login(request, user)

        return HttpResponseRedirect(reverse("profile"))
    else:
        return render(request, "app/register.html")



@login_required(login_url='login')
def profile(request):
    if request.user.is_authenticated:
        user_profile = request.user.userprofile

        if request.method == 'POST':
            form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
            if form.is_valid():
                new_profile_picture = form.cleaned_data.get('profile_picture')
                if new_profile_picture:
                    user_profile.profile_picture = new_profile_picture
                user_profile.bio = form.cleaned_data['bio']
                user_profile.birthdate = form.cleaned_data['birthdate']
                user_profile.save()
                return HttpResponseRedirect(reverse("profile"))
        else:
            form = UserProfileForm(instance=user_profile)

        return render(request, "app/profile.html", {"user_profile": user_profile, "form": form})

    else:
        return HttpResponseRedirect(reverse("login"))


@login_required(login_url='login')
def jobfromlink(request):
    if request.user.is_authenticated:
        user_profile = request.user.userprofile

    adzuna_api_key = '35f895d24be16c0e0d1f5918306df65c'
    url = 'https://api.adzuna.com/v1/api/jobs/in/search/1' 
    headers = {'User-Agent': 'YourApp/1.0'}

    params = {
        'app_id': 'e10133ba',
        'app_key': adzuna_api_key,
        'results_per_page': 5,
        
    }

    response = requests.get(url, params=params, headers=headers)
    
    if response.status_code == 200:
        try:
            data = response.json()
            job_list = data.get('results', [])
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {e}")
            job_list = []
    else:
        print(f"Request to Adzuna API failed with status code: {response.status_code}")
        job_list = []

    return render(request, 'app/jobsfromlink.html', {'job_list': job_list,'user_profile': user_profile})


@login_required(login_url='login')
def cv(request,id):
    if request.user.is_authenticated:
        user_profile = request.user.userprofile


    try:
        cv = Candidate.objects.get(pk=id)
    except Candidate.DoesNotExist:
        return  render(request,'app/404.html',{
            'user_profile': user_profile,
        })

    return render(request,'app/cv.html',{
        'cv': cv,
        'user_profile': user_profile,
    })









@login_required(login_url='login')
def cvtopdf(request, id):
    if request.user.is_authenticated:
        user_profile = request.user.userprofile


    
    try:
        cv = Candidate.objects.get(pk=id)
    except Candidate.DoesNotExist:
        return  render(request,'app/404.html',{
            'user_profile': user_profile,
        })

    pdf_buffer = BytesIO()
    template = loader.get_template('app/cv.html')
    context = {'cv': cv, 'user_profile': user_profile,'ispdf': True}
    html = template.render(context)
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), pdf_buffer)

    if  pdf:
        pdf_buffer.seek(0)
        response = HttpResponse(pdf_buffer.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment'
        return response
        

    else:
        return HttpResponse('PDF generation failed')
@login_required(login_url='login')
def list(request):
    if request.user.is_authenticated:
        user_profile = request.user.userprofile


    cvs = Candidate.objects.annotate(like_count=Count('like')).all().order_by('-id')
    
    
    return render(request,'app/listing.html',{'cvs': cvs,'user_profile': user_profile,'theuser': request.user,})



@login_required(login_url='login')
def like_cv(request, cv_id):
    cv = get_object_or_404(Candidate, pk=cv_id)
    user = request.user

    try:
        like = Like.objects.get(user=user, cv=cv)
        like.delete()  
        liked = False
    except Like.DoesNotExist:
        like = Like(user=user, cv=cv)
        like.save()
        liked = True

    data = {'liked': liked, 'like_count': cv.like_set.count()}
    return JsonResponse(data)


@login_required(login_url='login')
def edit(request,id):
    if request.method=='POST':
        cvtodelete = Candidate.objects.get(pk=id)
        cvtodelete.delete()
        return HttpResponseRedirect(reverse('list'))
    

@login_required(login_url='login')
def section_list(request):
    if request.user.is_authenticated:
        user_profile = request.user.userprofile
    sections = Section.objects.all()
    user_sections = request.user.sections.all()
    return render(request, 'app/sectionlist.html', {'sections': sections, 'user_sections': user_sections, 'user_profile':user_profile})

@login_required(login_url='login')
def join_section(request, section_id):
    section = get_object_or_404(Section, pk=section_id)
    request.user.sections.add(section)
    return HttpResponseRedirect(reverse('section_list'))


@login_required(login_url='login')
def leave_section(request, section_id):
    section = get_object_or_404(Section, pk=section_id)
    request.user.sections.remove(section)
    return HttpResponseRedirect(reverse('section_list'))


@login_required(login_url='login')
def section_users(request, section_id):
    if request.user.is_authenticated:
        user_profile = request.user.userprofile
    section = Section.objects.get(pk=section_id)
    users = section.members.all() 

    return render(request, 'app/sectionusers.html', {
        'section': section,
        'users': users,
        'user_profile' : user_profile,
    })