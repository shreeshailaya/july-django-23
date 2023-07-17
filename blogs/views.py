from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogContent
from .forms import TestFormClass, ModelsDemoForm
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dummy(request):
    return HttpResponse("This is dummy page ")

def allBlogs(request):
    obj = BlogContent.objects.all()
    context = {"all_blogs": obj}
    return render(request, 'pages/blogs.html',context)

def addBlogPage(request):
    return render(request, 'pages/add_blog.html')

def addBlogHandler(request):
    if request.GET.get('title') :
        title_r = request.GET.get('title')
        description_r = request.GET.get('description')
        author_r = request.GET.get('author')
        no_of_lines_r = request.GET.get('no_of_lines')

        obj = BlogContent(title=title_r, description = description_r,
                        author = author_r, no_of_line = no_of_lines_r
                        )
        obj.save()
        return render(request, "pages/add_blog.html", {"response":"Blog Saved Successfully"})
    else:
        return render(request, "pages/add_blog.html", {"response":"Please fill form"})
    
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
    form = ModelsDemoForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        success = "data saved successfully"

    context = {'form': form, 'success':success}
    return render(request, 'pages/model_form.html', context)

def deleteById(request, id):
    BlogContent.objects.get(pk= id).delete()
    success = 'Successfully deleted the blog'
    return render(request, 'pages/blogs.html', {'success':success})

def updateBlog(request, id):
    obj = BlogContent.objects.get(id = id)
    return render(request, 'pages/update_view.html', {"data":obj})

def updateData(request,id):
    success = ''
    c_id = id
    c_title = request.POST.get('title')
    c_author = request.POST.get('author')
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

