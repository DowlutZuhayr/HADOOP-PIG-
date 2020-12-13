from mrjob.job import MRJob
from mrjob.step import MRStep
import csv

cols = 'iso_code, continent, location, total_cases, new_cases, total_deaths, new_deaths'.split(',')

class Top10(MRJob):
  def mapper(self, _, line):
    # convert each line into a dictionary
    row = dict(zip(cols, [a.strip() for a in csv.reader([line]).next()]))
    
    if row['date'] >= '01\/09\/2020" and row['new_cases'] and row['location']:
      yield row['location'], int(row['new_cases'])
      
    
  def reducer_count_newcases(self, location, new_cases):
      yield None, (int(max(new_cases)), location)
      
  def secondreducer(self, key, max_cases):
      self.max_list = []
      for value in max_cases:
        self.max_list.append(value)
        
      for index in range(10):
        yield max(self.max_list)
        self.max_list.remove(max(self.max_list))
        
  def steps(self):
    return [
      MRStep(mapper=self.mapper,
              reducer=self.reducer_count_newcases),
      MRStep (reducer=self.secondreducer)
      ]
      
if '__name__' == '__main__':
  Top10.run()
