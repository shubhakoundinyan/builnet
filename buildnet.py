#! /usr/bin/python

from mininet.cli import CLI
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.log import lg, info, setLogLevel
from mininet.node import Node
from mininet.topo import Topo
from threading import Thread
import random
from multiprocessing.pool import ThreadPool
import Queue

"""
queue = Queue.Queue()
queue1 = Queue.Queue()
queue2 = Queue.Queue()

def threaded_function(arg):
		i = random.randint(1, (arg))
		print "I::"+str(i)
		queue.put(i)
		return '1'+str(i)
"""		
		
class Host1(Topo):
	
	def __init__(self, h, sw, **opts):
		self.sw = sw
		self.h = h
		Topo.__init__(self)		
		lastSwitch = None
		
		for j in range(1, (sw+1)):
			for i in range(1,(h+1)):
			#for j in range(1,sw):
				#print "i:"+str(i)+"j:"+str(j)
				switch = self.addSwitch('s%s'%j)
				
				host = self.addHost('h%s'%i)
				#print "Host:"+host
				#queue1.put(host)	
				self.addLink(host, switch)
				#self.delLink(host, switch)
			if lastSwitch :
					self.addLink(switch, lastSwitch)
			lastSwitch = switch
			#queue2.put(switch)
							
	#def delLink( self, src, dst):
	#	dst.delete()
	#	src.delete()

def run():
	a = raw_input("Enter the number of hosts:")
	b = raw_input("Enter the number of switches:")
	print "Host:"+a+"Switches:"+b
	topo = Host1(h = int(a), sw=int(b))
	net = Mininet(topo)
	#c = RemoteController('c', '0.0.0.0', 6633)
	#net.addController(c)
	#pool = ThreadPool(processes = 1)
	#async_result = pool.apply_async(threaded_function(5))
	#return_val = async_result.get()
	#thread = Thread(target = threaded_function, args=(5,))
 	#thread.start()
	#print "Queue Length:"+str(queue.qsize())
	#i  = queue.get()
	#print "i:"+str(i)
	#j = queue1.get()
	#print "Queue1 length:"+str(queue1.qsize())
	#k = queue2.get()
	#r = []
	#for h in range(queue1.qsize()):
	#	l = queue1.get()
		#r = list(l)
	#	k_r = r.append(l)
		#print "k_r:"+str(k_r)		
		#print "Queue2 length:"+str((queue1.qsize()+1)/(queue2.qsize()+1))+"queue2:"+str(h)
	#t = list(set(r))
	#print "r:"+str(t)
	net.start()
	#h3 = net.addHost('h3')
	#print eval(r[1]).cmd('link s2 down')
	#delLink(s1-eth0, h1-eth0)
	net.pingAll()
	#print "r[1]:"+str(r[1])
	CLI(net)
	net.stop()

if __name__ == '__main__':
	setLogLevel('info')
	run()
	 

