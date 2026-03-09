from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    authorized = False
    error = ""
    
    # 20+ Features/Data Points for the Dashboard
    stats = {
        "Student Name": "Your Name",
        "Roll Number": "12345678",
        "Project": "EduVantage Pro v1.0",
        "Status": "Verified",
        "Server": "Cloud-Hosted",
        "Database": "Connected",
        "Uptime": "99.9%",
        "Language": "Python 3.13",
        "Framework": "Flask 3.0",
        "Security": "AES-256 Enabled",
        "Encryption": "SSL/TLS",
        "Last Login": datetime.now().strftime("%H:%M:%S"),
        "Theme": "Modern Slate",
        "Modules": "15 Active",
        "Storage": "Cloud Synced",
        "API Status": "Online",
        "Latency": "24ms",
        "Region": "Global",
        "Backup": "Daily Auto",
        "Environment": "Production"
    }

    if request.method == 'POST':
        if request.form.get('password') == "123": # Change password here
            authorized = True
        else:
            error = "Invalid Access Key"
            
    return render_template('index.html', authorized=authorized, error=error, data=stats)

if __name__ == '__main__':
    app.run(debug=True)