# Rizwan Momin — Full-Stack Portfolio

A beginner-friendly portfolio built with HTML, CSS, JavaScript, Python and Flask.

## Features
- Responsive single-page portfolio
- About, skills, projects, resume and contact sections
- Flask route renders the portfolio page
- Server-side validation for the contact form
- Mobile navigation and simple reveal animations
- Resume link placeholder in `static/files/resume.pdf`

## 1. Requirements
- Python 3.10 or newer recommended
- VS Code or another code editor
- A browser

Check Python:
```bash
python --version
```
On some systems, use `python3 --version`.

## 2. Open the project
Extract the ZIP file and open the `rizwan_portfolio` folder in VS Code.

## 3. Create and activate a virtual environment

Windows PowerShell:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Windows Command Prompt:
```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 4. Install Flask
```bash
python -m pip install -r requirements.txt
```

## 5. Run the website
```bash
python app.py
```
Open http://127.0.0.1:5000 in your browser. Stop the server with `Ctrl+C`.

## 6. Personalize before sharing
Open `app.py` and update:
- `PROFILE`: email, GitHub and LinkedIn URLs
- `PROJECTS`: accurate descriptions and working project/repository links
- `SKILLS`: keep only technologies you can discuss honestly

Put your real PDF resume at `static/files/resume.pdf`. The provided link is only a placeholder until you add that file.

## Contact form note
The form validates fields on the Flask server and logs submissions in the terminal. It does **not** send email or store messages permanently. To receive messages, integrate a mail provider or database and protect secrets using environment variables.

## Deployment note
Do not deploy Flask's debug server to production. For a public deployment, use a production WSGI server and set a strong `SECRET_KEY` as an environment variable. Also configure a real contact delivery method.
