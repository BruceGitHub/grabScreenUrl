#!/usr/bin/python

import sys, getopt,fileinput, os, urllib2

lineFile = 1
version = "0.1.0"
numberLine = 0

def slugify(value):
    value = value.replace("https", "")
    value = value.replace("http", "")
    value = value.replace("www", "")
    value = value.replace(":", "")
    value = value.replace("/", "")
    value = value.replace(".", "_")
    value = value.replace("\n", "")
    # value = urllib2.quote(value, '')
    return value #add

def grab_url_from_file(paramFilename):
    global numberLine

    print 'Open file:',paramFilename
    url = sys.argv[2]
    f = open(sys.argv[2],'rs')
    for line in iter(f):
        # print (type(line), line)
        if line == '\n': break
        if line == '': break

        if "\xe2" in line:
            line = repr(line)
        
        print 'Grab: %s' % line
        # webkit2png -o test -F https://www.google.it
        outNameFile = slugify(line)
        commandBashScreen = "webkit2png -D output --ignore-ssl-check --timeout 180 -o %s -T %s" % (outNameFile,line.rstrip())

        # print(commandBash)
        os.system(commandBashScreen)
        # numberLine = numberLine +1

    f.close()   
    

def print_menu():
    print '####################'
    print 'Ver: %s,  Dev Bruce, Source: xxx ' % version
    print 'Usage:'
    print 'grabscreeenurl.py -h for this help'
    print 'or'
    print 'grabscreeenurl.py -i list.txt'
    print '####################'

def main():

    if ( len(sys.argv) == 1 ) : 
        print_menu()
        sys.exit(2)


    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:", ["help", "input="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err)  # will print something like "option -a not recognized"
        sys.exit(2)
    for o, a in opts:
        if o in ("-h", "--help"):
            print_menu()
            sys.exit()
        elif o in ("-i", "--input"):
            print '####################'
            print 'Start...'
            grab_url_from_file(a)
        else:
            assert False, "unhandled option"


if __name__ == "__main__":
    main()
