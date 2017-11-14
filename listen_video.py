import get_photo
import classs





##整理queue_video的函数，将其整理后保存到queue_video_true
#def rego_quvi(qu,qut):
 #   pass


#video帧处理函数，
#输入：车牌序列
#内容：提取给定时间范围内最远的一帧，判断是否有车辆
#     如果有，则请求高清图片
#     若没有，那就什么也不做
def pro_vid_one(qu):


    vwt = classs.video_with_time()      #此处应该从qu_video中获取一个vwt而不是新创建一个
    vwt = pick_up_from_qu_video_tidy(qu)
    exist_car = get_photo.analyse_video(vwt)
    if exist_car:
        get_photo.request_photo(vwt)
    else :
        pass

def pick_up_from_qu_video_tidy():
    pass
