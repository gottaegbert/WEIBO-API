# -*- coding: utf-8 -*-

# 访问 m.weibo.cn 的 request headers
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}

# info for https://passport.weibo.cn/signin/login
USER_PASSWORD = [
    {
        'user': '18846199813',
        'password': 'zzy1996110'
    },
    {
        'user': 'liyiming159@qq.com',
        'password': 'zxcvbnm0707'
    }
]

# Chrome driver 的路径，前往 http://chromedriver.chromium.org/downloads 下载
CHROME_DRIVER_PATH = 'C:\\Users\dell\Desktop\chromedriver_win32\chromedriver.exe'

# 请求次数，每次请求返回的数据大约10条，因具体 API 而异
WAITING_FOR_REQUESTS = 1
# 停多少秒
DELAY = 2
# 允许同时爬取的最多用户数量
MAX_CRAWING_USERS = 1
