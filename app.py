#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    CP_a = 35
    CM_a = 90
    CP_b = 4
    CM_b = 7.5

    P = float(request.form['power'])
    D_a = float(request.form['d_a'])
    D_b = float(request.form['d_b'])
    D_cavo = float(request.form['d_cavo'])
    D_aereo = float(request.form['d_aereo'])
    D_totale = D_cavo + D_aereo

    A = CP_a * P + CM_a * P * D_aereo / D_totale + 2 * CM_a * P * D_cavo / D_totale + 100
    B = CP_b * P + CM_b * P * D_aereo / D_totale + 2 * CM_b * P * D_cavo / D_totale + 6000

    price = min(A, B)

    return render_template('result.html', price=price)

if __name__ == '__main__':
    app.run()


# In[ ]:




