#__*__ coding:utf-8 __*__

from django.shortcuts import render
from django.shortcuts import render_to_response
from calcmd5_app.models import StorageMd5
from django.db import models
import os
import os.path
import sys 
import hashlib
import time
import django

def GetDir(request):
    return render(request, 'putdir.html')

def CalcMd5(request):
    rootdir = request.GET.get('dirpath')
    rootdir = str(rootdir).replace('\\', '/')
    wdir = os.getcwd().replace('\\', '/')
    fname = rootdir.split('/')[-1]
    nowtime = time.strftime('%Y-%m-%d-%H-%M',time.localtime(time.time()))
    resname = wdir + "/" + fname + "-" + nowtime + ".num"  
    if os.path.isdir(rootdir) and os.path.exists(rootdir):
        for parent,dirnames,filenames in os.walk(rootdir):
            for filename in filenames:
                fileres = os.path.join(parent, filename).replace('\\', '/')
                f = open(resname, 'a+')
                f.write(fileres)
                f.write('\n')   
        f.close()
    else:
        sys.exit(1)   
    files = open(resname,'r')
    md5check = []
    md5change = []
    for md5files in files:
        md5file =md5files.strip()
        if not os.path.isfile(md5file):
            sys.exit(2)
        md5str = hashlib.md5()
        fm = file(md5file, 'rb')
        md5str.update(fm.read())
        md5sum = md5str.hexdigest()
        django.setup()
        repeatmd5 = StorageMd5.objects.filter(filename=md5file)
        checknum = StorageMd5.objects.filter(filename=md5file, md5num=md5sum)
        if len(repeatmd5) >= 2:
            deletemd5 = StorageMd5.objects.filter(filename=md5file).delete() 
        elif len(checknum) == 0:
            insertmd5 = StorageMd5.objects.create(filename=md5file, md5num=md5sum) 
            md5create = "File: %s | Md5: %s is Generated" % (md5file, md5sum)
            md5change.append(md5create)
    
        else:
            md5checknum = "Files:%20s | Md5:%-50s is not changed!" % (md5file, md5sum)
            md5check.append(md5checknum)

    files.close()
    os.remove(resname)
    return render(request, 'calcmd5.html', {'md5check': md5check, 'md5change':md5change})



