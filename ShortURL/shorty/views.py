from django.shortcuts import render, redirect, get_object_or_404

from .models import URL
from .forms import URLForm
from django.views.generic import DetailView, DeleteView
from .tasks import timer


class ShortyDetailView(DetailView):
    model = URL
    template_name = 'shorty/details_view.html'
    context_object_name = 'shortylink'

class ShortyDeleteView(DeleteView):
    model = URL
    template_name = 'shorty/shortlink-delete.html'
    success_url = '/'

def shorty_home(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('shortlink')

    form = URLForm()

    data = {
        'form': form
    }

    return render(request, 'shorty/shortlink.html', data)

def shortlink(request):

    url_hash = URL.objects.order_by('id')

    data = {
        'title': 'Ваши ссылки',
        'URL': url_hash
    }
    return render(request, 'shorty/shorty_home.html', data)

def root(request, url_hash):
    url = get_object_or_404(URL, url_hash=url_hash)
    url.clicked()

    return redirect(url.full_url)

def shutdown(request, pk):
    time = request.POST.get("forma")
    if time != None:
        timer(int(time), pk)
        return redirect('/')

    return render(request, 'shorty/timer.html')

class ShutdownDeleteView(DeleteView):
    model = URL
    template_name = 'shorty/shutdown.html'
    success_url = '/'

