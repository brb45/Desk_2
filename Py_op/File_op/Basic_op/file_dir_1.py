import os, sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

file_dir = os.path.dirname(__file__)
file_path = os.path.pardir

join_path = os.path.join(file_dir, file_path)

print(file_dir)
print(file_path)
print(join_path)

print(sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))))

# C:/Users/jsun/Documents/Desk_1
# ..
# C:/Users/jsun/Documents/Desk_1\..
# None