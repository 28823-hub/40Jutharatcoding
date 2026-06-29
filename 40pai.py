print("โปรแกรมคำนวณ  Bmi และแปลสุขภาพ\n")
hight = float(input("ส่วนสูงของคุณ m."))
wieght = int(input("นํ้าหนักของคุณ kg."))

total = (hight * hight)
Bmi = (wieght/total)
print("Bmi ของคุณคือ , Bmi , หน่วย")
if Bmi > 19 :
 print("อยู่ในเกณฑ์ปกติ\n")
