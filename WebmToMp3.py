import os, threading, time

BashBlacklist = [' ' , '(' , ')' , '[' , ']' , "'"]

def ReplaceCharacters(blacklist, subject):
    for character in blacklist:
        subject = subject.replace(str(character), '\\' + character)
    return subject

def converter(File):
    os.system('ffmpeg -loglevel 16 -i ' + Path + File + ' ' + Path + File.replace('.webm', '.mp3'))

Path = input('where are the files you want to convert? ')
FileList = os.listdir(Path)
#Path = FileList[0]
#print(Path)
#counter = 1
#for character in range(len(Path)):
#    CurrentStringIndex = len(Path) - counter
#    print(character)
#    if Path[CurrentStringIndex] == "/":
#        BasePath = command[:(CurrentStringIndex)]
#        break
#    counter = counter + 1
    
#FileList = os.listdir('/home/cat/Music')
FileListRefined = []
for File in FileList:
    File = ReplaceCharacters(BashBlacklist, File)
    if File.endswith('.webm'):
        FileListRefined.append(File)

threads = []
for File in FileListRefined:
    thread = threading.Thread(target=converter, name=File.replace(' ',''), args=(File,))
    thread.start()

while threading.active_count() > 0: #One will always be running cause thats the one you are running on
    if threading.active_count() == 1:
        print("\n Finished, quitting...")
        quit()
    elif threading.active_count() < 6:
        for thread in threading.enumerate():
            if thread.name != 'MainThread':
                print("Remaining Thread " + str(thread.name), end='\r')
    else:
        print("Remaining threads: " + str(threading.active_count() - 1), end='\r')
    time.sleep(5)
