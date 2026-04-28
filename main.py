import subprocess
import sys
import os

def run():
    # تعديل file إلى __file__ للحصول على مسار الملف الحالي
    base_dir = os.path.dirname(__file__)
    control_path = os.path.join(base_dir, 
    "telegram-members-transfer-bot-main", 
    "control.py")

    subprocess.run([sys.executable, 
    control_path, "start"])

# تعديل التحقق من اسم الملف ليكون بالصيغة الصحيحة
if __name__ == "__main__":
    run()
