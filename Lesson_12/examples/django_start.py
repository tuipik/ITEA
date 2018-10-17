from django.conf.urls import url
from django.conf import settings
from django.http import HttpResponse

settings.configure(
    ROOT_URLCONF = __name__,
    DEBUG = True
)

from pprint import pprint



def index(request):
    out = ['{}: {}'.format(k, v)
           for k, v in sorted(request.META.items())
           if k.startswith('HTTP_')]
    html = '<br>'.join(out)
    html += '<br>Method: ' + request.method
    return HttpResponse(html, content_type='text/html')

urlpatterns = [
    url('^$', index)
]

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    import sys
    execute_from_command_line(sys.argv)
