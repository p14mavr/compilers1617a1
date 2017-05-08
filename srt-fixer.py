
import sys
import re
import argparse


parser = argparse.ArgumentParser()
# add mandatory (positional) arguments
parser.add_argument("fname",help="input srt file name")
parser.add_argument("offset",type=float,help="subtitle offset in seconds to apply (can be fractional)")

# parse arguments
args = parser.parse_args()

with open(args.fname,newline='') as ifp:	
	for line in ifp:
	
		 
		rexp=re.compile(r'(?P<hours>\d{2}):(?P<minutes>\d{2}):(?P<seconds>\d+,\d+))
		m=rexp.search(line)
		if(m):
			hs=float(m.group(hours))
			ms=float(m.group(minutes))
			ss=float(m.group(seconds))
				
				
			Secondstotal=hs*360+m*60+ss+offset
				
		        sys.stdout.write(Secondstotal)

		else:
				 sys.stdout.write(line)
			


		
		
		
		
		
		
		
		
		
		
		
		
