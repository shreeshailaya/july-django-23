from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogContent
from .forms import TestFormClass, ModelsDemoForm
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'index.html')

def dummy(request):
    return HttpResponse("This is dummy page ")

def allBlogs(request):
    obj = BlogContent.objects.all()
    context = {"all_blogs": obj}
    return render(request, 'pages/blogs.html',context)

@login_required(login_url="/admin/")
def addBlogPage(request):
    return render(request, 'pages/add_blog.html')

def addBlogHandler(request):
    if request.GET.get('title') :
        title_r = request.GET.get('title')
        description_r = request.GET.get('description')
        author_r = request.user
        no_of_lines_r = request.GET.get('no_of_lines')

        obj = BlogContent(title=title_r, description = description_r,
                        author = author_r, no_of_line = no_of_lines_r
                        )
        obj.save()
        return render(request, "pages/add_blog.html", {"response":"Blog Saved Successfully"})
    else:
        return render(request, "pages/add_blog.html", {"response":"Please fill form"})

@login_required(login_url="/admin/") 
def deleteBlogByID(request):
    id1 = request.GET.get('id')
    BlogContent.objects.get(pk=id1).delete()
    context = {"response": f"id {id1} deleted successfully"}
    return render(request, "pages/add_blog.html", context)

def djangoFormsDemo(request):
    form = TestFormClass()
    return render(request, "pages/django_form.html", {"form":form})

def modelDjangoForm(request):
    success = ""
    form = ModelsDemoForm(request.POST, request.FILES)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        print(request.user)
        obj.save()
        success = "data saved successfully"

    context = {'form': form, 'success':success}
    return render(request, 'pages/model_form.html', context)

@login_required(login_url="/admin/")
def deleteById(request, id):
    obj = BlogContent.objects.get(id=id)
    if obj.author == request.user:
        BlogContent.objects.get(pk= id).delete()
        success = 'Successfully deleted the blog'
    else:
        success = f"You cannot delete this blog author is {obj.author}"
    return render(request, 'pages/blogs.html', {'success':success})

@login_required(login_url="/admin/")
def updateBlog(request, id):
    obj = BlogContent.objects.get(id = id)
    if obj.author == request.user:
        pass
    else:
        return HttpResponse("You Cannot edit this")
    return render(request, 'pages/update_view.html', {"data":obj})

@login_required(login_url="/admin/")
def updateData(request,id):
    success = ''
    c_id = id
    c_title = request.POST.get('title')
    c_author = request.user
    c_description = request.POST.get('description')
    c_no_of_line = request.POST.get('no_of_line')

    obj = get_object_or_404(BlogContent, id = c_id)
    obj.title = c_title
    obj.author = c_author
    obj.description = c_description
    obj.no_of_line = c_no_of_line
    obj.save()
    success = f"{c_id} - Data updated successfully"
    return render(request, 'pages/blogs.html', {"success":success})

class BlogCreate(CreateView):
    model = BlogContent
    fields = "__all__"

