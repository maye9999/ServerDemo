# APIs
-----

文档中列出来的调用地址，均省去了域名信息。如调用接口为:
```
/apis/register
```
实际调用地址应为:
```
http://123.57.50.143/apis/register
```
以此类推。


文档中的参数使用遵守接口标准，采用`Http Get`方式访问，如参数名为`phone`，参数值为`123`，
另有参数名为`passwd`，参数值为`123456789`,则实际调用为（多个参数使用`&`符号连接）:
```
http://123.57.50.143/apis/register?phone=123&passwd=123456789
```


文档中所有返回值均采用标准json数据格式。如返回`text`，则具体返回格式应为：
```
{
  ‘code': '0',
  ‘text':'something'
}
```
目前已经实现的接口如下：

注册 Register
```
http://123.57.50.143/apis/register?username=peter&password=123456789
```
注册失败（重名），返回code=1,注册成功，返回code=0

登陆 Login
```
http://123.57.50.143/apis/login?username=peter&password=123456789
```
用户名密码错误返回code=1，登陆成功返回code=0

登出 Logout
```
http://123.57.50.143/apis/logout
```

查询 Get
```
http://123.57.50.143/apis/get
```
目前返回
```
{
  balance: 19,
  code: 0,
  flow: 12,
  user: "peter"
}
```
flow为流量，balance为余额

设置 Set
```
http://123.57.50.143/apis/set?flow=123&balance=456
```
返回为设置之后的get的json包

注意：Get 和 Set命令必须要求已经登陆，目前采用两种验证方法：
1.Django自带的Cookies和Session验证，登陆后一段时间内调用get和set都会成功，但是似乎要求支持cookies，我在浏览器上测试成功，安卓手机不一定可以成功，不过我查似乎有HttpClient的代码可以实现android的cookies连接

2.(备用)Http Basic Authentication，每一个HTTP GET请求的头中加入auth模块， 其中含有Base64编码的用户名和密码， 具体实现可以google下Basic Authentication的实现

查询所有接受(发出)到的流量
```
http://123.57.50.143/apis/getentriesfrom
http://123.57.50.143/apis/getentriesto
```
返回样例如下

```
{
code: 0,
data: [
{
user to: "john",
user from: "maye",
date: "2015-04-12",
flow: 1024,
time: "04:00:16.970689"
},
{
user to: "tom",
user from: "maye",
date: "2015-04-12",
flow: 11111,
time: "04:10:10.702649"
},
{
user to: "tony",
user from: "maye",
date: "2015-04-12",
flow: 90,
time: "12:13:06.332694"
}
]
}
```

添加新的流量记录
```
http://123.57.50.143/apis/addentry?user_from=USERNAME&user_to=USERNAME&flow=NUM
```


另：APIs所有域名和端口号待定。如有API更新会及时通知

---
## Example Section
### checkin
> * URL
>> * /apis/checkin

> * Parameters
>> * uuid             : phone unique identifier 
>> * info (optional)  : extra infomation

> * Return
>> * text : explaination
>> * code : true if successful, false else

> * Example
>> * url: /apis/register?uuid=ab10e301&info=none
>> * ret: {"text":"Sucessfully Check In","code":true}

### example 2

...

## Example Section 2

