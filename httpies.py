#  环境必须安装过httpie
# python 3.5 后调用 要加上  --ignore-stdin
# 命令行调用http请求
import time
import subprocess

command1 ="ipconfig /all"

command2 ="http devcoder.cn -h --ignore-stdin"

# subprocess.call(command1, shell = True)
if __name__ == '__main__':
        while(True):
            subprocess.call(command2, shell = True)
            time.sleep(1)
