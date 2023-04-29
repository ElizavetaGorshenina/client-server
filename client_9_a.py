from subprocess import Popen, CREATE_NEW_CONSOLE


client_read = Popen("python .\client_9_read.py", creationflags=CREATE_NEW_CONSOLE)
client_write = Popen("python .\client_9_write.py", creationflags=CREATE_NEW_CONSOLE)
