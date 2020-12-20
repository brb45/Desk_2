
def complain_about(substring):
    print('Please talk to me!')
    try:
        while True:
            text = (yield)
            if substring in text:
                print('Oh no: I found a %s again!'
                      % (substring))
    except GeneratorExit:
        print('Ok, ok: I am quitting.')

def coroutine(fn):
     def wrapper(*args, **kwargs):
         c = fn(*args, **kwargs)
         next(c)
         return c
     return wrapper

@coroutine
def complain_about2(substring):
    print('Please talk to me!')
    while True:
        text = (yield)
        if substring in text:
            print('Oh no: I found a %s again!'
                  % (substring))


c = complain_about2('JavaScript')
Please talk to me!
c.send('Test data with JavaScript somewhere in it')
Oh no: I found a JavaScript again!
c.close()

###############################################################
def coroutine(fn):
    def wrapper(*args, **kwargs):
        c = fn(*args, **kwargs)
        next(c)
        return c
    return wrapper


def cat(f, case_insensitive, child):
    if case_insensitive:
        line_processor = lambda l: l.lower()
    else:
        line_processor = lambda l: l

    for line in f:
        child.send(line_processor(line))


@coroutine
def grep(substring, case_insensitive, child):
    if case_insensitive:
        substring = substring.lower()
    while True:
        text = (yield)
        child.send(text.count(substring))


@coroutine
def count(substring):
    n = 0
    try:
        while True:
            n += (yield)
    except GeneratorExit:
        print(substring, n)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', action='store_true',
                        dest='case_insensitive')
    parser.add_argument('pattern', type=str)
    parser.add_argument('infile', type=argparse.FileType('r'))

    args = parser.parse_args()

    cat(args.infile, args.case_insensitive,
        grep(args.pattern, args.case_insensitive,
             count(args.pattern)))


# $ time python3.5 grep.py -i love pg2600.txt
# love 677
# python3.5 grep.py -i love pg2600.txt  0.09s user 0.01s system 97% cpu 0.097 total