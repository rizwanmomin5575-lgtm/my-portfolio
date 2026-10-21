from flask import Flask, render_template, request, flash, redirect, url_for
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-this-secret-key-for-production")

# Edit these details before publishing.
PROFILE = {
    "name": "Rizwan Momin",
    "role": "Aspiring Software Developer",
    "location": "Pune, Maharashtra, India",
    "email": "rizwanmomin5575@gmail.com",
    "github": "https://github.com/rizwanmomin5575-lgtm.",
    "linkedin": "https://www.linkedin.com/in/yourusername/",
    "intro": "I build responsive web experiences with HTML, CSS and JavaScript, and I’m learning Python to develop practical backend applications."
}

SKILLS = [
    {"name": "HTML5", "group": "Frontend", "description": "Semantic page structure"},
    {"name": "CSS3", "group": "Frontend", "description": "Responsive layouts and styling"},
    {"name": "JavaScript", "group": "Frontend", "description": "Interactive user experiences"},
    {"name": "Python", "group": "Backend", "description": "Programming fundamentals and web development"},
    {"name": "Flask", "group": "Backend", "description": "Beginner-friendly Python web framework"},
    {"name": "Git & GitHub", "group": "Tools", "description": "Version control and project hosting"},
]

PROJECTS = [
    {
        "number": "01",
        "name": "Restaurant Website Portfolio",
        "type": "Frontend project",
        "description": "A responsive restaurant website concept with menu, service information and a clear customer-focused layout.",
        "stack": ["HTML", "CSS", "JavaScript"],
        "status": "Add your live project link"
    },
    {
        "number": "02",
        "name": "Hospital Management System",
        "type": "Academic project",
        "description": "A project concept for organizing patient registration, appointments, billing and records to reduce manual work.",
        "stack": ["Add your actual technologies"],
        "status": "Add your repository link"
    },
    {
        "number": "03",
        "name": "Flask Portfolio Website",
        "type": "Full-stack project",
        "description": "This portfolio uses Flask to render pages and process contact form submissions with server-side validation.",
        "stack": ["HTML", "CSS", "JavaScript", "Python", "Flask"],
        "status": "You're viewing this project"
    }
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        profile=PROFILE,
        skills=SKILLS,
        projects=PROJECTS,
        year=datetime.now().year
    )

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        flash("Please fill in every field.", "error")
        return redirect(url_for("home") + "#contact")

    if len(name) > 100 or len(email) > 254 or len(message) > 3000:
        flash("One of your fields is too long. Please shorten it and try again.", "error")
        return redirect(url_for("home") + "#contact")

    # Demo behavior: do not pretend this sends an email.
    # For production, connect an email service or save submissions to a database.
    print(f"[Portfolio contact form] From: {name} <{email}>")
    print(f"Message: {message}")
    flash("Thanks! Your message passed validation. This demo logs it in the terminal; email delivery is not configured yet.", "success")
    return redirect(url_for("home") + "#contact")

if __name__ == "__main__":
    app.run(debug=True)
