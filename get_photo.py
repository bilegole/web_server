from multiprocessing import Process,Queue


def analyse_video(vwt):
#   调用神经网络，识别是否有车 参数为照片（二进制），时间戳（string）
#   if 判断是否有车（photo）：
#       请求高清照片（time）
    if (1):
        return True
    else:
        return False

def tell_me_plain(photo):
    plain = None
    return plain

#用作线程，不断从qu_photo中获取需要分析的照片的时间戳，
#向客户端发起请求，获取后进行神经网络识别并将结果写入qu_plain
#输入:带有string的qu_photo.
#
def analy_photo(qup,qupl):
    time_str = qup.get(True)
    photo = request_photo(time_str)


#给定string：时间戳，向客户端请求图片
#类型：中间函数
#过程：
#返回：二进制，照片
def request_photo(time):
    photo = None
    return photo