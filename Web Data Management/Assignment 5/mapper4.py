#!/usr/bin/env python
#Student Name: Sneha Chitre
#student id: 1001244953

import sys,os,math

#o','are','as','at','be','because','been','but','by','can','cannot','could','dear','did','do','does','either','else','ever','every','for','from','get','got','had','has','have','he','her','hers','him','his','how','however','i','if','in','into','is','it','its','just','least','let','like','likely','may','me','might','most','must','my','neither','no','nor','not','of','off','often','on','only','or','other','our','own','rather','said','say','says','she','should','since','so','some','than','that','the','their','them','then','there','these','they','this','tis','to','too','twas','us','wants','was','we','were','what','when','where','which','while','who','whom','why','will','with','would','yet','you','your']
#with open("stopwords.txt",'rb') as f:
 #   for line in f:
  #      stopwords.append(line.strip().split(','))
#for w in stopwords:
 #   print w
#print "\n\n\n\n\n\n\n\n"
# input comes from STDIN (standard input)


for line in sys.stdin:
    #filename=os.environ["map.input.file"]
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    # words = line.split()
    # increase counters
    wordfile,value= line.split('\t',1)
    
    
	#for c in count:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
	#filepath = os.environ["map_input_file"]
        #filename = os.path.split(filepath)[-1]
        #try:
#  	input_file = os.environ['mapreduce_map_input_file']
	#except KeyError:
    value=value.split('&')
    n=float(value[0])
    N=float(value[1])
    m=float(value[2])
    #D = number of input files
    D=float(10)
    #print input_file
    TFIDF=(n/N)*math.log10(D/m)
	
    
    print '%s\t%s' % (wordfile,TFIDF)
	
	
    
