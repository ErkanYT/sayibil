import random

secsayi = random.randint(1,10)
can = 3

while True:
	
	tahmin = int(input("Sayı Gir: "))
				
	if (tahmin < secsayi):
		print("Girilen Sayıdan Küçük")
		can -= 1
		
	elif (tahmin > secsayi):
		print("Girilen Sayıdan Büyük")
		can -= 1
		
	else:
		print("Tebrikler! Tahmin Sayınız:",secsayi)
		
	if can == 0:
		print("Hakkınız Bitti Sayınız:",secsayi)
		break
