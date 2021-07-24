from rest_framework.compat import (INDENT_SEPARATORS, LONG_SEPARATORS,
                                   SHORT_SEPARATORS)
from rest_framework.renderers import JSONRenderer
from rest_framework.utils import json


class JSONResponseRenderer(JSONRenderer):
    # media_type = 'text/plain'
    # media_type = 'application/json'
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if data is None:
            return b''

        renderer_context = renderer_context or {}
        indent = self.get_indent(accepted_media_type, renderer_context)

        if indent is None:
            separators = SHORT_SEPARATORS if self.compact else LONG_SEPARATORS
        else:
            separators = INDENT_SEPARATORS

        status_code = renderer_context['response'].status_code
        success = str(status_code)[0:2] == '20'

        response_dict = {
            'success': success,
            'next': data['next'] if 'next' in data else None,
            'previous': data['previous'] if 'previous' in data else None,
            'status code': status_code,
            'data': data['results'] if 'results' in data else data,
            'message': ''
        }

        data = response_dict

        ret = json.dumps(
            data,
            cls=self.encoder_class,
            indent=indent,
            ensure_ascii=self.ensure_ascii,
            allow_nan=not self.strict,
            separators=separators
        )
        ret = ret.replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')
        return ret.encode()
