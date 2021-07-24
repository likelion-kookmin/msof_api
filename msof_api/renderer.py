from rest_framework.renderers import JSONRenderer
from rest_framework.utils import json


class JSONResponseRenderer(JSONRenderer):
    # media_type = 'text/plain'
    # media_type = 'application/json'
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_dict = {
            'success': True,
            'status code': 200,
            'next': data['next'] if 'next' in data else None,
            'previous': data['previous'] if 'previous' in data else None,
            'data': data['results'] if 'results' in data else data,
            'message': '',
        }
        data = response_dict
        return json.dumps(data)
