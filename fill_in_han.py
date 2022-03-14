import urllib.request

url="
https://www.informationofdum.com/DMU_WEB/student_5/info/?jsonnumber=1120191283&jsonname=%E9%9F%A9%E7%8E%89%E9%9B%AA&jsonclass=2019%E7%BA%A7%E7%A1%95%E5%A3%AB%E7%A0%94%E7%A9%B6%E7%94%9F%E4%B8%AD%E9%98%9F&morning=36.2%E2%84%83&afternoon=36.2%E2%84%83&night=36.2%E2%84%83&jsonbody=1&jsonbodychangeinfo=&textarea=%E5%AF%9D%E5%AE%A4&textprople=%E5%90%8C%E5%AD%A6&jsontouch=1&jsontouchchangeinfo=0&jsonisolate=1&jsonisolatechangeinfo=0&latitude=38.870710192743374&longitude=121.5242078467827%20HTTP/1.1"
req=urllib.request.Request(url)
resp=urllib.request.urlopen(req)
data=resp.read().decode('utf-8')

print(data)
