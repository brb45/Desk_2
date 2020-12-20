
file_name = "C:\\Users\jsun\Documents\Desk_1\Py_op\File_op\\logging_test.txt"
# 2018-02-10 18: 33: 52, 527 - DEBUG - End
# 2018-02-10 18: 33: 52, 527 - INFO - The log
# 2018-02-10 18: 33: 52, 527 - WARNING - An
# 2018-02-10 18: 33: 52, 527 - ERROR - An err.

with open(file_name, 'r') as infile:
    #text = infile.read()# return a string
    tarr = []
    start_pos = infile.tell() # 0

    text = infile.read(10) #read 10 chars (10 bytes) starting byte 1 to byte 10
    pos = infile.tell()
    print(f"value at {pos} is {text}") 
    # value at 10 is 2018-02-10
    tarr.append(text)
    
    infile.seek(10) #point to byte 10, but starting read from byte 11
    text = infile.read(9) # read another 9 chars, starting at @11 -- @19
    tarr.append(text)
    print(tarr)  # ['2018-02-10', ' 18:33:52']
    pos = infile.tell() #19
    
with open(file_name, 'r') as infile:
    tarr = []
    text = infile.read(5)

    while text:
        end = infile.tell()
        tarr.append((end, text))
        text = infile.read(5)

    print(tarr) # Total 160 chars.

# [(5, '2018-'), (10, '02-10'), (15, ' 18:3'), (20, '3:52,'), (25, '527 -'), 
# (30, ' DEBU'), (35, 'G- En'), (41, 'd\n201'), (46, '8-02-'), (51, '10 18'), 
# (56, ':33:5'), (61, '2,527'), (66, ' - IN'), (71, 'FO- T'), (76, 'he lo'), 
# (82, 'g\n201'), (87,'8-02-'), (92, '10 18'), (97, ':33:5'), (102, '2,527'), 
# (107, ' - WA'), (112, 'RNING'), (118, '- An\n'), (123, '2018-'), 
# (128, '02-10'), (133, ' 18:3'), (138, '3:52,'), (143, '527 -'), 
# (148, ' ERRO'), (153, 'R- An'), (158, ' err.'), (160, '\n')]

with open(file_name, 'r') as infile:
    text_str = infile.read()
    print(len(text_str)) # 156
    #len() count '\n' as one char, infile.read('\n') count '\n' as 2 chars.

#2018-02-10
with open(file_name, 'r') as infile:
    pos = infile.seek(5) # Point to byte @5
    text = infile.read(5) # read 5 bytes starting byte @6
    print(text)  #02-10

