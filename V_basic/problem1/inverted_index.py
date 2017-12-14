import MapReduce, sys

mr = MapReduce.MapReduce()

def mapper(record):
  # key: document identifier
  # value: document contents
  fileName = record[0]
  value = record[1]
  words = value.split()
  for w in words:
    mr.emit_intermediate(w, fileName)

def reducer(key, fileNames):
  fileList = []
  for fileName in fileNames:
    if fileName not in fileList:
      fileList.append(fileName)
  mr.emit((key, fileList))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
