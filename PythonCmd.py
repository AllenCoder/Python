import subprocess

command ="ipconfig /all"

command =["http","devcoder.cn",'-h']

# command =["http"]
# proc = subprocess.Popen("ipconfig /all", shell = True)
# proc = subprocess.Popen(command, shell = True)

# s = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
# s.communicate()
# proc.wait() # 等待子进程结束

"cd C:\\work\\android"
"gradle assemble"

# subprocess.call("cd C:\\work\\android", shell = True)
# subprocess.call("gradle assemble", shell = True)
subprocess.call("http baidu.com -h", shell = True)
# out_text=subprocess.check_output(command, shell = True).decode('utf-8')
# proc.wait() # 等待子进程结束