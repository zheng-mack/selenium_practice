"""
    转换网页上复制的cookies（字符串）为集合类型
    eg:('cookies=n')=>({'cookies':'n'})
"""
cookies = str()
cookie = {}
for line in cookies.split(';'):
    key, value = line.split('=', 1)
    cookie[key] = value

print(cookie)
