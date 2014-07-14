import requests
import simplejson

try:
    from urllib.parse import urlencode
except:
    from urllib import urlencode

DEFAULT_HOST = 'v2.decipherinc.com/api'
VALID_RESPONSE_FORMATS = ['json', 'tsv', 'csv']
VALID_SURVEY_STATUS = [
    'all', 'partial', 'complete', 'qualified', 'terminated', 'overquota']


class Client(object):

    def __init__(self, username, password, host=DEFAULT_HOST):
        self.host = host
        self.session = requests.session()
        self.session.auth = (username, password)
        self.session.headers.update({
            'User-Agent': 'decipher-python-client',
        })

    def request(self, target, fmt='json', return_uri=False):
        uri = self._build_uri(target)
        if return_uri:
            return uri
        response = self.session.get(uri)
        if response.status_code == requests.codes.OK and response.text:
            if fmt == 'json':
                return simplejson.loads(response.text)
            if fmt == 'tsv':
                return response.text.strip()
            if fmt == 'csv':
                return response.text.strip().replace('\t', ',')
            raise Exception("can't parse response. unknown format:", fmt)

        raise Exception(response.status_code, response.text)

    def _build_uri(self, target):
        return "https://{}{}".format(self.host, target)

    def get_survey(self, survey, start=None, end=None, status=None, columns=None, filters=None, fmt='json', return_uri=False):
        assert fmt in VALID_RESPONSE_FORMATS, "invalid format: {}".format(fmt)
        if status is not None:
            assert status in VALID_SURVEY_STATUS, "invalid status: {}".format(status)

        target = '/data/tab?survey={}'.format(survey)

        args = {}

        if start:
            args['start'] = start.isoformat() + 'Z'

        if end:
            args['end'] = end.isoformat() + 'Z'

        if status:
            args['status'] = status

        if columns and len(columns) > 0:
            args['vars'] = ','.join(columns)

        if fmt in ['tsv', 'csv']:
            args['format'] = 'text'
        else:
            args['format'] = 'json'

        if filters and len(filters) > 0:
            for col_val in filters:
                col, val = col_val.split('=')
                args['var:{}'.format(col)] = val

        if len(args) > 0:
            target = target + '&' + urlencode(args)

        return self.request(target, fmt=fmt, return_uri=return_uri)

    def list_surveys(self, fmt='json', return_uri=False):
        assert fmt in VALID_RESPONSE_FORMATS, "invalid format: {}".format(fmt)

        target = '/surveylist'
        args = {}

        if fmt in ['tsv', 'csv']:
            args['format'] = 'text'
        else:
            args['format'] = 'json'

        if len(args) > 0:
            target += '?' + urlencode(args)

        return self.request(target, fmt=fmt, return_uri=return_uri)
