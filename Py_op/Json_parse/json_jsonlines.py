import json

data = [
  {
    "id": 1,
    "label": "A",
    "size": "S"
  },
  {
    "id": 2,
    "label": "B",
    "size": "XL"
  },
  {
    "id": 3,
    "label": "C",
    "size": "XXl"
  }
]

filename = "data_pretty.json"
filename_1 = "data_single_line.json"
filename_2 = "data_multiple_lines.json"

with open(filename, 'w') as fout:
    json.dump(data, fout, indent=4, sort_keys=True)

with open(filename_1, "w") as fout:
    json.dump(data, fout)

with open(filename_2, "w") as fout:
  for item in data:
    json.dump(item, fout)
    fout.write("\n")

# with open(filename_2, 'r') as fin:
#   data = json.load(fin)
#   print(data)
# son.decoder.JSONDecodeError: Extra data: line 2 column 1 (char 37)
with open(filename, 'r') as fin:
  data = json.load(fin)
  print(data)

