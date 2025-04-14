from rest_framework.response import Response
from rest_framework.decorators import api_view

from tasks.models import Task
from .serializer import TaskSerializer

@api_view(['GET'])
def tasks(request):

    all_tasks = Task.objects.filter(is_deleted=False)

    serializer = TaskSerializer(all_tasks, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def create_task(request):

    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        response_data = {
            'status' : 2200,
            "message": "Task created successfully",
            "task": serializer.data
        }
        return Response(response_data)
    else:
        response_data = {
            'status' : 2404,
            "message": "Validation Error",
            "errors": serializer.errors
        }
        return Response(response_data)


@api_view(['POST'])
def update_task(request, pk):

    if Task.objects.filter(pk=pk).exists():

        task = Task.objects.get(pk=pk)

        serializer = TaskSerializer(instance=task,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()

            response_data = {
                'status' : 2200,
                "message": "Task Updated successfully",
                "task": serializer.data
            }
            return Response(response_data)
        else:
            response_data = {
                'status' : 2404,
                "message": "Validation Error",
                "errors": serializer.errors
            }
            return Response(response_data)
    else:
        response_data = {
            'status' : 2404,
            "message": "Task not found",
        }
        return Response(response_data)
    
@api_view(['POST'])
def delete_task(request, pk):

    if Task.objects.filter(pk=pk).exists():

        task = Task.objects.get(pk=pk)

        serializer = TaskSerializer(instance=task,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()

            response_data = {
                'status' : 2200,
                "message": "Task Updated successfully",
                "task": serializer.data
            }
            return Response(response_data)
        else:
            response_data = {
                'status' : 2404,
                "message": "Validation Error",
                "errors": serializer.errors
            }
            return Response(response_data)
    else:
        response_data = {
            'status' : 2404,
            "message": "Task not found",
        }
        return Response(response_data)