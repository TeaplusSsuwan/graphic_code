#---------------------------------------------------------------------------#

def draw_pyramid():
  # เลือกค่าพารามิเตอร์จากผู้ใช้ภายในฟังก์ชัน
  type = input("เลือกขนาดที่ต้องการจะวาด \n     1 : เล็ก \n     2 : กลาง \n     3 : ใหญ่ \n"+ ("-"*20) +"\n  กรอกหมายเลขขนาดที่ต้องการจะวาด : ")
  print('-'*30)
  if type == "1":
    num_stars = 3
  elif type == "2":
    num_stars = 5
  elif type == "3":
    num_stars = 7
  else:
    print("ตัวเลือกไม่ถูกต้อง")
    num_stars = 0

  # วาดรูปพีรมิด
  for i in range(num_stars):
    print(" " * (num_stars - i - 1) + "*" * (2 * i + 1))


def draw_invert_pyramid():
  # เลือกค่าพารามิเตอร์จากผู้ใช้ภายในฟังก์ชัน
  type = input("เลือกขนาดที่ต้องการจะวาด \n     1 : เล็ก \n     2 : กลาง \n     3 : ใหญ่ \n"+ ("-"*20) +"\n  กรอกหมายเลขขนาดที่ต้องการจะวาด : ")
  print('-'*30)
  if type == "1":
    num_stars = 3
  elif type == "2":
    num_stars = 5
  elif type == "3":
    num_stars = 7
  else:
    print("ตัวเลือกไม่ถูกต้อง")
    num_stars = 0

  # วาดรูปพีรมิดกลับด้าน
  for i in range(num_stars):
    print(" " * i + "*" * (num_stars * 2 - 2 * i - 1))


def draw_triangle():
  # เลือกค่าพารามิเตอร์จากผู้ใช้ภายในฟังก์ชัน
  type = input("เลือกขนาดที่ต้องการจะวาด \n     1 : เล็ก \n     2 : กลาง \n     3 : ใหญ่ \n"+ ("-"*20) +"\n  กรอกหมายเลขขนาดที่ต้องการจะวาด : ")
  print('-'*30)
  if type == "1":
    num_stars = 3
  elif type == "2":
    num_stars = 5
  elif type == "3":
    num_stars = 7
  else:
    print("ตัวเลือกไม่ถูกต้อง")
    num_stars = 0

  # วาดรูปสามเหลื่ยม
  for i in range(num_stars):
    print( "*" * (num_stars - i))


#---------------------------------------------------------------------------#

def main():
  while True:
    print('-'*30)
    print("โปรแกรมวาดภาพ")
    print('-'*30)
    # รับค่าพารามิเตอร์จากผู้ใช้เพื่อเลือกประเภทภาพที่ต้องการจะวาด
    type = input("เลือกประเภทภาพที่ต้องการจะวาด \n     1 : พีรมิด \n     2 : พีรมิดกลับด้าน \n     3 : สามเหลื่ยม \n"+ ("-"*20) +"\n  กรอกหมายเลขของประเภทรูปภาพ : ")
    print('-'*30)
    if type == "1":
        draw_pyramid()
    elif type == "2":
        draw_invert_pyramid()
    elif type == "3":
        draw_triangle()
    else:
        print("ตัวเลือกไม่ถูกต้อง")
     
    # ตรวจสอบว่าผู้ใช้ต้องการออกหรือไม่
    choice = input("ต้องการออกหรือไม่ (y/n): ")
    if choice.lower() == "y":
      break
    elif choice.lower() == "n":
      continue
    else:
      print("ตัวเลือกไม่ถูกต้อง")

  print("--- โปรแกรมเสร็จสิ้นการทำงาน ---")
  print('-'*30)
if __name__ == "__main__":
  main()

  #---------------------------------------------------------------------------#