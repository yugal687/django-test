from django.shortcuts import render
from todo.serializers import TodoSerializer 
# from rest_framework import viewsets, response, generics
# from rest_framework.decorators import api_view     
from .models import Todo         
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status        
from rest_framework.decorators import api_view



# class TodoView(generics.ListCreateAPIView):  
    # serializer_class = TodoSerializer   
    # queryset = Todo.objects.all()


    # def get(self, request, id = None):
    #     todos = Todo.objects.all()
    #     serializer = TodoSerializer(todos, many=True)
    #     return Response({'data': serializer.data}, status=200)


@api_view(['GET','POST'])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializers = TodoSerializer(todos,many=True)
        return Response({'data': serializers.data, 'status': status.HTTP_200_OK})

    elif(request.method == 'POST'):
        serializers = TodoSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)






# @api_view(['GET', 'POST'])
# def todo_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         todos = Todo.objects.all()
#         serializer = TodoSerializer(todos, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    


 