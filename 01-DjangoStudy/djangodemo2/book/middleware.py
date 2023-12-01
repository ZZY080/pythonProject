import  time
from django.http import  HttpResponse
from django.utils.deprecation import  MiddlewareMixin
# 限制用户访问次数 每60秒不超过5次
# 构建访问者IP池
# 以'ip'地址为键,以访问的网站的时间戳表作为值形如：{"127.0.0.1":[时间戳]}
visit_ip_pool={}

def simple_middleware(get_response):
    print('simple_middleware1 被调用')
    def middleware(request):
        # 此处编写的代码会在每个请求处理视图前被调用
        print('middleware1 before request 被调用')
        response=get_response(request)
        print('middleware1 after request 被调用')
        return response
    return  middleware

def simple_middleware2(get_response):
    print('simple_middleware2 被调用')
    def middleware2(request):
        # 此处编写的代码会在每个请求处理视图前被调用
        print('middleware2 before request 被调用')
        response=get_response(request)
        print('middleware2 after request 被调用')
        return response
    return  middleware2

class VisitLimitMiddleWare(MiddlewareMixin):
    def process_request(self,request):
        # 获取用户的访问的ip地址
        ip=request.META.get("REMOTE_ADDR")
        # 获取访问时间
        visit_time=time.time()
        if ip not in visit_ip_pool:
            # 维护字典,将新的ip地址加入字典
            visit_ip_pool[ip]=[visit_time]
        else:
            # 已经存在，则将ip对应值的插入列表开始位置
            visit_ip_pool[ip].insert(0,visit_time)
        # 获取ip_list列表
        ip_list=visit_ip_pool[ip]
        # 计算访问时间差
        lead_time=ip_list[0]-ip_list[-1]
        print("地址：",ip,"访问次数：",len(ip_list),"时间差",lead_time)
        # 两个条件同时成立则,间隔时间在60s内
        while ip_list and lead_time>60:
            # 默认移除列表中的最后一个元素
            ip_list.pop()
        # 间隔在六十秒内判断列表的长度即访问的次数是否大于5次
        if len(ip_list)>5:
            return  HttpResponse("对不起，访问过于频繁，将终止你的访问请求....")
        print("地址：", ip, "访问次数：", len(ip_list), "时间差", lead_time)