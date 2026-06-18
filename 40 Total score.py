point1 = float(input("คะแนนวิชาที่1:"))
point2 = float(input("คะแนนวิชาที่2:"))
point3 = float(input("คะแนนวิชาที่3:"))
total_point =(point1 + point2 + point3)
average = total_point/3
if average < 60:
   print ("คะแนนรวมของคุณ = " , total_point)
   print ("คะแนนเฉลี่ย  3 วิชา = ", average)
   print ("ควรปรับปรุง")
elif average < 80:
   print ("คะแนนรวมของคุณ = " , total_point)
   print ("คะแนนเฉลี่ย  3 วิชา = ", average)
   print("ผ่าน")   
else:
    print ("คะแนนรวมของคุณ = " , total_point)
    print ("คะแนนเฉลี่ย  3 วิชา = ", average)
    print("ดีเยี่ยม")