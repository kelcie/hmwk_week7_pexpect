pexpect.run("date") #pexpect captures print output
pexpect.run("ls -l")
print pexpect.run("ls -l")
results = pexpect.run("ls -l") 

results.splitlines()[2] 

prim_run_1 = pexpect.run("mb primates.nex")

 for line in prim_run_1.splitlines(): 
    line = line.lstrip()
    if line.startswith("Analysis") or line.startswith("Likelihood of"):
        print line
   ....:         
Analysis completed in 12 seconds
Analysis used 12.02 seconds of CPU time
Likelihood of best state for "cold" chain of run 1 was -6288.82
Likelihood of best state for "cold" chain of run 2 was -6288.55

##### WORKING WITH SUBPROCCESSES 
import pexpect

newprimates = open("primates2.nex", "w")

In [27]: oldprimates = open("primates.nex").read()

In [28]: corrected = oldprimates.replace("mcmc", "mcmcp")

In [29]: newprimates.write(corrected)

In [30]: newprimates.close

#### PART 1

child = pexpect.spawn("mb -i primates2.nex") #-i tells mrbayes to run in interactive mode
#send the string "mcmc" to the process. This tells mrbayes to start running. The \r is carriage

In [32]: child.sendline(r"mcmc") # tells mrbayes to stop the analysis (do not continue)
Out[32]: 5

In [33]: child.sendline("no")
Out[33]: 3

In [34]: child.expect("MrBayes >")  # wait for the mrbayes prompt.
Out[34]: 0

In [35]: print child.before # child.before shows all of the screen output
##now add a line to tell mrbayes to quit ("quit")

child.sendline("quit")

#################### PART 2 
#spawn an interactive mrbayes process
child = pexpect.spawn("mb -i primates2.nex")
 
#send the command "execute primates2.nex" to mrbayes
child.sendline("execute primates2.nex")
#Out[47]: 22

#send the sumt command to mrbayes
child.sendline("sumt") 
#Out[48]: 5

#check to see that the mrbayes command prompt is returned
child.expect("MrBayes >") 
#Out[49]: 0

#print everything before the mrbayes prompt
print child.before 

#send the sump command
child.sendline("sump")

#Quit MrBayes
child.sendline("quit")

################  PART THREE: WRITE A FUNCTION

#! /usr/bin/python

from __future__ import division

import pexpect
import glob

#interactively starting MrBayes

def function(nexus, numgen = 1100):
   offspring = pexpect.spawn("mb -i %s" %(nexus))   #offspring could be any type of word. Same as child below
   #%s refers to a string- file names apply; %d refers to the digit #
   offspring.sendline("set nowarn = yes")
   offspring.sendline("mcmcp ngen = %d" %(numgen))
   offspring.sendline("mcmc")
   offspring.sendline("no")
   offspring.sendline("quit")


def functionB(nexusb):
   child = pexpect.spawn("mb -i %s" %(nexusb))
   child.sendline("execute %s" %(nexusb))
   child.sendline("sumt")
   child.sendline("sump")
   child.sendline("quit")


allfiles =glob.glob('*')
tfiles =glob.glob('*.t')

### TAKE A SECOND FILE THAT RUNS SUMP AND SUMT

print("there are " + str(len(allfiles)) + "total files in the current directory and " + str(len(tfiles)) + " files that end in '.t'")
#print("there are " + %d + "total files in the current directory and " + %d + " files that end in '.t'")
#followed by %(len(all files), len(tfiles))


function("primates2.nex")
functionB("primates2.nex")

allfiles2 =glob.glob('*')
tfiles2 =glob.glob('*.t')

print("there are " + str(len(allfiles2)) + "total files in the current directory and " + str(len(tfiles2)) + " files that end in '.t'")
print ("these files end in '.t': " + str(tfiles2))