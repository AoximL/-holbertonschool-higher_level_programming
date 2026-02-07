import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/items')
def items():
    # 1. قراءة البيانات من ملف JSON
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            # استخراج القائمة التي مفتاحها "items"
            items_list = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        # في حال عدم وجود الملف أو خطأ في التنسيق، نرسل قائمة فارغة
        items_list = []

    # 2. تمرير القائمة إلى القالب items.html
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
