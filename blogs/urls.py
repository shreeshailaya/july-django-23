from django.urls import path
from . import views
from blogs.views import BlogCreate

urlpatterns = [
    path('', views.index, name='index'),
    path('dummy/', views.dummy, name='dummy'),
    path('blogs/', views.allBlogs, name='blogs'),
    path('add-blog/', views.addBlogPage, name='add_blog_page'),
    path('add-blog/add_blog_handler', views.addBlogHandler, name='abh'),
    path('add-blog/delete_blog', views.deleteBlogByID, name="deleteblogbyid"),
    path("django-form", views.djangoFormsDemo, name="django_forms" ),
    path('model_form', views.modelDjangoForm, name='model_form'),
    path('delete/<id>', views.deleteById, name='delete-by-id'),
    path('update/<id>', views.updateBlog, name="update_blog"),
    path('update_data/<id>', views.updateData, name='update-data'),
    path('class-based-create', BlogCreate.as_view())
]
'''
1. create html file for adding blogs(add form)
2. create view for calling the created html form
3. register url
4. add action URL 
5. add view for action url (HTTPResponse)
6. register url 
'''