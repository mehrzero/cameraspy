import cv2
import time
import os

# تنظیمات شفاف
SAVE_PATH = os.path.join(os.path.expanduser('~'), 'Desktop', 'TEST_LOGS')
os.makedirs(SAVE_PATH, exist_ok=True)

# هشدار به کاربر
print("""
🔔 سیستم تست وبکم فعال شد!
• هر ۵ ثانیه یک عکس گرفته میشود
• عکس‌ها فقط در مسیر زیر ذخیره میشوند:
  {}
• برای خروج کلید Q را فشار دهید
""".format(SAVE_PATH))

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ دسترسی به وبکم امکان‌پذیر نیست")
    exit()

# نمایش چراغ وضعیت
print("🔴 دوربین فعال")
last_capture = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # نمایش تصویر زنده با واترمارک
    cv2.putText(frame, "TEST MODE - VISIBLE", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.imshow('Webcam Test - Press Q to Exit', frame)
    
    # ذخیره زمان‌بندی شده
    if time.time() - last_capture > 5:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        cv2.imwrite(f"{SAVE_PATH}/test_{timestamp}.jpg", frame)
        print(f"📸 Test Capture: test_{timestamp}.jpg")
        last_capture = time.time()
    
    # خروج با کلید Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("✅ تست پایان یافت. تمام فایل‌ها در دسترس هستند.")
