from django.shortcuts import render, get_object_or_404
from branches.models import Branch

# Create your views here.
def branches_list_view(request):
    branches = Branch.objects.all()
    return render(request, 'branches/branches_list.html', {'branches':branches})


def branch_view(request, name):
    branch = get_object_or_404(Branch, name=name)
    posts = branch.post_set.all()
    return render(request, 'branches/branch.html', {'posts': posts,'branch': branch})
