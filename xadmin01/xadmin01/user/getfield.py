import datetime
import json

from django.db import connection

def getconn(set):
	import pymssql
	# sql服务器名，这里(127.0.0.1)是本地数据库IP
	serverName = '192.168.0.180'
	# 登陆用户名和密码
	userName = 'sa'
	passWord = '$u2930123WJ'
	# 建立连接并获取cursor
	conn = pymssql.connect(serverName, userName, passWord, "KQA")
	cursor = conn.cursor()
	sql1 = "select id  from employee  where id ='方高燕'"
	cursor.execute(sql1)


def gethead(sql):
	cursor=connection.cursor()

	try:
		cursor.execute(sql)
		desc=cursor.description
		meat = []
		for item in desc:
			meat.append(item[0])
		cursor.close()
		connection.close()
		return (meat)
	except:
		pass
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self,obj)

#这个是针对easyui 的dataset返回数据集
def getvalue(sql):
	result={}
	list=[]
	try:
		tas=gethead(sql)
		cursor = connection.cursor()
		cursor.execute(sql)
		rows=cursor.fetchall()
		for row in rows:
			dl = {}
			i=0
			for ta in tas:
				dl[ta]=row[i]
				i=i+1
			list.append(dl)
		result["total"]=16
		result["rows"]=list
		results = json.dumps(result,cls=DateEncoder)
		cursor.close()
		connection.close()
		return results

	except Exception as e:
		raise e
