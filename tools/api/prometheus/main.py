import time
from urlparse import urlparse, parse_qs

import requests
from flask import request
from flask.helpers import make_response
from prometheus_client import core, generate_latest, CONTENT_TYPE_LATEST, Gauge, Histogram, Counter
import flask


def monitor(app):
    def before_request():
        flask.g.start_time = time.time()
        http_concurrent_request_count.inc()
        content_length = request.content_length
        if (content_length):
            http_request_size_bytes.labels(request.method, request.path).observe(content_length)

    def after_request(response):
        request_latency = time.time() - flask.g.start_time
        http_request_latency_ms.labels(request.method, request.path).observe(request_latency)

        http_concurrent_request_count.dec()

        username = 'Unknown'
        if request.authorization:
            username = request.authorization.get('username')

        http_request_count.labels(request.method, request.path, response.status_code, username).inc()
        http_response_size_bytes.labels(request.method, request.path).observe(response.calculate_content_length())
        return response

    http_request_latency_ms = Histogram('http_request_latency_ms', 'HTTP Request Latency',
                                        ['method', 'endpoint'])

    http_request_size_bytes = Histogram('http_request_size_bytes', 'HTTP request size in bytes',
                                        ['method', 'endpoint'])

    http_response_size_bytes = Histogram('http_response_size_bytes', 'HTTP response size in bytes',
                                         ['method', 'endpoint'])

    http_request_count = Counter('http_request_count', 'HTTP Request Count', ['method', 'endpoint', 'http_status', 'user'])
    http_concurrent_request_count = Gauge('http_concurrent_request_count', 'Flask Concurrent Request Count')
    app.before_request(before_request)
    app.after_request(after_request)

    app.add_url_rule('/metrics', 'prometheus_metrics', view_func=metrics)
    res = requests.get('http://localhost:9090/api/v1/query?query=http_request_count',
                       headers={'Accept': 'application/json'})

    results = res.json()['data']['result']
    for result in results:
        val = int(result['value'][1])
        method = result['metric'].get('method') or 0
        endpoint = result['metric'].get('endpoint') or 0
        http_status = result['metric'].get('http_status') or 0
        user = result['metric'].get('user') or 0
        http_request_count.labels(method, endpoint, http_status, user).inc(val)


def metrics():
    registry = core.REGISTRY
    params = parse_qs(urlparse(request.path).query)
    if 'name[]' in params:
        registry = registry.restricted_registry(params['name[]'])
    output = generate_latest(registry)
    response = make_response(output)
    response.headers['Content-Type'] = CONTENT_TYPE_LATEST
    return response
