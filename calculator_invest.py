bank = int(input("Укажите ваш бюджет: "));
pay = int(input("Укажите периодические инвестиции: "));
percent = float(input("Укажите процентную ставку: ")) / 100;
period = int(input("Укажите сроки: "));
work = input('Укажите вид вложений "вклад для учебы", "инвестиции", "вклад в банке": ')

all_per = [bank, pay, percent, period, work];
print(all_per);
print()

if work == "инвестиции":
	for i in range(1, period+1):
		bank = bank * percent + bank
		print(i, bank)
		bank = bank + pay

elif work == "вклад для учебы":
	percent = percent / 12
	period = period * 12
	for i in range(1, period+1):
		if i % 6 == 0:
			bank = bank  - 44000
		bank = bank * percent + bank
		print(i, "%.2f" % bank)
#		if i % 6 == 0 and i < 18:
#			bank = bank + pay
		
elif work == "вклад в банке":
	percent = percent / 12
	period = period * 12
	for i in range(1, period+1):
		bank = bank * percent + bank
		print(i, bank)
		
		
print()
print(int(bank))