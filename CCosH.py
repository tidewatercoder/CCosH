import shutil
import os
import hashlib
import zlib
import sys

whoami = os.getlogin()
os.chdir(f'C:/Users/{whoami}/Documents')
hashedlist = []
def hashfile(i,dirlist2,homefile,compressit=''):
    if dirlist2 != homefile:
        if dirlist2 not in os.listdir(f'C:/Users/{whoami}/Documents/BackupDF/{homefile}'):
            os.mkdir(f'C:/Users/{whoami}/Documents/BackupDF/{homefile}/{dirlist2}')
    elif dirlist2 == homefile:
        if dirlist2 not in os.listdir(f'C:/Users/{whoami}/Documents/BackupDF'):
            os.mkdir(f'C:/Users/{whoami}/Documents/BackupDF/{dirlist2}')
    i2 = i.split('.')
    begin, end = i2
    if compressit == 'n':
        if hashit == 'y':
            with open(i, 'rb') as g:
                g2 = g.read()
            # hashed_string = hashlib.sha256(g2.encode('utf-8')).hexdigest()
            hashed_string = hashlib.sha256(g2).hexdigest()
            print('Original',hashed_string)
            g.close()
        if dirlist2 == homefile:
            shutil.copyfile(i, f"C:/Users/{whoami}/Documents/BackupDF/{dirlist2}/{begin}.{end}")
            openfile = f"C:/Users/{whoami}/Documents/BackupDF/{dirlist2}/{begin}.{end}"
        elif dirlist2 != homefile:
            shutil.copyfile(i, f"C:/Users/{whoami}/Documents/BackupDF/{homefile}/{dirlist2}/{begin}.{end}")
            openfile = f"C:/Users/{whoami}/Documents/BackupDF/{homefile}/{dirlist2}/{begin}.{end}"
        if hashit == 'y':
            with open(openfile, 'rb') as x:
                x2 = x.read()
            # hashed_string2 = hashed_string = hashlib.sha256(x2.encode('utf-8')).hexdigest()
            hashed_string2 = hashlib.sha256(x2).hexdigest()
            print('Backup  ',hashed_string2)
            if hashed_string == hashed_string2:
                print('Hashes are the same\n')
                hashedlist.append(f'{begin}.{end} '+hashed_string2)
            x.close()
        with open(f"C:/Users/{whoami}/Documents/BackupDF/{homefile}/Hashedfiles.txt",'w') as hashg:
            hashedlist2 = ''
            for i in hashedlist:
                hashedlist2 += i+'\n'
            hashg.write(hashedlist2)
    elif compressit == 'y':
        if hashit == 'y':
            if dirlist2 == homefile:
                with open(i,'rb') as hashg:
                    hashg2 = hashg.read()
                    hashed_string2 = hashlib.sha256(hashg2).hexdigest()
                    print(hashed_string2)
            elif dirlist2 != homefile:
                with open(i,'rb') as hashg:
                    hashg2 = hashg.read()
                    hashed_string2 = hashlib.sha256(hashg2).hexdigest()
                    print(hashed_string2)
            hashedlist.append(f'{begin}.{end} ' + hashed_string2)
            with open(f"C:/Users/{whoami}/Documents/BackupDF/{homefile}/Hashedfiles.txt", 'w') as hashg:
                hashedlist2 = ''
                for i2 in hashedlist:
                    hashedlist2 += i2 + '\n'
                hashg.write(hashedlist2)
        if dirlist2 == homefile:
            with open(i,'rb') as becomp, open(f"C:/Users/{whoami}/Documents/BackupDF/{dirlist2}/{begin}.{end}",'wb') as compr:
                becomp1 = becomp.read()
                compressed_data = zlib.compress(becomp1, zlib.Z_BEST_COMPRESSION)
                print(f'Original size: {sys.getsizeof(becomp1)}')
                print(f'Compressed size: {sys.getsizeof(compressed_data)}\n')
                compr.write(compressed_data)
        elif dirlist2 != homefile:
            with open(i,'rb') as becomp, open(f"C:/Users/{whoami}/Documents/BackupDF/{homefile}/{dirlist2}/{begin}.{end}",'wb') as compr:
                becomp1 = becomp.read()
                compressed_data = zlib.compress(becomp1, zlib.Z_BEST_COMPRESSION)
                print(f'Original size: {sys.getsizeof(becomp1)}')
                print(f'Compressed size: {sys.getsizeof(compressed_data)}\n')
                compr.write(compressed_data)

def uncompress(i,dirlist2,homefile,hashit):
    while True:
        if dirlist2 == homefile:
            homefile2 = homefile+'uncompressed'
            dirlist22= dirlist2+'uncompressed'
            if dirlist22 not in os.listdir(f"C:/Users/{whoami}/Documents/BackupDF"):
                os.mkdir(f"C:/Users/{whoami}/Documents/BackupDF/{dirlist22}")
        elif dirlist2 != homefile:
            homefile2 = homefile + 'uncompressed'
            dirlist22 = dirlist2 + 'uncompressed'
            if dirlist2 not in os.listdir(f'C:/Users/{whoami}/Documents/BackupDF/{homefile2}'):
                os.mkdir(f'C:/Users/{whoami}/Documents/BackupDF/{homefile2}/{dirlist2}')
        i2 = i.split('.')
        begin, end = i2
        if i == 'Hashedfiles.txt':
            break
        if dirlist2 == homefile:
            with open(i,'rb') as ung, \
                    open(f"C:/Users/{whoami}/Documents/BackupDF/{homefile2}/{begin}.{end}",'wb') as uncompr:
                ung2 = ung.read()
                uncompressed_data = zlib.decompress(ung2)
                uncompr.write(uncompressed_data)
        elif dirlist2 != homefile:
            with open(i, 'rb') as ung, \
                    open(f"C:/Users/{whoami}/Documents/BackupDF/{homefile2}/{dirlist2}/{begin}.{end}",'wb') as uncompr:
                ung2 = ung.read()
                uncompressed_data = zlib.decompress(ung2)
                uncompr.write(uncompressed_data)
        if hashit =='y':
            if dirlist2 == homefile:
                with open(f"C:/Users/{whoami}/Documents/BackupDF/{homefile2}/{begin}.{end}",'rb') as hashg:
                    hashg2 = hashg.read()
                    hashed_string2 = hashlib.sha256(hashg2).hexdigest()
                    print(hashed_string2)
            elif dirlist2 != homefile:
                with open(f"C:/Users/{whoami}/Documents/BackupDF/{homefile2}/{dirlist2}/{begin}.{end}",'rb') as hashg:
                    hashg2 = hashg.read()
                    hashed_string2 = hashlib.sha256(hashg2).hexdigest()
                    print(hashed_string2)
            hashedlist.append(f'{begin}.{end} ' + hashed_string2)
            with open(f"C:/Users/{whoami}/Documents/BackupDF/{homefile2}/Hashedfiles.txt", 'w') as hashg:
                hashedlist2 = ''
                for i2 in hashedlist:
                    hashedlist2 += i2 + '\n'
                hashg.write(hashedlist2)
        break


if 'BackupDF' in os.listdir():
    filestocopy = input('What files do you want to copy?\n'
                        'Note: Please provide path!\n')
    comuncom = input('Would you like to compress or uncompress this file?\n'
                     'If not type no or n!\n').lower()
    hashit = input('Would you like to hash the files? y/n\n')
    if comuncom == 'compress':
        compressit = 'y'
        uncompressit = ''
    elif comuncom == 'uncompress':
        compressit = None
        uncompressit = 'uncompress'
    elif comuncom == 'n' or comuncom == 'no':
        compressit = 'n'
        uncompressit = ''
    filestocopyre = filestocopy.replace('\\','/')
    if os.path.isfile(filestocopyre):
        filestocopy2 = filestocopy.split('\\')
        filestocopy2 = filestocopy2[-1]
        filestocopy2 = filestocopy2.split('.')
        begin,end = filestocopy2
        if hashit == 'y':
            with open(filestocopyre,'r') as g:
                g2 = g.read()
            hashed_string = hashlib.sha256(g2.encode('utf-8')).hexdigest()
            print('Original',hashed_string)
            g.close()
        shutil.copyfile(filestocopyre,f"C:/Users/{whoami}/Documents/BackupDF/{begin}.{end}")
        if hashit == 'y':
            with open(f"C:/Users/{whoami}/Documents/BackupDF/{begin}.{end}",'r') as x:
                x2 = x.read()
            hashed_string2 = hashed_string = hashlib.sha256(x2.encode('utf-8')).hexdigest()
            print('Backup',hashed_string2)
            if hashed_string == hashed_string2:
                print('Hashes are the same')
            x.close()
    elif os.path.isdir(filestocopyre):
        dirlist = []
        dirdir = 0
        len1 = 0
        os.chdir(filestocopyre)
        filestocopyre3 = filestocopyre.split('/')
        filestorage = []
        dirlist2 = filestocopyre3[-1]
        homefile = filestocopyre3[-1]
        while True:
            for i in os.listdir():
                if i in dirlist:
                    dirdir +=1
                    continue
                elif os.path.isdir(i):
                    dirdir = 0
                    dirlist.append(i)
                    os.chdir(i)
                    len1 = len(os.listdir())
                    dirlist2 = i
                    # print(i)
                    break
                elif os.path.isfile(i):
                    if i in filestorage:
                        continue
                    dirdir+=1
                    print(i)
                    filestorage.append(i)
                    if uncompressit != 'uncompress':
                        hashfile(i,dirlist2,homefile,compressit)
                    elif uncompressit == 'uncompress':
                        uncompress(i,dirlist2,homefile,hashit)
            if os.getcwd() == filestocopy:
                break
            elif dirdir == len1:
                os.chdir('..')
                dirdir = 0
                len1 = len(os.listdir())
else:
    os.mkdir('BackupDF')
