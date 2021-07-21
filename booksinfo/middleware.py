from django.http import response
import stringcase, json, pdb
from django.utils.deprecation import MiddlewareMixin

class SnakeCaseMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.method == 'POST':
            request_data = getattr(request, '_body', request.body)
            request_data = json.loads(request_data)

            if request_data.get('title'):
                request_data['title'] = stringcase.snakecase(request_data['title'])
            if request_data.get('author'):
                request_data['author'] = stringcase.snakecase(request_data['author'])
            if request_data.get('description'):
                request_data['description'] = stringcase.snakecase(request_data['description'])

            request._body = json.dumps(request_data).encode('utf-8')