from django.shortcuts import render
from todo.serializers import TodoSerializer 
from .models import Todo         
from rest_framework.response import Response
from rest_framework import status        
from rest_framework.decorators import api_view


@api_view(['GET','POST','PUT','DELETE'])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializers = TodoSerializer(todos,many=True)
        return Response({'data': serializers.data, 'status': status.HTTP_200_OK, 'message': 'Successfully Fetched'})


    elif(request.method == 'POST'):
        serializers = TodoSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def todo_detail(request, pk):
    try:
        todos = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response(status=404)
  
    if request.method == 'GET':
        serializer = TodoSerializer(todos)
        return Response(serializer.data)
  
    # elif request.method == 'PUT':
    #     data = JSONParser().parse(request)
    #     serializer = TodoSerializer(todos, data=data)
  
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=400)
  
    elif request.method == 'DELETE':
        todos.delete()
        return Response({'status':204, 'message': 'successfully deleted'})







    # elif(request.method == 'PUT'):
    #     todo = Todo.objects.get(id=request.data['id'])
    #     serializers = TodoSerializer(instance=todo,data=request.data)
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response(serializers.data,status=status.HTTP_201_CREATED)
    #     return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    # elif(request.method == 'DELETE'):
    #     todo = Todo.objects.get(id=request.data['id'])
    #     todo.delete()
    #     return Response({'message': 'success'},status=status.HTTP_200_OK)


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

    


 