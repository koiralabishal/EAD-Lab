# EAD Lab Report Generator

This web application generates a well-formatted DOCX file containing the EAD Lab report with proper formatting and structure.

## Features

- Web interface for viewing lab report
- Download report as DOCX file
- Properly formatted sections and content
- Responsive design

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Local Development

1. Clone this repository:
```bash
git clone https://github.com/yourusername/ead-lab-report.git
cd ead-lab-report
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the development server:
```bash
python app.py
```

4. Open your browser and visit `http://localhost:5000`

## Deployment

### Deploy to Heroku

1. Create a Heroku account if you don't have one
2. Install Heroku CLI
3. Login to Heroku:
```bash
heroku login
```

4. Create a new Heroku app:
```bash
heroku create your-app-name
```

5. Push to Heroku:
```bash
git push heroku main
```

### Deploy to GitHub Pages (Static Content Only)

1. Create a new repository on GitHub
2. Push your code:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/your-repo.git
git push -u origin main
```

3. Go to repository Settings > Pages
4. Select your main branch as source
5. Click Save

## Project Structure

```
.
├── app.py              # Flask application
├── generate_report.py  # DOCX generation script
├── requirements.txt    # Python dependencies
├── Procfile           # Heroku deployment config
└── static/            # Static files
    ├── index.html     # Main webpage
    └── images/        # Images used in the report
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details 