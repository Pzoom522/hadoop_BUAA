import MapReduce, sys

mr = MapReduce.MapReduce()

def mapper(friendship):
  mr.emit_intermediate(friendship[0], friendship[1])
  mr.emit_intermediate(friendship[1], friendship[0])

def reducer(person, list_of_friends):
  friendCount = {}
  for friend in list_of_friends:
    friendCount.setdefault(friend, 0)
    friendCount[friend] = friendCount[friend] + 1

  asymfriends = filter(lambda x : friendCount[x] == 1, friendCount.keys())

  for friend in asymfriends:
    mr.emit((person, friend))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
