import os
import datetime
# import pandas as pd

perm_dict={'0':'---',
  '1':'--x',
  '2':'-w-',
  '3': '-wx',
  '4':'r--',
  '5': 'r-x',
   '6':'rw-',
   '7':'rwx'}

def get_file_atr(path   ):
    atr=os.stat(path)
    atr_={}
    #print (atr)
    mydt=datetime.datetime.fromtimestamp( atr.st_mtime)
    isdir=os.path.isdir(path)

    atr_['modify_time']=mydt.strftime('%Y-%m-%d %H:%M:%S')
    atr_['is_dir']=isdir
    atr_['name']=os.path.basename(path)
    size=atr.st_size
    if atr.st_size>1024 and atr.st_size <1024*1024:
        size='{:10.1f} KB'.format(atr.st_size/1024)

    elif atr.st_size>1024*1024:
        size='{:10.1f} Mb'.format(atr.st_size/(1024*1024))
    else:
        size=str(atr.st_size) +' bytes'
    atr_['size_str']=str(size)


    #print(type(isdir) )
    if isdir:
        isdir_str='d'
        atr_['size_str']=str(size)
    else:
        isdir_str='-'
    perm=''
    for item in oct(atr.st_mode)[-3:]:
        perm=perm+perm_dict[item]
    #print (isdir_str,perm)
    atr_['permiss']=isdir_str+perm
    return atr_
def get_files(base_dir):
#base_dir='/home/jovyan/'
    f=os.listdir(base_dir)
    files=[]
    dirs=[]
    for item in f:
        file=get_file_atr (base_dir+item)
        files.append(file)
        # if file['is_dir']:
        #     dirs.append(file)
        # else:
        #     files.append(file)


    # dirs.extend(files)
    # df =df=pd.DataFrame(files)
    # rec=df.sort_values(['is_dir', 'name'],      ascending = [False, True]).to_dict('records')
    return "rec"
