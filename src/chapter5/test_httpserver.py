# Author: lindafang
# Date: 2020-11-26 08:33
# File: test_httpserver.py

import requests
from pytest_httpserver import HTTPServer
from pytest_httpserver.httpserver import RequestHandler


def test_root(httpserver: HTTPServer):
    handler = httpserver.expect_request('/')
    assert isinstance(handler, RequestHandler)
    handler.respond_with_data('', status=200)

    response = requests.get(httpserver.url_for('/'))
    assert response.status_code == 200


def test_root1():
    # 不方便使用fixtures的场景，可以通过with来使用相同功能
    with HTTPServer() as httpserver:
        handler = httpserver.expect_request('/')
        assert isinstance(handler, RequestHandler)
        handler.respond_with_data('', status=200)

        response = requests.get(httpserver.url_for('/'))
        assert response.status_code == 200


def test_status(httpserver: HTTPServer):
    uri = '/status'
    handler = httpserver.expect_request(uri)
    handler.respond_with_data('', status=302)

    response = requests.get(httpserver.url_for(uri))
    assert response.status_code == 302


def test_method(httpserver: HTTPServer):
    uri = '/method'
    handler = httpserver.expect_request(uri=uri, method='GET')
    handler.respond_with_data('', status=200)

    response = requests.get(httpserver.url_for(uri))
    assert response.status_code == 200
    response = requests.post(httpserver.url_for(uri))
    assert response.status_code == 500


def test_respond_with_data(httpserver: HTTPServer):
    uri = '/data'
    handler = httpserver.expect_request(
        uri=uri,
        method='POST',
    )
    handler.respond_with_data('good')

    response = requests.post(httpserver.url_for(uri))
    assert response.status_code == 200
    assert response.content == b'good'


def test_respond_with_json(httpserver: HTTPServer):
    uri = '/data'
    expect = {'a': 1, 'b': 2}
    handler = httpserver.expect_request(
        uri=uri,
        method='POST',
    )
    handler.respond_with_json(expect)

    response = requests.post(httpserver.url_for(uri))
    assert response.status_code == 200
    assert expect == response.json()
