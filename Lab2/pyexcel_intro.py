import pyexcel
from collections import OrderedDict

data = [
    OrderedDict({
        'name' : 'an',
        'age' : 22,
    }),
    OrderedDict({
        'name' : 'not human',
        'age' : 0,
    }),
    OrderedDict({
        'name' : 'what ever',
        'age' : 0,
    })
]

pyexcel.save_as(records = data, dest_file_name='sample.xlsx')