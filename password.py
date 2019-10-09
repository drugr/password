password = '123456'
chance = 3
print('共有3次機會')
while True:
	password_input = input('請輸入密碼: ')
	if password_input == password:
		print('登入成功')
		break
	else:
		if chance == 0:
			print('你不能再輸入了')
			break
		else:
			chance = chance - 1
			if chance > 0:
				print('密碼錯誤，還有', chance , '次機會')
			else:
				print('你不能再輸入了')
				break

