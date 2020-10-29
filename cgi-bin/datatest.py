#!/opt/anaconda3/bin/python3.8
# The line above ^ is important. Don't leave it out. It should be at the
# top of the file.

import cgi, cgitb # Not used, but will be needed later.

def judge_type(x):
    if(x=="+"):
        return str(int(form['a'].value)+int(form['b'].value))
    else:
        return str(int(form['a'].value)/int(form['b'].value))

print("Content-type: text/html\n\n")

form = cgi.FieldStorage()
'''if "name" not in form or "addr" not in form:
    print("<H1>Error</H1>")
    print("Please fill in the name and addr fields.")'''
# Output to stdout, CGIHttpServer will take this as response to the client

print("<p>Hello world!</p>")         # Start of content

'''print("<p>Hello world!</p>")         # Start of content
print ("<p>" +  form['a'].value + "</p>")'''

print("<head>")
print("<title>WOW</title>")
print("</head>")
print("<html>")
print("<p>Wow, Python Server</p>")
print('<IMG src="../image/test.jpg"/>')
print('<form name="input" action="cgi-bin/post.py" method="post">')
print('a:<input type="text" name="a" value="')
try:
    print(form['a'].value)
except:
    print()
print('"><br>')


print('b:<input type="text" name="b" value="')
try:
    print(form['b'].value)
except:
    print()
print('"><br>')

print('    res:')
try:
    print(judge_type(form['type'].value))
except:
    print()
print('<br>')

print('<input type="submit" value="Submit">')
print('</form>')




import cgi, cgitb # Not used, but will be needed later.
import pymysql
from twisted.enterprise import adbapi
from twisted.internet import reactor
import cgi, cgitb
class connectDb:
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls):  # 函数名固定，会被scrapy调用，直接可用settings的值
        """
        数据库建立连接
        :param settings: 配置参数
        :return: 实例化参数
        """
        adbparams = dict(
            host="localhost",
            db='Crawler',
            user='root',
            password='Aa123456',
            cursorclass=pymysql.cursors.DictCursor  # 指定cursor类型
        )
        # 连接数据池ConnectionPool，使用pymysql或者Mysqldb连接
        dbpool = adbapi.ConnectionPool('pymysql', **adbparams)
        # 返回实例化参数
        return cls(dbpool)



    def process_item(self, item):
        """
        使用twisted将MySQL插入变成异步执行。通过连接池执行具体的sql操作，返回一个对象
        """
        try:
            query = self.dbpool.runInteraction(self.do_insert,item)  # 指定操作方法和操作数据
        except Exception as e:
            print(e)
        # 添加异常处理
        query.addCallback(self.handle_error)  # 处理异常

    def do_insert(self, cursor, item):
        # 对数据库进行插入操作，并不需要commit，twisted会自动commit
        '''insert_sql = """
        insert into new(title,text,kind,source) VALUES(%s,%s,%s,%s)
                    """'''
        insert_sql = "select * from new where title='{}';".format(item)
        cursor.execute(insert_sql)#, (item['title'], item['text'], item['kind'],item["source"]))
        res=cursor.fetchone()
        return res

    def handle_error(self, failure):
        if failure:
            # 打印错误信息
            print(failure)

id=form['id'].value
a=connectDb.from_settings()
query_res=a.process_item(id)
reactor.callLater(4, reactor.stop)
reactor.run()



print('<form name="dataquery" action="cgi-bin/datatest.py" method="post">')
print('id:<input type="text" name="id"><br>')
print('    res:<br>')
print('<input type="submit" value="Submit">')
print('</form>')

print('</html>')
