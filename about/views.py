from django.shortcuts import render, get_object_or_404
from django.contrib.flatpages.models import FlatPage

def about_me(request):
    return render(request, 'abouut/about_me.html')

def flatpage_by_id(request, id):
    flatpage = get_object_or_404(FlatPage, id=id)
    return render(request, 'flatpages/flatpage_detail.html', {'flatpage': flatpage})
