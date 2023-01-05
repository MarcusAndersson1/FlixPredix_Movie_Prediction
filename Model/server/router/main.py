print("döda mig")

import csv


with open('Model/data/tmdb_5000_movies.csv','rt') as f:
    data = csv.reader(f)

    for row in data:
        print(row[0])

    # for row in data:
    #     for feature in row:
    #         try:
    #             print(int(feature))
    #         except:
    #             print()
