
set PROGRAM=python flowGen.py
REM set PROGRAM=dist\flowGen
REM set PROGRAM=flowGen

REM test 1
rem python flowGen.py test\test_flow1.csv
%PROGRAM% test\test_flow1.csv
diff -b test_flow.txt test\test_flow1_out.txt

REM test 2
%PROGRAM% test\test_flow2.csv
diff -b test_flow.txt test\test_flow2_out.txt

REM test 3
%PROGRAM% test\test_flow3.csv
diff -b test_flow.txt test\test_flow3_out.txt

REM test 4
%PROGRAM% test\test_flow4.csv
diff -b test_flow.txt test\test_flow4_out.txt

REM test 5
%PROGRAM% test\test_flow5.csv
diff -b test_flow.txt test\test_flow5_out.txt

REM test 6
%PROGRAM% test\test_flow6.csv
diff -b test_flow.txt test\test_flow6_out.txt

REM test 7
%PROGRAM% test\test_flow7_mps.csv
diff -b test_flow.txt test\test_flow7_mps_out.txt

REM test 8
%PROGRAM% test\test_flow8.csv
diff -b test_flow.txt test\test_flow8_out.txt

REM test 9
%PROGRAM% test\test_flow9_mps.csv
diff -b test_flow.txt test\test_flow9_out.txt

REM test 10 : example1_wifi
%PROGRAM% input\example1_wifi.csv
diff -b test_flow.txt test\example1_wifi_out.txt

REM test 11 : example2_wifi_mps
%PROGRAM% input\example2_wifi_mps.csv
diff -b test_flow.txt test\example2_wifi_mps_out.txt

REM test 12 : example3_wifi
%PROGRAM% input\example3_wifi.csv
diff -b test_flow.txt test\example3_wifi_out.txt

REM test 13 : multiple csv files
%PROGRAM% test\test_flow1.csv test\test_flow6.csv
diff -b test_flow.txt test\test_flow13_out.txt

REM test 14 : Tushar's multiple csv files
%PROGRAM% test\tushar_wifi.csv test\tushar_wifi_mps.csv test\tushar_5G_wifi.csv test\tushar_5G_wifi_mps.csv -o tushar_out.txt
diff -b tushar_out.txt test\tushar_out.txt

REM test 15
%PROGRAM% test\test_flow15_bt.csv
diff -b test_flow.txt test\test_flow15_out.txt

REM test 16
%PROGRAM% input\example4_bt.csv
diff -b test_flow.txt test\example4_bt_out.txt

REM test 17 multiple-section csv input file plus regular csv files
%PROGRAM% test\test_flow1.csv test\test_flow17.csv test\test_flow7_mps.csv
diff -b test_flow.txt test\test_flow17_out.txt

REM test 18 : example1_wifi for short format
%PROGRAM% -f short input\example1_wifi.csv
diff -b test_flow.txt test\test_flow18_out.txt

REM test 19 : example2_wifi_mps for short format
%PROGRAM% -f short input\example2_wifi_mps.csv
diff -b test_flow.txt test\test_flow19_out.txt

REM test 20 : example3_wifi for short format
%PROGRAM% -f short input\example3_wifi.csv
diff -b test_flow.txt test\test_flow20_out.txt

REM test 21: example5_bt for short format
%PROGRAM% -f short input\example5_bt_short.csv
diff -b test_flow.txt test\test_flow21_out.txt

REM test 22: multiple-section csv input file plus regular csv files, for short format
%PROGRAM% -f short test\test_flow1.csv test\test_flow17.csv test\test_flow7_mps.csv
diff -b test_flow.txt test\test_flow22_out.txt

REM test 23: whitespace in csv file (input equivalent to test1, so compare test1 output)
%PROGRAM% test\test_flow23.csv
diff -b test_flow.txt test\test_flow1_out.txt

REM test 24 multiple-section csv input file, with excel ",,,," dividers, 
REM for iqlite (with output same as test 17)
%PROGRAM% test\test_flow1.csv test\test_flow24.csv test\test_flow7_mps.csv
diff -b test_flow.txt test\test_flow17_out.txt

REM test 25 multiple-section csv input file, with excel ",,,," dividers, 
REM for short format (with output same as test 22, and uses test 24 input)
%PROGRAM% -f short test\test_flow1.csv test\test_flow24.csv test\test_flow7_mps.csv
diff -b test_flow.txt test\test_flow22_out.txt

REM test 26 use template with limits, on multiple-section csv input file plus regular csv files
%PROGRAM% -t templates.limits test\test_flow1.csv test\test_flow17.csv test\test_flow7_mps.csv
diff -b test_flow.txt test\test_flow26_out.txt

REM test 27 : test tx tests for push flow
%PROGRAM% -f push test\push_tx.csv
diff -b test_flow.txt test\test_flow27_out.txt

REM test 28 : test tx tests for push flow
%PROGRAM% -f push test\push_rx.csv
diff -b test_flow.txt test\test_flow28_out.txt

REM test 29 : test tx tests for push flow
%PROGRAM% -f push test\push_txrx.csv
diff -b test_flow.txt test\test_flow29_out.txt

REM test 30 : test tx tests for long push flow
%PROGRAM% -f push test\push_tx_long.csv
diff -b test_flow.txt test\test_flow30_out.txt

REM test 31 : test rx tests for long push flow
%PROGRAM% -f push test\push_rx_long.csv
diff -b test_flow.txt test\test_flow31_out.txt

REM test 32 : test tx/rx tests for long push flow
%PROGRAM% -f push test\push_txrx_long.csv
diff -b test_flow.txt test\test_flow32_out.txt

REM test 33 : test enable duplicate tests for tx/rx tests for long push flow
%PROGRAM% -d -f push test\push_txrx_long.csv
diff -b test_flow.txt test\test_flow33_out.txt


