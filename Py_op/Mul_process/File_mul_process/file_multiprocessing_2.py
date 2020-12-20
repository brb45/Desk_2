import os
import time
from multiprocessing import Pool


def getFile(path):
  fileList = []
  for root, dirs, files in list(os.walk(path)):
    for i in files:
      if i.endswith('.txt') or i.endswith('.txt'):
        fileList.append(os.path.join(root, i))
  return fileList

def operFile(filePath) :
  # count lines and num of chars
  filePath = filePath
  fp = open(filePath)
  content = fp.readlines()
  fp.close()
  lines = len(content)
  alphaNum = 0
  for i in content :
    alphaNum += len(i.strip('\n'))
  return lines, alphaNum, filePath

def out(list1, writeFilePath) :
  # write results
  fileLines = 0
  charNum = 0
  # with open(writeFilePath, 'a') as fin:


  fp = open(writeFilePath, 'a')
  for i in list1:
    fp.write(i[2] + " has {} lines and {} chars\n".format(i[0], i[1]))
    #fp.write("lines")
    fileLines += i[0]
    charNum += i[1]
  fp.close()
  #print(fileLines, charNum)

if __name__ == "__main__":
  # Create processes
  startTime = time.time()
  filePath = os.getcwd()
  fileList = getFile(filePath)

  pool = Pool(5)
  resultList = pool.map(operFile, fileList)

  pool.close()
  pool.join()


  writeFilePath = "new_res.txt"
  print("Result List is: ")
  for i in resultList:
    print(i)
  out(resultList, writeFilePath)
  endTime = time.time()
  print ("\n\nused time is ", endTime - startTime)
