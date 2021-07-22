passwd = 'a123456'
input()
passwdin = 'a'
input()
count = 3
input()
while passwdin != passwd
    passwdin = input('請輸入密碼?')
    count = count - 1
    print('密碼錯誤 還有', count, '次機會')
print('登入成功')
input()
