'''
題目：密碼保衛戰
輸入密碼，長度 < 8 拋出自訂例外 `WeakPasswordException`，
加上 EOF 與 finally 處理。
'''


class WeakPasswordException(Exception):

    def __init__(self, pwd, length):
        super().__init__(pwd)
        self.pwd = pwd
        self.length = length

try:
    pwd = input("請輸入密碼: ")

    if len(pwd) < 8:
        raise WeakPasswordException(pwd, len(pwd))

except WeakPasswordException as e:
    print("密碼長度不足 8 個字元")
    print("輸入的密碼為:", e.pwd)
    print("密碼長度為:", e.length)

except EOFError:
    print("輸入EOF，請重新輸入")

else:
    print("輸入密碼為:", pwd)

finally:
    print("請妥善保管密碼")

