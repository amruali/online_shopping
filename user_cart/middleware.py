



from django.http import HttpResponsePermanentRedirect

class CustomTrailingSlashMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.endswith('/') and not request.path_info.endswith('/'):
            return HttpResponsePermanentRedirect(request.path_info + '/')
        response = self.get_response(request)
        return response