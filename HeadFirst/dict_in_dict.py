import pprint

people = {}
people['Ford'] = { 'Name': 'Ford Prefect',
                  'Gender': 'Male',
                  'Occupation': 'Researcher',
                  'Home Planet': 'Betelgeuss Seven' }
people['Arthur'] = { 'Name': 'Arthur Dent',
                  'Gender': 'Male',
                  'Occupation': 'Sandwich-Maker',
                  'Home Planet': 'Earth' }
people['Trillian'] = { 'Name': 'Tricia McMillan',
                  'Gender': 'Female',
                  'Occupation': 'Mathematician',
                  'Home Planet': 'Earth' }
people['Robot'] = { 'Name': 'Marvin',
                  'Gender': 'Unknown',
                  'Occupation': 'Paranoid Android',
                  'Home Planet': 'Unknown' }
pprint.pprint(people['Arthur']['Occupation'])