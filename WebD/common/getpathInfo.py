import os


def get_Path():

    path = os.path.split(os.path.realpath(__file__))
    print(f"path is {os.path.realpath(__file__)}")
    # path is C:\Users\jsun\Documents\Desk_2\WebD\1\find_path.py
    return path[0]


if __name__ == '__main__':  # 执行该文件，测试下是否OK
    print('测试路径是否OK,路径为：', get_Path())
    # 测试路径是否OK, 路径为： C:\Users\jsun\Documents\Desk_2\WebD\1
