import csv

cid_header = ['id']
with open('cid.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if row == cid_header:
            print(f"header{row}")
            continue
        print(row)

cid1_header = ['id', 'name']
with open('cid1.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        try:
            cid = int(row[0].strip())
            print(f'type(id): {type(cid)}')
        except ValueError:
            print(f'row[0]: {row[0]} is not int')
            continue
        if row == cid1_header:
            print(f"header{row}")
            continue

        print(f'id: {row[0]}, name: {row[1]}')
