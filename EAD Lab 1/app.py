from flask import Flask, send_file
from generate_report import main as generate_report
import os

app = Flask(__name__)

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/download')
def download_report():
    # Generate the report
    generate_report()
    
    # Send the file
    return send_file('EAD_Lab_Report_1.docx',
                    mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                    as_attachment=True,
                    download_name='EAD_Lab_Report_1.docx')

if __name__ == '__main__':
    # Get port from environment variable or use 5000 as default
    port = int(os.environ.get('PORT', 5000))
    # In production, set debug to False
    app.run(host='0.0.0.0', port=port, debug=False) 