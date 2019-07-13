country = input('請問你是哪國人: ')
age = input('請輸入年齡: ')
if country == '台灣':
	if int(age) >= 18:
		print('你可以考駕照')
	else:
		print('你不能考駕照喔')
elif country == '美國':
	if int(age) >= 16:
		print('你可以考駕照')
	else:
		print('你不能考駕照喔')
else:
	print('只能輸入台灣或美國哦')