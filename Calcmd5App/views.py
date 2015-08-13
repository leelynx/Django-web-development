# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response, RequestContext
import paramiko
import os
import sys
from paramiko.ssh_exception import SSHException, BadHostKeyException


def GetMd5(request):
    errors = []
    if 'hostname' in  request.POST and 'passwd' in request.POST and 'dirpath' in  request.POST:
	hostname = request.POST.get('hostname')
	username = request.POST.get('username')
	passwd = request.POST.get('passwd')
	dirname = request.POST.get('dirpath')
	rootdir = dirname.encode('utf-8')
	if not hostname and not passwd and not dirname:
	    errors.append('Input value is none.')
	else:
	    try:
		ssh = paramiko.SSHClient()  
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
		ssh.connect(hostname,22,username,passwd,timeout=5)
	    except paramiko.ssh_exception.AuthenticationException, autherror:
		errors.append(autherror)
	    else:
		cmd = "/bin/bash /calcmd5/calcmd5.sh " + rootdir
		stdin, stdout, stderr = ssh.exec_command(cmd)
		messageout = stdout.readlines()
		return render_to_response('getinfo.html', {'messageout': messageout}, context_instance=RequestContext(request))
    return render(request, 'calc_form.html', {'errors': errors, 'hostname': request.POST.get('hostname', ''), 'dirname': request.POST.get('dirpath', '')})