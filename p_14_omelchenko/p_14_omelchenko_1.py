import requests
import csv


fieldnames = ['song', 'year']

with open('p_14_omelchenko\\beatles', 'w') as file_path:
    writer = csv.DictWriter(file_path, fieldnames =  fieldnames)
    writer.writerow({   
                        'song': "Hard day's night",
                        'year': 1964,
                    })
    writer.writerow({   
                        'song': "Ticket to Ride",
                        'year': 1969,
                    })
    writer.writerow({   
                        'song': "Let it be",
                        'year': 1970,
                    })
    writer.writerow({   
                        'song': "I want to hold your hand",
                        'year': 1964,
                    })
    writer.writerow({   
                        'song': "I Want You (She’s So Heavy)",
                        'year': 1969,
                    })
with open('p_14_omelchenko\\beatles', 'r') as file_path:
    reader = csv.DictReader(file_path, fieldnames =  fieldnames)
    for heading in reader.fieldnames:
            print(heading, end=' ')
    print('\n------------------------------')
    for row in reader:
        print(row['song'], row['year'])
