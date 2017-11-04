from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.views.generic import FormView
from django.utils.encoding import smart_str
from wsgiref.util import FileWrapper

from .forms import LandingForm


class LandingView(FormView):
    template_name = "index.html"
    form_class = LandingForm
    success_url = reverse('view_landing') 

    def get_context_data(self, **kwargs):
        context = super(LandingView, self).get_context_data(**kwargs)
        translation.activate('uk')
        return context

    def form_invalid(self, form):
        print(self.request.POST)
        response = super(LandingView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        print(self.request.POST)
        response = super(LandingView, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'download_url': reverse('download_view') 
            }
            form.save()
            form.send_email()
            return JsonResponse(data)
        else:
            return response


def download_view(request):
    file_path = settings.STATIC_ROOT+'/file.pdf'
    wrapper = FileWrapper(file(file_path))
    response = HttpResponse(wrapper, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=file.pdf'
    response['X-Sendfile'] = smart_str(file_path)
    return response