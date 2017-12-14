import MapReduce, sys

mr = MapReduce.MapReduce()

def mapper(record):
  order_id = record[1]
  value = record
  mr.emit_intermediate(order_id, value)

def reducer(order_id, values):
  for value in values:
    if value[0] == 'order':
      order=value
      
  for value in values:
    if value[0] == 'line_item':
      mr.emit((order + value))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
