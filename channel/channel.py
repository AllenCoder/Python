# coding=utf-8

import zipfile
import shutil
import os
import sys
import platform

if __name__ == '__main__':
    # apkFile = sys.argv[1]

    apkFile = './app-debug4zj.apk'
    apk = apkFile.split('.apk')[0]
    # print apkFile
    emptyFile = 'xxx.txt'
    f = open(emptyFile, 'w')
    f.close()
    with open('channel/android_channels.txt', 'r') as f:
        contens = f.read()
    lines = contens.split('\n')
    if (os.path.exists('./release')):
        pass
    else:
        os.mkdir('./release')

    # print lines[0]
    for line in lines:
        channel = 'channel_' + line
        destfile = './release/%s_%s.apk' % (apk, channel)
        shutil.copy(apkFile, destfile)
        zipped = zipfile.ZipFile(destfile, 'a')
        channelFile = "META-INF/{channelname}".format(channelname=channel)
        zipped.write(emptyFile, channelFile)
        zipped.close()
    os.remove('./xxx.txt')

    # mac
    # os.system('chmod u+x zipalign_batch.sh')
    # os.system('./zipalign_batch.sh')

    # windows
    # os.system('zipalign_batch.bat')
    sysstr = platform.system()
    if (sysstr == "Windows"):
        os.system('zipalign_batch.bat')
    elif (sysstr == "Linux"):
        os.system('chmod u+x zipalign_batch.sh')
        os.system('./zipalign_batch.sh')
    else:
        print("Other System tasks")

