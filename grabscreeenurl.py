#!/usr/bin/python

import sys, getopt,fileinput, os, urllib2, urllib, cStringIO,argparse
from cv2.cv import *
from selenium import webdriver

sys.path.append('/usr/local/lib/python2.7/site-packages')

lineFile = 1
version = "0.1.0"
numberLine = 1
paramGrabUtility = ""


def slugify(value):
    value = value.replace("https", "")
    value = value.replace("http", "")
    value = value.replace("www", "")
    value = value.replace(":", "")
    value = value.replace("/", "")
    value = value.replace(".", "_")
    value = value.replace("\n", "")
    value = value + ".jpg"
    # value = urllib2.quote(value, '')
    	
    return value #add

def grab_url_from_file(paramArgs):
    global numberLine
    global paramGrabUtility

	
    print 'Open file:',paramArgs.inputfile
    print 'Converter type:',paramArgs.converter
    
    f = open(paramArgs.inputfile,'rs')
    for line in iter(f):
        # print (type(line), line)
        if line == '\n': break
        if line == '': break

        if "\xe2" in line:
            line = repr(line)
        
        # print 'Grab: %s' % line
        # webkit2png -o test -F https://www.google.it
        outNameFile = slugify(line)
        
	#commandBashScreen = "webkit2png -D output --ignore-ssl-check --timeout 180 -o %s -T %s" % (outNameFile,line.rstrip())
		

	if  paramGrabUtility == "":
		print 'Line:', numberLine, ' - DemoUtility -o', outNameFile, '-u',line.rstrip()
	
	numberLine = numberLine +1

    f.close()   
    

def print_menu():
    print '####################'
    print '#'
    print '# Ver: %s,  Dev: BruceGitHub  ' % version
    print '#'
    print '# Type -h or --help for help'
    print '####################'
    print ' '

def main():
	print_menu()
	parser = argparse.ArgumentParser()

	parser.add_argument("-i","--inputfile",action="store", help="Read line by file url from file")
	parser.add_argument("-g","--grabutility",action="store", help="Call for each line with parameter OutFileName and Url")
	parser.add_argument("-c","--converter",action="store", help="Select source to convert file [dirsearch].")

	args = parser.parse_args()

	if len(sys.argv) <=1: 
		sys.exit(1)

	if args.inputfile==None and args.converter==None:
		print 'Missing parameter -i and Missing parameter -c. You must specify parameter -i or -c'
		sys.exit(1)

	if args.inputfile==None:
		print 'Missing parameter -i.  You must specify inputfile'
		sys.exit(1)

	#if args.inputfile!=None and args.converter!=None:
	#	print 'Conflict. You must specify parameter -i or -c'
	#	sys.exit(1)

	if args.grabutility==None:
		paramGrabUtility= ""
		print ' '
		print 'Missing parameter -g. You must specify a grabber. The grabber is utility (i.e webkit2png or OpenCV) to pass parameter OutFileName and Url'
		print 'Run demo mode!!!'

	#convert input from dirsearch tool
	if args.converter !=None and args.converter == "dirsearch":
		print 'Run Convert type DirSearch'	
		f = open(args.inputfile,'rs')

		#use same variable
 		args.inputfile = 'dir_search_list.txt'	
		target = open(args.inputfile,'w')

		for line in iter(f):
			#print line	
			if "\xe2" in line:
           			line = repr(line)
			splitLine = line.split(" ")
			if splitLine[0]=='200':
				target.write(splitLine[6])
		target.write('\n') 
				
		f.close()   				
		target.close()
	#end converter dirsearch
	

		
		
	print ' '
	grab_url_from_file(args)


if __name__ == "__main__":
    main()
