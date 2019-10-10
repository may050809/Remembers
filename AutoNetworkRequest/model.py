import urllib.request
import plistlib
from html.parser import HTMLParser
from operator import itemgetter
import os

def saveTofile(string, fileName):
  workspaceDir = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
  path = workspaceDir + "/" + fileName
  stream = open(path, 'w')
  stream.write(string)
  stream.close()
  print("file saved in {}".format(path))


fileName = "Model.swift"
swiftString = "import Foundation\nimport SwiftyJSON\n\n"

with open("Model.plist", 'rb') as fp:
  pl = plistlib.load(fp)
  
  for key, value in pl.items():
    firstLine = "struct " + key + " {\n"
    swiftString = swiftString + firstLine
    dic = pl[key]
    for keyOfDic, valueOfDic in dic.items():
      lineString = "  let " + keyOfDic + ": " + valueOfDic + "\n"
      swiftString = swiftString + lineString
    
    produceLineString = "\n  static func produce(from json: JSON) -> " + key + " {\n" + "    return " + key + "("
    swiftString = swiftString + produceLineString
    numOfSpace = len(key) + 12
    spaceString = " " * numOfSpace
    isFirstLine = 1
    notLastLine = len(dic)
    for keyOfDicForProduce, valueOfDicForProduce in dic.items():
      lineStringOfProduce = ""
      if not(isFirstLine):
        lineStringOfProduce = spaceString
      if valueOfDicForProduce == "Bool" or valueOfDicForProduce == "String" or valueOfDicForProduce == "Int":
        lineStringOfProduce = lineStringOfProduce + keyOfDicForProduce + ": " + "json[\"" + keyOfDicForProduce + "\"]"
        lineStringOfProduce = lineStringOfProduce + "." + valueOfDicForProduce.lower() + "Value"
      else :
        lineStringOfProduce = lineStringOfProduce + keyOfDicForProduce + ": " + valueOfDicForProduce + ".produce(from: json[\"" + keyOfDicForProduce + "\"])"
      notLastLine = notLastLine - 1
      if notLastLine:
        lineStringOfProduce = lineStringOfProduce + ",\n"
      else:
        lineStringOfProduce = lineStringOfProduce + ")\n"
      swiftString = swiftString + lineStringOfProduce
      isFirstLine = 0
      
    swiftString = swiftString + "  }\n"
    lastLine = "}\n\n"
    swiftString = swiftString + lastLine

saveTofile(swiftString, fileName)
