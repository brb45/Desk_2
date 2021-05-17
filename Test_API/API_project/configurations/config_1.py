import configparser

config = configparser.ConfigParser()

config['DEFAULT'] = {
    'ServerAliveInterval' : "45",
    'Compression' : 'yes',
    'CompressiionLevel': '9'
}

config['bitbucket.org'] = {}

config['users'] = {}
# config['users']['id'] = 1 raise TypeError("option values must be strings")
config['users']['id'] = '1'

config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Port'] = '50022'     # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'

with open("config_1.ini", "w") as configfile:
    config.write(configfile)


# read back
config_read = configparser.ConfigParser()
print(config_read.sections()) # []

print(config_read.read('example.ini')) # []

res = config.sections() #
print(type(res), res)
# <class 'list'>
# ['bitbucket.org', 'users', 'topsecret.server.com']



print(config['DEFAULT']['Compression'])
'yes'
topsecret = config['topsecret.server.com']
print(topsecret['ForwardX11'])
'no'
print(topsecret['Port'])
'50022'
for key in config['bitbucket.org']:
    print(key)
# user
# compressionlevel
# serveraliveinterval
# compression
# forwardx11


# Config parsers do not guess datatypes of values in configuration files, always storing them internally as strings.
# This means that if you need other datatypes, you should convert on your own:

#  int(topsecret['Port'])
# 50022
#  float(topsecret['CompressionLevel'])
# 9.0

# Supported INI File Structure¶
# A configuration file consists of sections, each led by a [section] header, followed by key/value
# entries separated by a specific string (= or : by default 1). By default, section names are case
# sensitive but keys are not 1. Leading and trailing whitespace is removed from keys and values.
# Values can be omitted, in which case the key/value delimiter may also be left out. Values can
# also span multiple lines, as long as they are indented deeper than the first line of the value.
# Depending on the parser’s mode, blank lines may be treated as parts of multiline values or ignored.
#
# Configuration files may include comments, prefixed by specific characters (# and ; by default 1).
# Comments may appear on their own on an otherwise empty line, possibly indented. 1
#
# For example:
"""
[Simple Values]
key=value
spaces in keys=allowed
spaces in values=allowed as well
spaces around the delimiter = obviously
you can also use : to delimit keys from values

[All Values Are Strings]
values like this: 1000000
or this: 3.14159265359
are they treated as numbers? : no
integers, floats and booleans are held as: strings
can use the API to get converted values directly: true

[Multiline Values]
chorus: I'm a lumberjack, and I'm okay
    I sleep all night and I work all day

[No Values]
key_without_value
empty string value here =

[You can use comments]
# like this
; or this

# By default only in an empty line.
# Inline comments can be harmful because they prevent users
# from using the delimiting characters as parts of values.
# That being said, this can be customized.

    [Sections Can Be Indented]
        can_values_be_as_well = True
        does_that_mean_anything_special = False
        purpose = formatting for readability
        multiline_values = are
            handled just fine as
            long as they are indented
            deeper than the first line
            of a value
        # Did I mention we can indent comments, too?
"""