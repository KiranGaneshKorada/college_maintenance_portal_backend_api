from django.shortcuts import render
from django.http import JsonResponse
from .models import Complaint
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET'])
def get_issue_status_graph_data(request):
    category_filter = request.query_params.get("category")
    time_range_filter = request.query_params.get("time_range")

    if (not time_range_filter):

        if not category_filter:
            total_issues = Complaint.objects.all().count()
            solved_issues = Complaint.objects.filter(
                status="completed").count()
        else:
            total_issues = Complaint.objects.filter(
                category=category_filter).count()
            solved_issues = Complaint.objects.filter(
                status="completed", category=category_filter).count()

    else:
        if not category_filter:
            total_issues = Complaint.objects.filter(date_created__gte=time_range_filter).count()
            solved_issues = Complaint.objects.filter(
                status="completed", date_created__gte=time_range_filter).count()
        else:
            total_issues = Complaint.objects.filter(
                category=category_filter, date_created__gte=time_range_filter).count()
            solved_issues = Complaint.objects.filter(
                status="completed", category=category_filter, date_created__gte=time_range_filter).count()

    # total_issues = Complaint.objects.all().count()
    # solved_issues = Complaint.objects.filter(status="completed").count()

    return JsonResponse({"Data": [
        {"issue_type": "Total Issues", "issues": total_issues},
        {"issue_type": "Solved Issues", "issues": solved_issues},
        {"issue_type": "Under Progress Issues",
            "issues": total_issues-solved_issues}
    ]})
