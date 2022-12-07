import datetime
import os
import re
import shutil

# 编辑变量区域
folderPath = r"C:\Users\文杰\Desktop\svn\信息安全_svn\python脚本\其他\批量修改字幕文件名\ori\4"    # 要处理的文件所在文件夹地址
assNumRegStr = r"(\[アニメ\] ARIA The ORIGINATION 第)(\d*)"  # 用于匹配集数的正则
numStartIndex = 1  # 表示正则中集数出现的分组序号，从0开始计数
#finalFileNameFormat = r"[Moozzi2] Aria The Natural - {:0>2d} (BD 1440x1080 x.264 Flac).ass"
finalFileNameFormat = r"[Moozzi2] Aria The Origination - {:0>2d} (BD 1920x1080 x.264 Flac).ass"

# 程序区域
fileNameList = os.listdir(folderPath)
nowTime = datetime.datetime.now().strftime("%Y%m%d-%X")
finalFolderName = "结果"
finalFolderPath = os.path.join(os.getcwd(), finalFolderName, nowTime.replace(":", ""))
if not os.path.exists(finalFolderPath):
    os.makedirs(finalFolderPath)
for fileIndex, fileName in enumerate(fileNameList):
    print("\r正在处理{0}/{1}个文件".format(fileIndex + 1, len(fileNameList)), end="")
    reObj = re.match(assNumRegStr, fileName)
    fileNum = int(reObj.groups()[numStartIndex])
    oriFilePath = os.path.join(folderPath, fileName)
    finalFileName = finalFileNameFormat.format(fileNum)
    finalFilePath = os.path.join(finalFolderPath, finalFileName)
    shutil.copy(oriFilePath, finalFilePath)
print("\n处理完成")