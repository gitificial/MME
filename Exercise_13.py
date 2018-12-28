# -*- coding: utf-8 -*-
from __future__ import division

import time

rf = 0
while(rf <= 20):
	y = -1000
	x = 1
	
	while(y <= 0.2):
    		y = x - (5 
+                        	          (x-1)/5 
+                               ((x-1) - ((x-1)/5) -1)/5 
+                    (((x-2) - (((x-1) - ((x-1)/5) -1)/5) -1)/5) 
+          (((x-3) - (((x-2) - (((x-1) - ((x-1)/5) -1)/5) -1)/5) -1)/5) 
+(((x-4) - (((x-3) - (((x-2) - (((x-1) - ((x-1)/5) -1)/5) -1)/5) -1)/5) -1)/5) 
+ (rf * 5) )

		#print(y)		
		if(y == 0):    	
			print(x)
    		#time.sleep(0.01)
    		x += 1
	rf += 1
