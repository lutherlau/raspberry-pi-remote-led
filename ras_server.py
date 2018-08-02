import socket

# 地址信息
HOST = ('', 6005)

# 返回的头部
POST_RET = '''HTTP/1.1 200 OK  
Content-Type: text/html
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: POST

'''

# Socket配置（HTTP）
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(HOST)  # 绑定服务地址
server.listen(10)  # 最大连接数

# 报文首部与正文分隔符
line_separator = '\r\n\r\n'

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print('导入GPIO模块错误，请尝试使用管理员权限重试')

# 设置模式
GPIO.setmode(GPIO.BOARD)
# 忽略警告
GPIO.setwarnings(False)
# 设置输出的针脚
GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW)

led_state = 0
ret_state = ''
while True:
    client, address = server.accept()
    try:
        request = client.recv(1024).decode(encoding='utf-8')
    except Exception:
        client.sendall('error'.encode(encoding='utf-8'))
        client.close()
        continue

    method = request.split(' ')[0]

    if method == 'POST':
        # 获取控制表单
        user_cmd = request.split(line_separator)[-1]
        cmd = user_cmd.split('=')[-1]
        try:
            print(cmd)
            if cmd == 'on':
                GPIO.output(40, 1)
                led_state = 1
            elif cmd == 'off':
                GPIO.output(40, 0)
                led_state = 0

            if led_state:
                ret_state = 'led is on'
            else:
                ret_state = 'led is off'
            client.sendall((POST_RET + ret_state).encode(encoding='utf-8'))

        except Exception:
            client.sendall((POST_RET + 'Error').encode(encoding='utf-8'))
    client.close()
import socket

# 地址信息
HOST = ('', 3721)

# 返回的头部
POST_RET = '''HTTP/1.1 200 OK  
Content-Type: text/html
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: POST

'''

# Socket配置（HTTP）
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(HOST)  # 绑定服务地址
server.listen(10)  # 最大连接数

# 报文首部与正文分隔符
line_separator = '\r\n\r\n'

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print('导入GPIO模块错误，请尝试使用管理员权限重试')

# 设置模式
GPIO.setmode(GPIO.BOARD)
# 忽略警告
GPIO.setwarnings(False)
# 设置输出的针脚
GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW)

led_state = 0
ret_state = ''
while True:
    client, address = server.accept()
    try:
        request = client.recv(1024).decode(encoding='utf-8')
    except Exception:
        client.sendall('error'.encode(encoding='utf-8'))
        client.close()
        continue

    method = request.split(' ')[0]

    if method == 'POST':
        # 获取控制表单
        user_cmd = request.split(line_separator)[-1]
        cmd = user_cmd.split('=')[-1]
        try:
            print(cmd)
            if cmd == 'on':
                GPIO.output(40, 1)
                led_state = 1
            elif cmd == 'off':
                GPIO.output(40, 0)
                led_state = 0

            if led_state:
                ret_state = 'led is on'
            else:
                ret_state = 'led is off'
            client.sendall((POST_RET + ret_state).encode(encoding='utf-8'))

        except Exception:
            client.sendall((POST_RET + 'Error').encode(encoding='utf-8'))
    client.close()
