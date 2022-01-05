import json
from django.http import HttpResponse
from .models import Candidate, Scores

# Create your views here.


def create_candidate(request):
    """A view to create candidates from JSON"""
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    if Candidate.objects.filter(candidate_ref=body['candidate_ref']).exists():
        Candidate.object.create(
            name=body['name'],
            candidate_ref=body['candidate_ref']
        )
        return HttpResponse('<h1>Candidate Uploaded Successfully</h1>')
    else:
        return HttpResponse('<h1>Candidate already exists</h1>')


def create_score(request):
    """A view to add scores to existing candidates"""
    return HttpResponse('<h1>Hello1</h1>')


def get_candidate(request, candidate_ref):
    """A view to show all candidates scores"""
    return HttpResponse('<h1>Hello2</h1>')
