driving = input("請問你是否有去考過駕照? ")
if driving !='有' and driving !='沒有':
	print('只能輸入有/沒有')
	raise SystemExit
	
age = input("請問你的年齡是? ")
age = int(age)
if driving == '有':
	if age >= 18:
		print("不錯唷!")
	else:
		print('奇怪，你怎麼會有駕照?!')
elif driving == '沒有':
	if age >= 18:
		print('你可以去考考看喔!')
	else:
		print('很好!再過幾年就可以去考了!')