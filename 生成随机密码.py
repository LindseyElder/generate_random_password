import random
import hashlib

# 获取用户提供的种子字符串
user_seed = input("请输入种子：")

# 使用SHA-512算法计算种子的哈希值，并将其作为随机数生成器的种子值
random.seed(hashlib.sha512(user_seed.encode()).digest())

# 定义密码生成函数
def generate_password(length):
    # 密码字符集
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*"
    # 从字符集中随机选择指定长度的字符，并将它们连接起来生成密码
    password = "".join(random.choice(chars) for _ in range(length))
    return password

# 生成1个长度为20的随机密码
for i in range(1):
    password = generate_password(20)
    print(password)



