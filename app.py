import logging.config
import time

from flask import request, g

from blueprints import init_app

logging.config.fileConfig('logging.conf', defaults={'logfilename': 'log.log'})
logger = logging.getLogger('Request&Response')

app = init_app()


@app.before_request
def log_request():
    """
    Log all requests to a file
    """
    if request.path == '/favicon.ico':
        return
    elif request.path.startswith('/static'):
        return

    g.start = time.time()
    request_data = f"""\nRequest:
    Method: {request.method}
    Path: {request.path}
    IP: {request.headers.get('X-Forwarded-For', request.remote_addr)}
    HOST: {request.host.split(':', 1)[0]}
    Headers: {dict(request.headers)}
    Params: {dict(request.args)}
    Body: {request.get_data()}
"""
    logger.info(request_data)


@app.after_request
def log_request(response):
    """
    Log all responses to a file
    """
    if request.path == '/favicon.ico':
        return response
    elif request.path.startswith('/static'):
        return response

    duration = round(time.time() - g.start, 5)
    response_data = f"""\nResponse:
    Status code: {response.status_code}
    Time spent: {duration} secs
"""
    logger.info(response_data)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
