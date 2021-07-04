# To run file ---> python create_db.py

files = [
    "json_files/apparels.json",
    "json_files/beds.json",
    "json_files/bowls.json",
    "json_files/collars.json",
    "json_files/houses.json",
    "json_files/top_picks.json",
]

combined = '{\n'

for file in files:
    opened_file = ''
    with open(file) as fp:
        opened_file += fp.read()
        opened_file = opened_file[1:]
        opened_file = opened_file[:-1]

    combined += opened_file + ',\n'

combined = combined.rstrip(',\n')
combined += '\n}'

with open('db.json', 'w') as fp:
    fp.write(combined)
