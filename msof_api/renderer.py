from rest_framework.renderers import JSONRenderer
from rest_framework.utils import json


class JSONResponseRenderer(JSONRenderer):
    # media_type = 'text/plain'
    # media_type = 'application/json'
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context['response'].status_code
        success = str(status_code)[0:2] == '20'

        response_dict = {
            'success': success,
            'status code': status_code,
            'data': data['results'] if 'results' in data else data,
            'message': '',
        }
        if 'next' in data:
            response_dict['next'] = data['next']
        if 'previous' in data:
            response_dict['previous'] = data['previous']

        data = response_dict
        return json.dumps(data)
