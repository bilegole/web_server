from wsgiref.simple_server import make_server
from listen_on_80 import listen_on_80
from multiprocessing import Queue,Process
import listen_video
import get_photo
import send_message

import  socket



min_port = 9000
max_port = 18000
max_delay = 1000 #ms
tip = True





#服务器初始化函数
if __name__ == "__main__":
    qu_port = Queue()       #用于记录有效端口
    qu_video = Queue()      #用于存放照片加时间戳
    qu_photo = Queue()
    qu_plain = Queue()      #用于存放提取到的信息

    print("启动服务器，试图获取ip地址.......")
    hostname = socket.gethostbyname()
    ip = socket.gethostbyname(hostname)
    print('ip获取成功，为%s' % ip)
    print('尝试建立一个80端口服务器')



    #def main():
    listen_on_80()
    #-----------------------

    an_vi = Process(target=listen_video.pro_vid_one,args=qu_video)
    #建立线程，用于不断将低清图片序列排序，并从中读取最大范围内的最远项。
    #               判断是否存在车辆，若有，则将时间序列写入qu_photo

    an_ph = Process(target=get_photo.analy_photo,args=(qu_photo,qu_plain))
    #建立线程，用于不断从高清图片时间序列中读取，向客户端请求图片，
    #识别车牌号并写入车牌号序列。


    send_mes = Process(target=send_message.send_message,args=qu_plain)
    #建立线程，用于不断读取车牌情况，并将其发送给客户端


    #-----------------------





    while(1):
    #-----------------------
       if not tip:
           an_ph.terminate()
           an_vi.terminate()
           send_mes.terminate()
           print("线程释放完毕。。。。")
           break
    #-----------------------



















#处理车牌图片
def pro_qu_palin():

    pass






from hello import application
httpd = make_server('127.0.0.1',8000,application)
print('Serving HTTP on port 8000...')
httpd.serve_forever()




