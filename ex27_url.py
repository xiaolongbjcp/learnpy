

from urllib import request, parse

proxy_handler = request.ProxyHandler({'http': 'http://www.baidu.com/'})
opener = request.build_opener(proxy_handler)
with opener.open('http://www.baidu.com/') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    # print('Data:', data.decode('utf-8'))



# from urllib import request

# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))