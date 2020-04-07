# -*- coding: UTF-8 -*

config = {
    # Bmob 配置
    'bmob': {
        'APP_ID': '366372322020724a39d8de5ccd61eeaa',
        'REST_API_KEY': '40de9f3e91287703e695fe1f6b94393a',
    },
    # 微博配置
    'weibo': {
        # Cookie 获取方法：前往 m.weibo.cn，打开一条评论较多的微博全文，往下翻几页
        # 这时 Chrome 的 Network 界面的 request headers 就会有 Cookie 信息了
        # 注意: m.weibo.cn 比较特殊，查看微博并不需要登录，而看评论确实是需要的
        # 比如直接进这个网址 https://m.weibo.cn/detail/4389138709375153，往后多翻几条评论在 Network 的 XHR 里面可以看到 request headers 的 Cookie
        'COOKIE': '_T_WM=25387770715; WEIBOCN_FROM=1110006030; SCF=As_-yP-N2m2DH5s6zfyeGjQhu-krcrxuROefVtbVdJ6GJK9kya1QserAmHkWTbKEUTn6KmufDCW_813R2xCFu_E.; SUB=_2A25zjrf3DeRhGeNN71sU9yjFyT-IHXVRcNm_rDV6PUJbktANLUPkkW1NSYVk0UN-RRifgzbawAX6hgqvBG2v3nUh; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5UVcHLujdadU6ZwYbxNmHC5JpX5KzhUgL.Fo-0Sh.fS0q4eoe2dJLoI7yfMGH7dgLV97tt; SUHB=0ftpmFZq6YKmSF; SSOLoginState=1586153383; MLOGIN=1; XSRF-TOKEN=4861c7; M_WEIBOCN_PARAMS=lfid%3D102803%26luicode%3D20000174%26uicode%3D20000061%26fid%3D4489690394798363%26oid%3D4489690394798363'
    },
    'mysql': {
        'CONNECTION': {
            'host': "localhost",
            'user': 'root',
            'password':'1234567',
            'port':"3306",
            'charset': 'utf8mb4'
        }
    },
    'crawl': {
        # 用来初始化爬取队列
        'START_USER': '1769119665',
        # 每两次请求之间等待 PERIOD 秒
        'PERIOD': 4,
        # 被封之后等待 5 分钟再次请求
        'FORBID_PAUSE': 300
    }
}
