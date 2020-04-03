#!/usr/bin/python

import string
import keyword
import sys

alphas=string.letters+'_'
nums=string.letters+'_'+string.digits
def CheckID(s):
        if s[0] in alphas:
                if len(s)==1:
                        print "The ID is valid"
                        if s in keyword.kwlist:
                                print "And the ID is a key word"
                else:
                        for j in s[1:]:
                                if j not in nums:
                                        print "The other symbol is invalid."
                                        sys.exit()
                        print "The ID is valid."
                        if s in keyword.kwlist:
                                print "And the ID is a key word"
        else:
                print "The startwith is invalid."




if __name__=="__main__":
        sid=raw_input("Enter a string:")
        CheckID(sid)
