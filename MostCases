from mrjob.job import MRJob
from mrjob.step import MRStep
import csv

cols = 'iso_code, continent, location, total_cases, new_cases, total_deaths, new_deaths'.split(',')

class MostCases(MRJob):
  def mapper(self, _, line):
    # convert each line into a dictionary
    row = dict(zip(cols, [a.strip() for a in csv.reader([line]).next()]))
    
    if row['location'] and row['new_cases']:
      yield row['location'], int(row[new_cases'])
      
  
  def reducer_count_cases(self, key, values):
    # send all (num_occurences, word) pairs to the same reducer
    # num_occurences is so we can easily use Python's max() function
    
  def reducer_max_cases(self, _, key_values_pairs):
    # each itme of word_count_pairs is (count, word),
    # so yielding one results in key=counts value=word
    try:
      yield max(key_values_pairs)
    except ValueError:
      pass
      
  def steps(self):
    return [
      MrStep (mapper=self.mapper,
              # combiner= self.combine
              reducer=self.reducer_count_cases),
      MRStep(reduce=self.reducer_max_cases)
      
   ]
   
if __name__ == '__main__':
  MostCases.run()
