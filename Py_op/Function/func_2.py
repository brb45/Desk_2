kwargs in **kwargs is just variable name. You can very well have **anyVariableName
kwargs stands for "keyword arguments". But I feel they should better be called as "named arguments", as these are simply arguments passed along with names (I dont find any significance to the word "keyword" in the term "keyword arguments". I guess "keyword" usually means words reserved by programming language and hence not to be used by the programmer for variable names. No such thing is happening here in case of kwargs.). So we give names param1 and param2 to two parameter values passed to the function as follows: func(param1="val1",param2="val2"), instead of passing only values: func(val1,val2). Thus, I feel they should be appropriately called "arbitrary number of named arguments" as we can specify any number of these parameters (that is, arguments) if func has signature func(**kwargs)
So being said that let me explain "named arguments" first and then "arbitrary number of named arguments" kwargs.

Named arguments

named args should follow positional args
order of named args is not important
Example

def function1(param1,param2="arg2",param3="arg3"):
    print("\n"+str(param1)+" "+str(param2)+" "+str(param3)+"\n")

function1(1)                      #1 arg2 arg3   #1 positional arg
function1(param1=1)               #1 arg2 arg3   #1 named arg
function1(1,param2=2)             #1 2 arg3      #1 positional arg, 1 named arg
function1(param1=1,param2=2)      #1 2 arg3      #2 named args       
function1(param2=2, param1=1)     #1 2 arg3      #2 named args out of order
function1(1, param3=3, param2=2)  #1 2 3         #

#function1()                      #invalid: required argument missing
#function1(param2=2,1)            #invalid: SyntaxError: non-keyword arg after keyword arg
#function1(1,param1=11)           #invalid: TypeError: function1() got multiple values for argument 'param1'
#function1(param4=4)              #invalid: TypeError: function1() got an unexpected keyword argument 'param4'
Arbitrary number of named arguments kwargs

Sequence of function parameters:
positional parameters
formal parameter capturing arbitrary number of arguments (prefixed with *)
named formal parameters
formal parameter capturing arbitrary number of named parameters (prefixed with **)
Example

def function2(param1, *tupleParams, param2, param3, **dictionaryParams):
    print("param1: "+ param1)
    print("param2: "+ param2)
    print("param3: "+ param3)
    print("custom tuple params","-"*10)
    for p in tupleParams:
        print(str(p) + ",")
    print("custom named params","-"*10)
    for k,v in dictionaryParams.items():
        print(str(k)+":"+str(v))

function2("arg1",
          "custom param1",
          "custom param2",
          "custom param3",
          param3="arg3",
          param2="arg2", 
          customNamedParam1 = "val1",
          customNamedParam2 = "val2"
          )

# Output
#
#param1: arg1
#param2: arg2
#param3: arg3
#custom tuple params ----------
#custom param1,
#custom param2,
#custom param3,
#custom named params ----------
#customNamedParam2:val2
#customNamedParam1:val1
Passing tuple and dict variables for custom args

To finish it up, let me also note that we can pass

"formal parameter capturing arbitrary number of arguments" as tuple variable and
"formal parameter capturing arbitrary number of named parameters" as dict variable
Thus the same above call can be made as follows:

tupleCustomArgs = ("custom param1", "custom param2", "custom param3")
dictCustomNamedArgs = {"customNamedParam1":"val1", "customNamedParam2":"val2"}

function2("arg1",
      *tupleCustomArgs,    #note *
      param3="arg3",
      param2="arg2", 
      **dictCustomNamedArgs     #note **
      )
Finally note * and ** in function calls above. If we omit them, we may get ill results.

Omitting * in tuple args:

function2("arg1",
      tupleCustomArgs,   #omitting *
      param3="arg3",
      param2="arg2", 
      **dictCustomNamedArgs
      )
prints

param1: arg1
param2: arg2
param3: arg3
custom tuple params ----------
('custom param1', 'custom param2', 'custom param3'),
custom named params ----------
customNamedParam2:val2
customNamedParam1:val1
Above tuple ('custom param1', 'custom param2', 'custom param3') is printed as is.

Omitting dict args:

function2("arg1",
      *tupleCustomArgs,   
      param3="arg3",
      param2="arg2", 
      dictCustomNamedArgs   #omitting **
      )
gives

dictCustomNamedArgs
         ^
SyntaxError: non-keyword arg after keyword arg

import math
print(math.ceil(100.9)) # 101
print(math.floor(100.9)) # 100