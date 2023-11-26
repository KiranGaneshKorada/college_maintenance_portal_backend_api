from django.shortcuts import render
from django.http import JsonResponse
from .models import Issue
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET'])
def get_issue_status_graph_data(request):
    total_issues = Issue.objects.all().count()
    solved_issues = Issue.objects.filter(status="completed").count()
    under_process_issues = Issue.objects.filter(status="under process").count()
    
    return JsonResponse({
        "total_issues": total_issues,
        "solved_issues": solved_issues, "under_process_issues": under_process_issues
        })
