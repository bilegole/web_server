from wsgiref.simple_server import make_server
import json

def listen_on_80():
    httpd = make_server('',80,application_on_80)
    httpd.serve_forever()



def application_on_80(env,response):
    if env['Require-port'] == True: #打开10000。10001。10002。10003。10004端口
        free_port = get_free_port()
        js_free_port = json.dumps(free_port)
    response('200 OK',[('Content-Type','text/html'),('Free-port',js_free_port)])
    for i in free_port:
        listen_on_port(i,1)
    return [b'<h1>Hello.web!</h1>']



def get_free_port ():
    return [10000,10001,10002,10003,10004]


#打开相应接口的监听
def listen_on_port(port): #type-1:图片
    #打开端口
    httpd = make_server('',port,application_on_port)
    httpd.serve_forever()
    #获取
    return 0;

def application_on_port(env,response):
    try:
        request_body_size = int(env.get('CONTENT_LENGTH',0))
    except (ValueError):
        request_body_size = 0
    request_body = env['wsgi.input'].read(request_body_size)
    response('200 OK',[('Content-Type','test/html')])
    return [b'<h1>Hello, web!</h1>']