import os

def generate_invitations(template, attendees):
    # 1. التحقق من أنواع المدخلات (Input Types)
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # 2. التعامل مع المدخلات الفارغة (Empty Inputs)
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. معالجة كل حاضر (Attendee) وإنشاء الملفات
    for index, attendee in enumerate(attendees, start=1):
        # نأخذ نسخة من القالب لكل شخص
        content = template
        
        # قائمة بالمتغيرات التي نحتاج استبدالها
        placeholders = ["name", "event_title", "event_date", "event_location"]
        
        for key in placeholders:
            # الحصول على القيمة من القاموس، وإذا كانت None أو غير موجودة نضع "N/A"
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            
            # استبدال Placeholder في النص (مثلاً {name}) بالقيمة الحقيقية
            content = content.replace(f"{{{key}}}", str(value))
        
        # 4. كتابة المحتوى في ملف جديد
        filename = f"output_{index}.txt"
        
        # اختياري: التأكد مما إذا كان الملف موجوداً مسبقاً (حسب التلميحات)
        if os.path.exists(filename):
            print(f"Warning: {filename} already exists. Overwriting...")
            
        try:
            with open(filename, 'w') as f:
                f.write(content)
        except Exception as e:
            print(f"An error occurred while writing {filename}: {e}")
