"""Build the public one-page CV. Run from the repository root."""

from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import simpleSplit
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import Paragraph
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "docs/files/NDJOGOU_MPIRA_OKOUMBA_DAVID_LOIC_CV.pdf"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

font_dir = Path(r"C:\Windows\Fonts")
pdfmetrics.registerFont(TTFont("Arial", str(font_dir / "arial.ttf")))
pdfmetrics.registerFont(TTFont("Arial-Bold", str(font_dir / "arialbd.ttf")))

W, H = A4
ink = colors.HexColor("#183048")
muted = colors.HexColor("#536273")
line = colors.HexColor("#d6dee5")
accent = colors.HexColor("#216884")
c = canvas.Canvas(str(OUTPUT), pagesize=A4)
c.setTitle("NDJOGOU MPIRA OKOUMBA David Loic - CV")
c.setAuthor("NDJOGOU MPIRA OKOUMBA David Loic")

left = 42
right = W - 42
y = H - 42

def txt(value, x, yy, size=9, bold=False, color=ink):
    c.setFillColor(color)
    c.setFont("Arial-Bold" if bold else "Arial", size)
    c.drawString(x, yy, value)

def section(title):
    global y
    y -= 18
    txt(title.upper(), left, y, 9, True, accent)
    c.setStrokeColor(line)
    c.line(left, y - 6, right, y - 6)
    y -= 19

def item(title, date, detail, body=None):
    global y
    txt(title, left, y, 9, True)
    c.setFont("Arial", 8)
    c.setFillColor(muted)
    c.drawRightString(right, y, date)
    y -= 12
    if detail:
        txt(detail, left, y, 8, False, muted)
        y -= 12
    if body:
        for segment in simpleSplit(body, "Arial", 8, right-left):
            txt(segment, left, y, 8)
            y -= 10
    y -= 4

txt("NDJOGOU MPIRA OKOUMBA David Loic", left, y, 17, True)
y -= 18
txt("Software Engineering Student  |  Full-Stack Developer", left, y, 9, False, accent)
y -= 15
txt("Kigali, Rwanda  |  +250 790 801 245  |  ndjogoudaviddev@gmail.com", left, y, 8)
y -= 12
txt("bdc.is-a.dev  |  github.com/ndjogoudavid  |  linkedin.com/in/ndjogoudavid", left, y, 8)
y -= 2

section("Profile")
profile = ("Software engineering student building full-stack applications for health and public-service workflows. "
           "Experience with Java/Spring Boot, React, Node.js, REST APIs, and relational databases. "
           "Interested in applying software, data, and responsible AI to energy and public-policy problems.")
for segment in simpleSplit(profile, "Arial", 8.5, right-left):
    txt(segment, left, y, 8.5)
    y -= 12

section("Education")
item("Adventist University of Central Africa (AUCA)", "2022 - present",
     "BSc Information Technology, major in Software Engineering | Kigali, Rwanda",
     "Coursework includes probability and statistics, software engineering, databases, and object-oriented programming.")
item("Lycee Jacques Prevert", "2016 - 2019", "French Scientific Baccalaureate")

section("Selected projects")
item("Pharmacy Management System - desktop | solo project", "2025",
     "Java desktop application, PostgreSQL",
     "Built inventory, sales, customer, supplier, and reporting workflows.")
item("Pharmacy Management System - web", "2025",
     "Spring Boot, React, PostgreSQL, JWT",
     "Built a separate web application for medicines, prescriptions, billing, and role-based access.")
item("Owendo Municipal Workflow System | final-year project in progress", "2026 - present",
     "React, Node.js/Express, PostgreSQL",
     "Developing a municipal request and workflow system with role-based operations and service tracking; project remains under development.")
item("Immunization Planner & Tracker | collaborative project", "2026",
     "Android/Java, Firebase, HL7 FHIR",
     "Contributed to an Android vaccination planning and tracking application in a team project.")
item("Household Chore Manager", "2025", "Spring Boot, Thymeleaf, PostgreSQL, Docker",
     "Built a task scheduling application with persistence and automated tests.")
item("BloodDonorSystem | collaborative coursework", "2025", "ASP.NET/C#, SQL Server",
     "Used C# and ASP.NET to complete a team semester project.")
item("AxM Shop | additional build", "In development", "Next.js, TypeScript, PostgreSQL, Prisma",
     "Marketplace concept for local sellers and imported goods, with order and delivery tracking and simulated checkout.")
item("Ntchiré | additional build", "In development", "Flutter, NestJS, PostgreSQL",
     "Digital-health platform for Gabon; the mobile and backend systems remain under development.")
item("Lubao | additional build", "In development", "Expo, React Native, Supabase, TypeScript",
     "Language-learning app for Fang, Punu and Obamba, with lessons, quizzes, dictionary and community features.")

section("Certificates")
txt("AUCA English Proficiency Certificate I & II (Intermediate, 90 hours); Cisco Networking Essentials;", left, y, 8)
y -= 12
txt("Advanced Network Operations 2.0; Operating Systems Basics.", left, y, 8)
y -= 6

section("Technical skills")
for label, value in [
    ("Languages", "Java, JavaScript, HTML/CSS; C# used in semester coursework; basic Python"),
    ("Frameworks", "Spring Boot, React, Node.js/Express, ASP.NET coursework"),
    ("Data and tools", "PostgreSQL, MySQL, SQL Server, Git, GitHub, Docker"),
    ("Concepts", "Object-oriented programming, REST APIs, relational data modeling, testing"),
]:
    txt(label + ":", left, y, 8, True)
    txt(value, left + 86, y, 8)
    y -= 13

c.setStrokeColor(line)
c.line(left, 40, right, 40)
txt("Portfolio: bdc.is-a.dev", left, 27, 7.5, False, muted)
if y < 50:
    raise RuntimeError(f"CV content overflowed page: y={y}")
c.save()
print(OUTPUT)
