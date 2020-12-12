from mrjob.job import MRJob
from mrjob.step import MRStep
import csv

cols = 'iso_code, continent, location, total_cases, new_cases, total_deaths, new_deaths'.split(',')

class CovidAfrica(MRJob):
  def mapper(self, _, line):
    # convert each line into a dictionary
    row = dict(zip(cols, [a.strip() for a in csv.reader([line]).next()]))
    
    if row['continent'] == 'Africa' and row['new_deaths']:
      yield row['continent'], int(row['new_deaths'])
      
      
  def reducer(self, key, values):
    yield key, sum(values)
    
if __name__ == '__main__':
  CovidAfrica.run()
