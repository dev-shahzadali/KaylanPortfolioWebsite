from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from category.models import Category
from .models import Project, ProjectGallery
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def projects(request, category_slug=None):
    categories = None
    projects   = None

    if category_slug != None:
        categories      = get_object_or_404(Category, slug=category_slug)
        projects        = Project.objects.filter(category=categories)
        paginator       = Paginator(projects, 4)
        page            = request.GET.get('page')
        paged_projects  = paginator.get_page(page)
        project_count   = projects.count()
    else:
        projects        = Project.objects.all().order_by('id')
        paginator       = Paginator(projects, 4)
        page            = request.GET.get('page')
        paged_projects  = paginator.get_page(page)
        project_count   = projects.count()

    context = {
        'projects'      : paged_projects,
        'project_count' : project_count,
    }
    return render(request, 'projects.html', context)


def project_detail(request, category_slug, project_slug):
    try:
        single_project      = Project.objects.get(category__slug=category_slug, slug=project_slug)
        project_gallery     = ProjectGallery.objects.filter(project__slug=project_slug)

    except Exception as e:
        raise e

    context= {
        'single_project'    : single_project,
        'project_gallery'   : project_gallery,
    }
    return render(request, 'project_details.html', context)