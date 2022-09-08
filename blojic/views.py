from django.shortcuts import render

def post_list(request):
    return render(request, 'blojic/post_list.html', {})