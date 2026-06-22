print("โปแกรมคำนวณคะแนนแต่ละวิชา \n ")
mathematics= int(input("คะแนนวิชาคณิตศาสตร์") )
science= int(input("คะแนนวิชาวิทยาศาสตร์") )
thai= int(input("คะแนนวิชาภาษาไทย") )
total_point = (science + mathematics + thai)
averge = total_point /3
if averge <60:
    print("ดีเยี่ยม")
elif averge <80:
    print("ดีมาก")
elif averge <40:
    print("ผ่าน")
print("by pai 4/4" )
print("thank you")

     
   
