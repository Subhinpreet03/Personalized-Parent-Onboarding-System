from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Parent, Child, Blog
import json


# Create your views here.
@csrf_exempt
def add_parent(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        parent = Parent()

        parent.father_name = data.get('father_name')
        parent.mother_name = data.get('mother_name')
        parent.email = data.get('email')
        parent.parent_type = data.get('parent_type')

        parent.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Parent added successfully!',
            'parent_id': parent.id
        }, status=201)


@csrf_exempt
def get_parent(request, parent_id):
    if request.method == 'GET':
        parent = Parent.objects.get(id=parent_id)
        return JsonResponse({
            'status': 'success',
            'parent': {
                'id': parent.id,
                'father_name': parent.father_name,
                'mother_name': parent.mother_name,
                'email': parent.email,
                'parent_type': parent.parent_type
            }
        }, status=200)


@csrf_exempt
def update_parent(request, parent_id):
    if request.method == 'PUT' or request.method == 'POST':
        data = json.loads(request.body)
        parent = Parent.objects.get(id=parent_id)
        parent.father_name = data.get('father_name', parent.father_name)
        parent.mother_name = data.get('mother_name', parent.mother_name)
        parent.email = data.get('email', parent.email)
        parent.parent_type = data.get('parent_type', parent.parent_type)
        parent.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Parent updated successfully!',
            'parent_id': parent.id
        }, status=200)


@csrf_exempt
def delete_parent(request, parent_id):
    if request.method == 'DELETE':
        parent = Parent.objects.get(id=parent_id)
        parent.delete()
        return JsonResponse({
            'status': 'success',
            'message': 'Parent deleted successfully!'
        }, status=200)


@csrf_exempt
def add_child(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        child = Child()
        child.name = data.get('name')
        child.age = data.get('age')
        child.gender = data.get('gender')
        child.parent_id = data.get('parent_id')
        child.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Child added successfully!',
            'child_id': child.id
        }, status=201)


@csrf_exempt
def get_child(request, child_id):
    if request.method == 'GET':
        child = Child.objects.get(id=child_id)
        return JsonResponse({
            'status': 'success',
            'child': {
                'id': child.id,
                'name': child.name,
                'age': child.age,
                'gender': child.gender,
                'parent_id': child.parent.id
            }
        }, status=200)


@csrf_exempt
def update_child(request, child_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        child = Child.objects.get(id=child_id)
        child.name = data.get('name', child.name)
        child.age = data.get('age', child.age)
        child.gender = data.get('gender', child.gender)
        child.parent_id = data.get('parent_id', child.parent_id)
        child.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Child updated successfully!',
            'child_id': child.id
        }, status=200)


@csrf_exempt
def delete_child(request, child_id):
    if request.method == 'DELETE':
        child = Child.objects.get(id=child_id)
        child.delete()
        return JsonResponse({
            'status': 'success',
            'message': 'Child deleted successfully!'
        }, status=200)


@csrf_exempt
def add_blog(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        blog = Blog()
        blog.title = data.get('title')
        blog.content = data.get('content')
        blog.age_group = data.get('age_group')
        blog.gender = data.get('gender')
        blog.parent_type = data.get('parent_type')
        blog.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Blog added successfully!',
            'blog_id': blog.id
        }, status=201)


@csrf_exempt
def get_blog(request, blog_id):
    if request.method == 'GET':
        blog = Blog.objects.get(id=blog_id)
        return JsonResponse({
            'status': 'success',
            'blog': {
                'id': blog.id,
                'title': blog.title,
                'content': blog.content,
                'age_group': blog.age_group,
                'gender': blog.gender,
                'parent_type': blog.parent_type
            }
        }, status=200)


@csrf_exempt
def update_blog(request, blog_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        blog = Blog.objects.get(id=blog_id)
        blog.title = data.get('title', blog.title)
        blog.content = data.get('content', blog.content)
        blog.age_group = data.get('age_group', blog.age_group)
        blog.gender = data.get('gender', blog.gender)
        blog.parent_type = data.get('parent_type', blog.parent_type)
        blog.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Blog updated successfully!',
            'blog_id': blog.id
        }, status=200)


@csrf_exempt
def delete_blog(request, blog_id):
    if request.method == 'DELETE':
        blog = Blog.objects.get(id=blog_id)
        blog.delete()
        return JsonResponse({
            'status': 'success',
            'message': 'Blog deleted successfully!'
        }, status=200)


def get_age_group(age):
    if 2 <= age <= 5:
        return '2-5'
    elif 6 <= age <= 8:
        return '6-8'
    elif 9 <= age <= 12:
        return '9-12'
    elif 13 <= age <= 17:
        return '13-17'
    else:
        return '18+'


@csrf_exempt
def home_feed(request, parent_id):
    if request.method == 'GET':

        # Get the parent and associated child
        parent = Parent.objects.get(id=parent_id)
        child = parent.child_set.first()
        child_age = child.age
        age_group = get_age_group(child_age)
        blogs = Blog.objects.filter(age_group=age_group, gender=child.gender)

        blog_list = []
        for blog in blogs:
            blog_list.append({
                'id': blog.id,
                'title': blog.title,
                'content': blog.content,
                'age_group': blog.age_group,
                'gender': blog.gender,
                'parent_type': blog.parent_type
            })

        return JsonResponse({
            'status': 'success',
            'home_feed': blog_list
        }, status=200)


@csrf_exempt
def customize_feed(request, parent_id):
    if request.method == 'POST':

        data = json.loads(request.body)

        parent = Parent.objects.get(id=parent_id)
        child = parent.child_set.first()

        child_age = data.get('age', child.age)
        age_group = get_age_group(child_age)
        gender = data.get('gender', child.gender)
        parent_type = data.get('parent_type', parent.parent_type)

        blogs = Blog.objects.filter(age_group=age_group, gender=gender, parent_type=parent_type)

        blog_list = []
        for blog in blogs:
            blog_list.append({  
                'id': blog.id,
                'title': blog.title,
                'content': blog.content,
                'age_group': blog.age_group,
                'gender': blog.gender,
                'parent_type': blog.parent_type
            })

        return JsonResponse({
            'status': 'success',
            'customized_feed': blog_list
        }, status=200)
