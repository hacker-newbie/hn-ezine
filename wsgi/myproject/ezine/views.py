from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Hnezine

def ezine_list(request):
    hnezines = Hnezine.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'ezine/ezine_list.html', {'hnezines': hnezines})

def ezine_detail(request, pk):
    hnezine = get_object_or_404(Hnezine, pk=pk)
    return render(request, 'ezine/ezine_detail.html', {'hnezine': hnezine})
