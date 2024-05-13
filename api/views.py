from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import status as api_response_status
from rest_framework.decorators import api_view
from django_q.tasks import async_task

def healthcheck(request):
    return JsonResponse({
        "Message":"OK"
    })

def print_to_console(message):
    print(message)
    print("------------------------------------------------------")

def print_to_console1(message):
    print(message2)
    print("------------------------------------------------------")

def on_task_complete(task):
    print(task)
    print(task.success)
    print(task.result)
    print("======================================================")


@api_view(['GET'])
def upload_file(request):
    print("GIVING IT TO TASK-------------------")

    task_id = async_task(print_to_console, "ASYNC TASK IN PLACE", task_name="test234", hook=on_task_complete)
    print(task_id)

    return JsonResponse({
        'success': True,
        'userMessage': '',
        'data': {},
    }, status = api_response_status.HTTP_200_OK)

@api_view(['GET'])
def upload_file_fail(request):
    print("GIVING IT TO TASK-------------------")

    task_id = async_task(print_to_console1, "ASYNC TASK IN PLACE", task_name="test234", hook=on_task_complete)
    print(task_id)

    return JsonResponse({
        'success': True,
        'userMessage': '',
        'data': {},
    }, status = api_response_status.HTTP_200_OK)

