
log_file = "log_all.txt"
rst_file = "result.txt"
lastline = 0
search_key = 'DUT_DRIVER_INFO '
search_error = "<--Failed"
counter = 0
fout = open(rst_file,"w+")
with open(log_file,'r') as fin:
    for txt in fin:
        if search_key in txt:
            counter +=1
            #print("txt: ",txt, " counter: ",counter)
            fout.writelines("counter: %d           , txt: %s" %(counter,txt))
            #print("txt: {}, counter: {}".format(txt,counter))
        #if search_error in txt:
            #fout.write("Here is the error: %s" %txt)
lines_of_text = ["POWER_AVERAGE_DBM ", "EVM_AVG_DB ", "CH_FREQ_MHZ","\n"]
fout.writelines(lines_of_text)
fout.close()

from datetime import datetime
with open(rst_file,"a") as fout:
    test_time = datetime.now().strftime('%m/%d/%Y %H:%M:%S')
    fout.write(test_time)

with open(rst_file, 'r') as f:
    data = f.readlines()
    for line in data:
        words = line.split()
        word  = line.split(':')
        print (words)

with open(rst_file, 'r') as f:
    for line in f:
        words = line.split()
        word  = line.split(':')
        print (words)

with open(rst_file, 'r') as f:
    data = f.read()
    for line in data:
        words = line.split()
        word  = line.split(':')
        print (word)
    print (data)
    print (type(data))

