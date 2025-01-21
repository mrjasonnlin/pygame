from pyfirmata import Arduino, util
import time

# 初始化Arduino板
board = Arduino('com5')  # 根据实际情况修改端口

# 设置模拟引脚模式
temp_pin = board.get_pin('a:0:i')  # 模拟引脚0，输入模式


def read_temperature():
    return temp_pin.read() * 500  # 假设传感器输出0-5V对应0-500摄氏度


# 启动监听
it = util.Iterator(board)
it.start()

temp_pin.enable_reporting()

while True:
    temp = read_temperature()
    if temp is not None:
        print(f"Temperature: {temp:.2f} °C")
    time.sleep(1)