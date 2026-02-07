from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    # تشغيل التطبيق على المنفذ 5000 مع تفعيل وضع التصحيح
    app.run(debug=True, port=5000)
