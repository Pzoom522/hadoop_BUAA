import sys,MapReduce

# globals
mr = MapReduce.MapReduce()

# record [matrix, i, j, value] 
def mapper(record):
  maxI = 10
  maxJ = 10

  if record[0] == 'a':
    i = record[1]
    for j in range(maxJ+1):
      mr.emit_intermediate((i, j), record)
  elif record[0] == 'b':
    j = record[2]
    for i in range(maxI+1):
      mr.emit_intermediate((i, j), record)
  else:
    pass

# key is (row,col) and values have to be operated on
def reducer(key, values):
  values = list(values)
  a_rows = filter(lambda x : x[0] == 'a', values)
  b_rows = filter(lambda x : x[0] == 'b', values)

  result = 0
  for a in a_rows:
    for b in b_rows:
      if (a[2]==b[1]):
        result += a[3] * b[3]

  # emit non-zero results
  if (result != 0):
    mr.emit((key[0], key[1], result))

if __name__ == '__main__':
  matrix = open(sys.argv[1])
  mr.execute(matrix, mapper, reducer)
