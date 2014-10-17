from datetime import datetime
from unittest import TestCase
from DecipherAPI.client import Client, DEFAULT_HOST


def GetDimensions(text, delim=','):
    lines = text.split('\n')
    rows = len(lines)
    cols = len(lines[0].split(delim))
    return rows, cols


class TestClient(TestCase):

    def setUp(self):
        self.email = self.passwd = 'dataapi'
        self.path = 'kbdemo/data'

    def test_smoke(self):
        c = Client(self.email, self.passwd)
        self.assertIsInstance(c, Client)
        self.assertEqual(c.host, DEFAULT_HOST)

    def test_survey_json(self):
        c = Client(self.email, self.passwd)
        resp = c.get_survey(self.path)
        self.assertEqual(resp['status'], 'ok', resp)

    def test_list_json(self):
        c = Client(self.email, self.passwd)
        resp = c.list_surveys()
        self.assertEqual(resp['status'], 'ok', resp)

    def test_survey_csv(self):
        c = Client(self.email, self.passwd)
        n_rows, n_cols = GetDimensions(c.get_survey(self.path, fmt="csv"))
        self.assertEqual(
            n_rows, 74, 'produced a response with {} row(s)'.format(n_rows))
        self.assertEqual(
            n_cols, 11, 'produced a response with {} column(s)'.format(n_cols))

    def test_list_csv(self):
        c = Client(self.email, self.passwd)
        n_rows, n_cols = GetDimensions(c.list_surveys(fmt="csv"))
        self.assertEqual(
            n_rows, 2, 'produced a response with {} row(s)'.format(n_rows))
        self.assertEqual(
            n_cols, 9, 'produced a response with {} column(s)'.format(n_cols))

    def test_survey_tsv(self):
        c = Client(self.email, self.passwd)
        n_rows, n_cols = GetDimensions(
            c.get_survey(self.path, fmt="tsv"), delim='\t')
        self.assertEqual(
            n_rows, 74, 'produced a response with {} row(s)'.format(n_rows))
        self.assertEqual(
            n_cols, 11, 'produced a response with {} column(s)'.format(n_cols))

    def test_list_tsv(self):
        c = Client(self.email, self.passwd)
        n_rows, n_cols = GetDimensions(c.list_surveys(fmt="tsv"), delim='\t')
        self.assertEqual(
            n_rows, 2, 'produced a response with {} row(s)'.format(n_rows))
        self.assertEqual(
            n_cols, 9, 'produced a response with {} column(s)'.format(n_cols))

    def test_survey_start(self):
        c = Client(self.email, self.passwd)
        start = datetime(2009, 3, 5, 2, 35)
        n_rows, n_cols = GetDimensions(
            c.get_survey(self.path, start=start, fmt="csv"))
        self.assertEqual(
            n_rows, 57, 'produced a response with {} row(s)'.format(n_rows))
        self.assertEqual(
            n_cols, 11, 'produced a response with {} column(s)'.format(n_cols))

    def test_survey_end(self):
        c = Client(self.email, self.passwd)
        end = datetime(2009, 3, 5, 2, 35)
        n_rows, n_cols = GetDimensions(
            c.get_survey(self.path, end=end, fmt="csv"))
        self.assertEqual(
            n_rows, 18, 'produced a response with {} row(s)'.format(n_rows))
        self.assertEqual(
            n_cols, 11, 'produced a response with {} column(s)'.format(n_cols))

    def test_survey_status(self):
        c = Client(self.email, self.passwd)
        n_rows, n_cols = GetDimensions(
            c.get_survey(self.path, status='qualified', fmt="csv"))
        self.assertEqual(
            n_rows, 43, 'produced a response with {} row(s)'.format(n_rows))
        self.assertEqual(
            n_cols, 11, 'produced a response with {} column(s)'.format(n_cols))

    def test_survey_columns(self):
        c = Client(self.email, self.passwd)
        n_rows, n_cols = GetDimensions(
            c.get_survey(self.path, status='qualified', columns=['uuid', 'q1'], fmt="csv"))
        self.assertEqual(
            n_rows, 43, 'produced a response with {} row(s)'.format(n_rows))
        self.assertEqual(
            n_cols, 2, 'produced a response with {} column(s)'.format(n_cols))

    def test_survey_filters(self):
        c = Client(self.email, self.passwd)
        n_rows, n_cols = GetDimensions(c.get_survey(
            self.path, status='qualified', columns=['uuid', 'q1'], filters=['q1=1'], fmt="csv"))
        self.assertEqual(
            n_rows, 8, 'produced a response with {} row(s)'.format(n_rows))
        self.assertEqual(
            n_cols, 2, 'produced a response with {} column(s)'.format(n_cols))
