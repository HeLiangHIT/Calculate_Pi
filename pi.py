#!/usr/bin/env python
"""
Author:Urinx
"""
import sys

class Operator():
	"""Operator have 2 method:
		1.add
		2.mul_div
	"""

	def add(self,a,b,n):
		f=0
		for i in xrange(n-1,-1,-1):
			a[i]+=b[i]+f
			if a[i]>=10:
				a[i]-=10
				f=1
			else:
				f=0

	def mul_div(self,a,b,c,n):
		f=0
		for i in xrange(n-1,-1,-1):
			d=a[i]*b+f
			a[i]=d%10
			f=d/10
		f=0
		for i in xrange(0,n):
			d=a[i]+f*10
			a[i]=d/c
			f=d%c
		

class Pi(Operator):
	n=0
	N=0
	pi=[]
	temp=[]

	def __init__(self, n=100):
		self.N=n+1
		n=int(round(3.4*n))
		self.n = n
		self.pi=[0 for x in xrange(0,n)]
		self.temp=[0 for x in xrange(0,n)]
		self.pi[0]=2
		self.temp[0]=2

	
	def calculate(self):
		for i in xrange(1,self.n):
			self.mul_div(self.temp,i,2*i+1,self.n)
			self.add(self.pi,self.temp,self.n)
		return self.pi[:self.N]

class Output():
	def HelpPrint(self):
		print
		print 'Usage: ./pi.py [OPTION] [NUM]'
		print 'Calculate the Pi number'
		print
		print 'Mandatory arguments to long options are mandatory for short options too.'
		print """\
-a --all get all the numbers of Pi(e.g., -a 200)
-o --one get only one number of Pi(e.g., -o 521)
-r --range get range of Pi(e.g., -r 250:521)
-h --help display this help and exit
--version output version information and exit

Report Pi bugs to 1336006643@qq.com
GNU coreutils home page: <http://www.gnu.org/software/coreutils/>
General help using GNU software: <http://www.gnu.org/gethelp/>
For complete documentation, visit <http://git.oschina.net/urinx/>
"""

	def PiPrint(self):
		print '-------------------------'
		print '|-------Uri\'s Pi--------|'
		print '-------------------------'
		print '|                       |'
		print '|3.',
		for i in xrange(1,len(pi)):
			if i%10:
				print pi[i],
			else:
				print pi[i],'|'
				print '|  ',
		print
		print '-------------------------'
		


if len(sys.argv)>1:
	if sys.argv[1].startswith('-h') | sys.argv[1].startswith('--help'):
		Output().HelpPrint()
	elif sys.argv[1].startswith('--version'):
		print 'Version:1.0.1'
	elif sys.argv[1].startswith('-a') | sys.argv[1].startswith('-all'):
		pi=Pi(int(sys.argv[2])).calculate()
		Output().PiPrint()
	elif sys.argv[1].startswith('-o') | sys.argv[1].startswith('-one'):
		pi=Pi(int(sys.argv[2])).calculate()
		print pi[int(sys.argv[2])]
	elif sys.argv[1].startswith('-r') | sys.argv[1].startswith('-range'):
		pi=Pi(int(sys.argv[2][2])+1).calculate()
		print pi[int(sys.argv[2][0]):int(sys.argv[2][2:])+1]
	else:
		print 'Unknown option!'
		sys.exit()
else:
	pi=Pi().calculate()
	Output().PiPrint()