>>> [ s.upper() for s in st ]
['LORETTA', 'MARS']
>>> { s: 0 for s in st }
{'loretta': 0, 'mars': 0}
>>> { s: s.upper() for s in st }
{'loretta': 'LORETTA', 'mars': 'MARS'}
