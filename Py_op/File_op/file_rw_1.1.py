# with open("relayTest.json", "r+") as jsonFile:
#     data = json.load(jsonFile)
#
#     data["location"] = "OldPath"
#     jsonFile.seek(0)  # rewind
#     json.dump(data, jsonFile, indent=4, sort_keys=True)
#     jsonFile.truncate() # in case, new data file size is smaller
#
#
#
#
# with open('relay.text', 'r+') as jfile:
#     data = json.load(jfile)
#
#     jfile.seek(0)
#
#     jfile.tell()
#
#     json.dump(data, jfile, indent=4, sort_keys=True)
#
#     jfile.truncate()

file_name = "C:\\Users\jsun\Documents\Desk_2\Py_op\File_op\\outfile3.txt"
test_item = "This is a test\n"
test_list = ["FW test\n", "API test\n", "UI test\n"]

with open(file_name,"w+") as fw:
    fw.write(test_item)
    fw.writelines(test_list)

    fw.seek(0)

    print(f"current cursor is at {fw.tell()}")
    line = fw.read()
    print(f"text after cursor IS+{line}")
    print(fw.tell())


# fw.seek(0) points to the first char "T" in "This is a test\n"
# current cursor is at 0
# text after cursor IS+This is a test
# FW test
# API test
# UI test
#
# 44
print("===========================")
import os
file_name = "C:\\Users\jsun\Documents\Desk_2\Py_op\File_op\\outfile3_1.txt"
os.remove(file_name)
test_item = "123456789\n0"
print(len(test_item)) # 11
# "\n" considered as single char
with open(file_name,"w+") as fw:
    fw.write(test_item)

    fw.seek(0)

    print(f"current cursor is at {fw.tell()}")
    # current cursor is at 0

    line = fw.read()
    print(f"text starting at cursor IS+{line}")

    print(fw.tell()) # 12


print("****************************")
import os
file_name = "C:\\Users\jsun\Documents\Desk_2\Py_op\File_op\\outfile3_2.txt"
if os.path.exists(file_name):
    os.remove(file_name)
test_item = "123456789\n0"
print(len(test_item)) # 11
# "\n" considered as single char
with open(file_name,"w+") as fw:
    fw.write(test_item)

    fw.seek(10)
    # seek treat "\n" holds two positions: #9 and # 10

    print(f"current cursor is at {fw.tell()}")
    # current cursor is at 0

    line = fw.read()
    print(f"text starting at cursor IS+{line}")

    print(fw.tell()) # 12