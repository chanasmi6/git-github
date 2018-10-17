from wsgiref.simple_server import make_server
def hello_world(environ, start_response):
    status = '200 ok'
    headers = [('Content-type','text/plain')]
    start_response(status, headers)
    return ['Hello world']
httpd = make_server('',8085,hello_world)
print 'Serving on port 8085....'
httpd.serve_forever()   
