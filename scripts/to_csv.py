import csv
import stor
import pandas
import json

DATA_PATH = '../data/'

box = stor.Box(DATA_PATH)
population_raw = box.get('population_raw')
population = box.get('population')

f = open(DATA_PATH + 'population.csv', 'w+')
csv_file = csv.writer(f)
for i in range(0, len(population)):
    csv_file.writerow(population[i])
