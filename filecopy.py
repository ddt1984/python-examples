import os
import shutil

# 디렉토리에서 파일 이름 출력
files = os.listdir("G:\\My Drive\\SQL Training")
for file in files:
    print(file)

# 파일 하나 복사
origFilename = "G:\\My Drive\\test.txt"
destFilename = "C:\\Python Examples\\samples\\test.txt"
shutil.copyfile(origFilename, destFilename)

# 디렉토리 통으로 복사
origDirectory = "G:\\My Drive\\SQL Training"
destDirectory = "C:\\Python Examples\\samples\\sqltraining"
shutil.copytree(origDirectory, destDirectory)

# 디렉토리에서 특정 파일만 복사
origDirectory = "G:\\My Drive\\SQL Training\\"
filenames = os.listdir(origDirectory)
for filename in filenames:
    if filename.endswith(".png"): #파일이름이 .png로 끝나는 파일만 복사
        shutil.copyfile(origDirectory + filename, "C:\\Python Examples\\samples\\" + filename)

