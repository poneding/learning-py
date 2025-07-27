from urllib.parse import urlencode

url = "http://example.com/path/to/resource"
params = {"key1": "你好", "key2": "中国"}

en_result = urlencode(params)  #
print("Encoded URL parameters:", en_result)
# Encoded URL parameters: key1=%E4%BD%A0%E5%A5%BD&key2=%E4%B8%AD%E5%9B%BD
