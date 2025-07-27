import base64

bs = "你好周杰伦".encode("utf-8")

# 编码
bs64 = base64.b64encode(bs)

print("Base64 Encoded:", bs64)
# Base64 Encoded: b'5L2g5aW95ZGo5p2w5Lym'

# 解码
bs64_decode = base64.b64decode(bs64)
print("Base64 Decoded:", bs64_decode.decode("utf-8"))
# Base64 Decoded: 你好周杰伦
