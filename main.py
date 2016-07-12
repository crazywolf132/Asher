import os
import application

print "Just going to update the system."
os.system('git pull')
#os.system('clear')
reload(application)
print "Will now start the application"

f = application.run()
f.startmain()