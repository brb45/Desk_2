
# This is an experimental python file which replaces the .csv file,
# as an alternate input file format.  I don't recall if flowgen actually
# can read this. - 8/31/12

import flowGen

rates = [ 
          'OFDM_6',
          'OFDM_12',
          'OFDM_18',
          'OFDM_24',
          'DSSS_1',
        ]

channels = [ 2412 ]
analyses = [ "TX_VERIFY_EVM" ]
power    = [ 15.0 ]
antenna  = ["(1,0,0,0)"]
technology = "WIFI"
output_file = "test_datarates.txt"

params = [ "DATA_RATE", "FREQ_MHZ",  "TEST", "POWER_DBM", "ANTENNA" ]
values = [ rates, channels, analyses, power, antenna ]

flowGen.run( params, values, technology, output_file )

