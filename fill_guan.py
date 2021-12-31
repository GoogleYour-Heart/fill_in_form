import urllib.request

url="https://www.informationofdum.com/DMU_WEB/student_5/info/?jsonnumber=1120190276&jsonname=%E5%85%B3%E8%90%8C%E8%90%8C&jsonclass=2019%E7%BA%A7%E7%A1%95%E5%A3%AB%E7%A0%94%E7%A9%B6%E7%94%9F%E4%B8%AD%E9%98%9F&morning=36.2%E2%84%83&afternoon=36.2%E2%84%83&night=36.2%E2%84%83&jsonbody=1&jsonbodychangeinfo=&textarea=%E7%BD%91%E7%BB%9C%E4%BF%A1%E6%81%AF%E4%B8%AD%E5%BF%83&textprople=%E5%90%8C%E5%AD%A6&jsontouch=1&jsontouchchangeinfo=0&jsonisolate=1&jsonisolatechangeinfo=0&latitude=39.265530&longitude=121.7796"
req=urllib.request.Request(url)
resp=urllib.request.urlopen(req)
data=resp.read().decode('utf-8')

print(data)
