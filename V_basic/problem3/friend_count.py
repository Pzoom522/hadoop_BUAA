import MapReduce, sys

mr = MapReduce.MapReduce()

def mapper(record):
  name = record[0]
  mr.emit_intermediate(name, 1)

def reducer(name, list_of_values):
  total = 0
  for v in list_of_values:
    total += v
  mr.emit((name, total))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
