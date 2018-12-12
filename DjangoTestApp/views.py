from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, \
    BasicAuthentication
from django.shortcuts import render, HttpResponse, \
    get_object_or_404, HttpResponseRedirect


from DjangoTestApp.models import *
from posts.models import *

import os
import json
import datetime


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return


def Home(request):

    return render(request, 'DjangoTestApp/home.html')


def CreatePost(request):

    return render(request, 'DjangoTestApp/create_post.html')


def ViewPost(request, post_pk):

    return render(request, 'DjangoTestApp/view_post.html')

def HomeSection(request):
    return render(request, 'DjangoTestApp/home_section.html')

def AboutSection(request):
    return render(request, 'DjangoTestApp/about_section.html')

def PostPageView(request):
    posts = Posts.objects.all()
    return render(request, 'DjangoTestApp/posts.html',{'object_list':posts})



class PublishPostAPI(APIView):

    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)

    def post(self, request, *args, **kwargs):

        response = {}
        response['status'] = 500
        try:

            data = request.data

            title = data['title']
            content = data['content']
            author = data['author']

            custom_user = CustomUser.objects.get(username=author)

            Post.objects.create(title=title,
                                content=content,
                                author=custom_user)

            response['status'] = 200

        except Exception as e:
            print("Error PostContentAPI", str(e))

        return Response(data=response)


class GetPostAPI(APIView):

    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    def get(self,request,*args,**kwargs):
        return render(request, 'DjangoTestApp/view_post.html')

    def post(self, request, *args, **kwargs):

        response = {}
        response['status'] = 500
        try:

            data = request.data

            print("data", data)

            post_pk = data['post_pk']


            post_obj = Post.objects.get(pk=post_pk)

            response['title'] = post_obj.title
            response['content'] = post_obj.content
            response['author'] = post_obj.author.username
            response['status'] = 200

        except Exception as e:
            print("Error GetPostAPI", str(e))

        return Response(data=response)



PublishPost = PublishPostAPI.as_view()

GetPost = GetPostAPI.as_view()
