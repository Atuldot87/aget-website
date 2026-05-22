from flask import Flask, render_template, request, jsonify, send_file
import json
import datetime
import io
import os

app = Flask(__name__)
app.secret_key = 'aget_secret_key_2026'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/programs')
def programs():
    return render_template('programs.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/api/contact', methods=['POST'])
def handle_contact():
    data = request.get_json()
    # In production, save to DB or send email
    return jsonify({'success': True, 'message': 'Thank you! We will contact you shortly.'})

@app.route('/api/donate', methods=['POST'])
def handle_donation():
    data = request.get_json()
    name = data.get('name', '')
    email = data.get('email', '')
    phone = data.get('phone', '')
    amount = data.get('amount', 0)
    pan = data.get('pan', '')
    address = data.get('address', '')
    purpose = data.get('purpose', 'General Donation')
    payment_mode = data.get('payment_mode', '')
    transaction_id = data.get('transaction_id', '')

    # Generate receipt number
    receipt_no = f"AGET/2026/{datetime.datetime.now().strftime('%m%d%H%M%S')}"
    date_str = datetime.datetime.now().strftime('%d %B %Y')
    time_str = datetime.datetime.now().strftime('%I:%M %p')

    receipt_data = {
        'success': True,
        'receipt_no': receipt_no,
        'name': name,
        'email': email,
        'phone': phone,
        'amount': amount,
        'pan': pan,
        'address': address,
        'purpose': purpose,
        'payment_mode': payment_mode,
        'transaction_id': transaction_id,
        'date': date_str,
        'time': time_str,
        'message': 'Donation received successfully! Your receipt has been generated.'
    }
    return jsonify(receipt_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
