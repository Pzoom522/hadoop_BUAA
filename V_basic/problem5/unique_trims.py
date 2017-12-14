import sys,json,MapReduce

mr = MapReduce.MapReduce()

def mapper(dnaseq):
  seqId = dnaseq[0]
  nucleotide = dnaseq[1]
  trimmedNucleotide = nucleotide[:-10]
  mr.emit_intermediate(trimmedNucleotide, seqId)

def reducer(trimmedNucleotide, seqIds):
  mr.emit(trimmedNucleotide)

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
