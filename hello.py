def wcgi_app(environ, start_responce):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    
    
    
    start_response(status, headers)
    return [body]
