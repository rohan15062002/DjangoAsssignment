from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

# Create your views here.


def get_post(id):
    try:
        return Post.objects.get(id=id)
    except Post.DoesNotExist:
        return None


@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "Detail View": "/detail/<int:id>",
        "Create": "/create/",
        "Update": "/update/<int:id>",
        "Delete": "/delete/<int:id>",
        "For accessing all posts": request.build_absolute_uri(f"/posts/"),
        "For creating a post": request.build_absolute_uri(f"/create/"),
    }
    return Response(api_urls)


@api_view(["GET", "POST"])
def blogListView(request):

    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
def blogDetailsView(request, id):
    post = get_post(id)
    if post is None:
        return Response({"Error": "Post with this Id doesn't exists"})
    elif request.method == "GET":
        serializer = PostSerializer(post, many=False)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(instance=post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == "DELETE":
        post.delete()
        return Response("Post is deleted successfully")


# creating seperate endpoints for each method


@api_view(["POST"])
def postCreate(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(["GET"])
def postDetail(request, id):
    post = get_post(id)
    if post is None:
        return Response({"Error": "Post with this Id doesn't exists"})

    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)


@api_view(["GET", "PUT"])
def postUpdate(request, id):
    post = get_post(id)
    if post is None:
        return Response({"Error": "Post with this Id doesn't exists"})

    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = PostSerializer(instance=post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


@api_view(["GET", "DELETE"])
def postDelete(request, id):
    post = get_post(id)
    if post is None:
        return Response({"Error": "Post with this Id doesn't exists"})
    if request.method == "GET":
        serializer = PostSerializer(post, many=False)
        return Response(serializer.data)
    post.delete()
    return Response("Post is deleted successfully")
