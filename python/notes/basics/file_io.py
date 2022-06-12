import csv
import os


def open_csv():
    # dirname = os.path.getcwd()
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../00_data/mpg.csv')
    with open(filename) as csvfile:
        # convert elements to a list , of dicts
        mpg=list(csv.DictReader(csvfile))

        # first 3 elements
        #print(mpg[:3])

        # column names
        print(mpg[0].keys())

        # get unique values available for some field
        cylinders = set(d['cyl'] for d in mpg )
        print(cylinders)

        vehicleClass = set(d['class'] for d in mpg )
        print(vehicleClass)


if __name__ == '__main__':
    open_csv()



