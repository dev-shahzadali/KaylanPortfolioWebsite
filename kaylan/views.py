from django.shortcuts import render,  get_object_or_404, redirect
from category.models import Category
from projects.models import Project, ProjectGallery
from user.models import Profile
from django.core.mail import send_mail
from django.contrib import messages

def home(request, category_slug=None):
    categories  = None
    projects    = None
    profile     = None

    profile     = Profile.objects.get()

    if category_slug != None:
        categories      = get_object_or_404(Category, slug=category_slug)
        projects        = Project.objects.filter(category=categories)
    
    else:
        projects        = Project.objects.all().order_by('-created_date')[:3]

    context = {
        'projects'      : projects,
        'profile'       : profile
    }
    return render(request, 'home.html', context)

def contact(request):
    try:
        profile         = Profile.objects.get()

    except(Project.DoesNotExist):
        profile         = None

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }
        message = '''
        From: {}
        Name: {}
        Message: {}
        '''.format(data['email'], data['name'], data['message'])
        send_mail(data['subject'], message, '', ['kaylan24484@gmail.com'])
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')

    context = {
        'profile': profile,
    }
    return render(request, 'contact.html', context)