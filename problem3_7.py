import csv


def problem3_7(csv_pricefile, flower):
  f = open(csv_pricefile)
  for i in csv.reader(f):
    if flower == i[0]:
      print(i[1])
  f.close()