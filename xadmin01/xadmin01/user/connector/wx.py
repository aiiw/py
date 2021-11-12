from fastapi import FastAPI,Request,Response
import hashlib
from pydantic import BaseModel
import uvicorn

from django.http import HttpResponse
from django.shortcuts import render
import requests,json
from urllib.parse import  quote,unquote
from bs4 import BeautifulSoup
import re

def mywx(request):
	try:
		if len(request.get('signature')) == 0:
				return "hello, this is handle view"
		signature = request.get('signature')
		timestamp = request.get('timestamp')
		nonce = request.get('nonce')
		echostr =request.get('echostr')
		token = "alidongxing" #请按照公众平台官网\基本配置中信息填写
		
		list = [token, timestamp, nonce]
		print(list)
		list.sort()
		print(list)
		sha1 = hashlib.sha1()
		

		sha1.update(list[0].encode('utf-8'))
		sha1.update(list[1].encode('utf-8'))
		sha1.update(list[2].encode('utf-8'))


		# print(list(map(sha1.update, list))
		hashcode = sha1.hexdigest()
		print("handle/GET func: hashcode, signature: ", hashcode, signature)

		if hashcode == signature:
			return Response(content=echostr, media_type="text/plain;charset=iso-8859-1")
			# return echostr
		else:

			return "11111"+signature+"--"+hashcode
	except Exception:
			return "如上有语法错误了"
	