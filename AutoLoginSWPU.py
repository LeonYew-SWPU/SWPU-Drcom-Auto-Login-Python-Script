import requests

##################################################################################################################
# 本脚本仅供学习交流使用，编写目的仅为方便本人每次去图书馆登录 Wi-Fi，请遵守学校网络提供商规定，不得用于任何商业和非法用途，否则后果自负。
# 本脚本基于 Python3.12.3 编写，使用了 request 库，需要安装 requests 库
# 本脚本仅适用于西南石油大学校园网，其他学校可能无法使用
# 作者：LeonYew(https://leonyew.fun/)
##################################################################################################################
debug_mode = False  # 调试模式，如果为 True 则每次都会登录，否则只有在没有互联网连接时才会登录

# 配置你的学校认证页面的URL、用户名和密码
auth_url = "http://************/"  # 替换为学校认证页面的URL
username = "************"  # 替换为你的用户名
upass = "************"  # 替换为你的密码
login_url = auth_url + "drcom/login?callback=dr1003&DDDDD=" + username + "&upass=" + upass + "&0MKKey=123456&R1=0&R2=&R3=0&R6=0&para=00&v6ip=&terminal_type=1&lang=zh-cn&jsVersion=4.1.3&v=3081&lang=zh"
logout_url = auth_url + "drcom/logout?callback=dr1004&jsVersion=4.1.3&v=1418&lang=zh"
test_url = "https://www.baidu.com"  # 用于测试互联网连接

# 检测互联网链接
def check_internet_connection(): 
    try:
        response = requests.get(test_url, timeout=5)
        if response.status_code == 200:
            print("Connected to the internet.(" + test_url + ")")
            return True
    except requests.RequestException:
        print("No internet connection...(" + test_url + ")")
        return False

# 登录认证操作
def login():
    # 发送登录请求
    response = requests.get(login_url)
    
    # if response.status_code == 200:
    #     print("Login request sent.")
    # else:
    #     print("Failed to send login request.")
    #     return
    
    if '"result":1' in response.text:
        print("Login Success!")
    else:
        print("Login Failed!")

    # 检查是否成功连接到互联网
    check_internet_connection()

# 程序入口

if(debug_mode):
    login()
else:
    if not check_internet_connection():
        login()

