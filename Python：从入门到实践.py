# 第一段
tittle1 = '''定义：字符串是一种数据类型，字符串就是一系列字符。在Python中，用引号括起的都是字符串，其中的引号可以是单引号，也可以是双引号（英文符号）
\n第一章 字符串编辑的“方法”
\n一、首字母大写: 'String'.title()'''
print(tittle1)
print('string'.title())
note = '同理的“方法”：全部字母小字 “string”.lower(), 全部字母大写 “STRING”.upper()'
print(note)
print('字母小写：', 'STRING'.lower())
print('字母大写：', 'string'.upper())

# 第二段
tittle1 = '''\n二、合并字符串：必须加连接符！---'字符1'+ '连接符' + '字符2'
\t(一) 加号：可直接连接单独字符串
格式: 'string1' + '连接符' + 'string2'''''
print(tittle1)
print('例1：', 'string1' + '这是连接符' + 'string2')
tittle2 = '''\t(二) join函数:必须使用列表包裹字符串，不能像+号一样可单独串连
格式: '这是连接符'.join(['string1.1', 'string2.2'])'''
print(tittle2)
print('例2：', '' '这是连接符'.join(['string1.1', 'string2.2']))
print('例2：',  '这是连接符'.join(['string1.1', 'string2.2']))
tittle3 = '''\n注意：加号（+）和逗号（,）在print函数中作用不同。
请看：
\t1.逗号(,)用于打印多个参数,参数之间使用空格分隔:
print('Hello', 'World') 
输出:Hello World
\t2.加号(+)用于拼接字符串,将多个字符串拼接成一个字符串打印出来:
print('Hello' + 'World')  
输出:HelloWorld
\t3.逗号可以打印多种类型的数据，加号只能连接字符串
print('Hello', 123)
输出:Hello 123
print('Hello' + 123) 
错误,不能拼接字符串和整数
\t区别：
用逗号时，python会自动在打印的内容之间添加空格,而加号不会在字符串间添加空格。
逗号的处理对象是：多种类型的数据（数字、字符串），并且自动在多个对象之间加空格；加号的处理对象只能用是字符串，并且不会自动在字符串间添加空格。
'''
print(tittle3)

# 第三段
tittle1 = r'''三、使用制表符和换行符在字符串中增加空白
在编程中，空白泛指任何非打印字符，如空格、制表符和换行符。你可使用空白来组织输出，以使其更易读。
（一）要在字符串中添加制表符，可使用字符组合\t
格式：print(\tPython)
输出：
    Python
（二）要在字符串中添加换行符，可使用字符组合\n；
格式：print(\n贵州省\n毕节市\n威宁县\n草海镇)
输出：
贵州省
毕节市
威宁县
草海镇
（三）示例：
'''
print(tittle1, end='')
print('地址：\n\t贵州省\n\t\t毕节市\n\t\t\t威宁县\n\t\t\t\t草海镇')








