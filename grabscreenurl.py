#!/usr/bin/python

import sys, getopt,fileinput, os, urllib2, urllib, cStringIO,argparse

sys.path.append('/usr/local/lib/python2.7/site-packages')

lineFile = 1
version = "0.1.0"
numberLine = 1


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
        
        outNameFile = slugify(line)
	
	#print paramArgs.grabutility 
	#sys.exit(0)

	if  paramArgs.grabutility != None:
		commandLine = paramArgs.grabutility.replace('<url>',line.rstrip())
		commandLine = commandLine.replace('<outfilename>',outNameFile)

		#print 'Line:', commandLine
		os.system(commandLine)
		#print 'Line:', numberLine,'cutycap --javascript=off --insecure --url=',line.rstrip(), '--out=',outNameFile

		
	if  paramArgs.grabutility == None:
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

	helpGrabber = (
		"Call for each line from inputfile "
		"example:"
		"\"webkit2png -o <outfilename> --timeout=2000 <url>\""
	)

	parser.add_argument("-i","--inputfile",action="store", help="Read line by file url from file")
	parser.add_argument("-g","--grabutility",action="store", help=helpGrabber)																	
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

	#args.grabutility = "cutycapt"
	if args.grabutility==None:
		print ' '
		print 'Missing parameter -g. You must specify a grabber utility.'
		print 'example usage:'
		print 'cutycapt --javascript=off --insecure --url=<url> --out=<outfilename>'
		print 'or'
		print 'webkit2png -o <outfilename> --timeout=2000 <url>'
		print ' '
		print 'Run demo mode'


	#convert input from dirsearch tool
	if args.converter !=None and args.converter == "dirsearch":
		print 'Run Convert type DirSearch'	
		with open(args.inputfile,'rs') as f:
			#use same variable
			args.inputfile = 'dir_search_list.txt'	
			with open(args.inputfile,'w') as target:
				for line in iter(f):
					#print line	
					if "\xe2" in line:
							line = repr(line)
					splitLine = line.split(" ")
					if splitLine[0]=='200':
						target.write(splitLine[6])
				target.write('\n') 
					
		print 'Done Convert file output to:',args.inputfile	 				
	#end converter dirsearch
	

		
		
	print ' '
	grab_url_from_file(args)


if __name__ == "__main__":
    main()
