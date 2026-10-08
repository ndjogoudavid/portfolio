"""Build the one-page public CV. Run from the repository root."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "docs/files/NDJOGOU_MPIRA_OKOUMBA_DAVID_LOIC_CV.pdf"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

FONT_DIR = Path(r"C:\Windows\Fonts")
pdfmetrics.registerFont(TTFont("CVSans", str(FONT_DIR / "arial.ttf")))
pdfmetrics.registerFont(TTFont("CVSans-Bold", str(FONT_DIR / "arialbd.ttf")))

PAGE_W, PAGE_H = A4
SIDEBAR_W = 174
PAD = 37
MAIN_X = SIDEBAR_W + 32
MAIN_W = PAGE_W - MAIN_X - PAD

NAVY = colors.HexColor("#142D3A")
NAVY_SOFT = colors.HexColor("#244653")
TEAL = colors.HexColor("#167C80")
TEAL_LIGHT = colors.HexColor("#A7DCDD")
INK = colors.HexColor("#182831")
MUTED = colors.HexColor("#53656D")
PALE = colors.HexColor("#F3F7F6")
RULE = colors.HexColor("#D9E3E2")
WHITE = colors.white

c = canvas.Canvas(str(OUTPUT), pagesize=A4)
c.setTitle("NDJOGOU MPIRA OKOUMBA David Loic - CV")
c.setAuthor("NDJOGOU MPIRA OKOUMBA David Loic")

styles = {
    "body": ParagraphStyle("body", fontName="CVSans", fontSize=8.5, leading=12, textColor=INK, alignment=TA_LEFT, spaceAfter=0),
    "small": ParagraphStyle("small", fontName="CVSans", fontSize=7.7, leading=10.6, textColor=MUTED, alignment=TA_LEFT, spaceAfter=0),
    "side": ParagraphStyle("side", fontName="CVSans", fontSize=7.8, leading=11, textColor=colors.HexColor("#E4EEEE"), alignment=TA_LEFT, spaceAfter=0),
    "side_small": ParagraphStyle("side_small", fontName="CVSans", fontSize=7.2, leading=10, textColor=colors.HexColor("#C2D2D4"), alignment=TA_LEFT, spaceAfter=0),
}


def para(text, x, top, width, style):
    p = Paragraph(text, styles[style])
    _, height = p.wrap(width, PAGE_H)
    p.drawOn(c, x, top - height)
    return top - height


def section(title, x, top, width, dark=False):
    color = TEAL_LIGHT if dark else TEAL
    c.setFillColor(color)
    c.setFont("CVSans-Bold", 8)
    c.drawString(x, top - 8, title.upper())
    c.setStrokeColor(NAVY_SOFT if dark else RULE)
    c.setLineWidth(.65)
    c.line(x, top - 14, x + width, top - 14)
    return top - 25


def side_item(title, detail, y, width=136):
    c.setFillColor(WHITE)
    c.setFont("CVSans-Bold", 8)
    c.drawString(19, y - 8, title)
    y -= 13
    if detail:
        y = para(detail, 19, y, width, "side_small") - 8
    return y


def project(title, detail, description, y):
    c.setFillColor(INK)
    c.setFont("CVSans-Bold", 9.1)
    c.drawString(MAIN_X, y - 9, title)
    y -= 15
    y = para(detail, MAIN_X, y, MAIN_W, "small") - 3
    y = para(description, MAIN_X, y, MAIN_W, "body")
    return y - 12


# Sidebar and top accent establish a clear, restrained visual frame.
c.setFillColor(NAVY)
c.rect(0, 0, SIDEBAR_W, PAGE_H, fill=1, stroke=0)
c.setFillColor(TEAL)
c.rect(0, PAGE_H - 7, PAGE_W, 7, fill=1, stroke=0)

# Main identity block.
y = PAGE_H - 42
c.setFillColor(MUTED)
c.setFont("CVSans-Bold", 7.5)
c.drawString(MAIN_X, y, "SOFTWARE ENGINEERING  /  KIGALI, RWANDA")
y -= 30
c.setFillColor(INK)
c.setFont("CVSans-Bold", 20)
c.drawString(MAIN_X, y, "NDJOGOU MPIRA OKOUMBA")
y -= 27
c.setFillColor(TEAL)
c.setFont("CVSans-Bold", 24)
c.drawString(MAIN_X, y, "David Loic")
y -= 19
c.setFillColor(MUTED)
c.setFont("CVSans", 9)
c.drawString(MAIN_X, y, "Information Technology student  |  Software Engineering")
y -= 19
y = para(
    "ndjogoudaviddev@gmail.com  &nbsp;|&nbsp;  bdc.is-a.dev<br/>"
    "github.com/ndjogoudavid  &nbsp;|&nbsp;  linkedin.com/in/ndjogoudavid",
    MAIN_X, y, MAIN_W, "small")
y -= 15

y = section("Profile", MAIN_X, y, MAIN_W)
y = para(
    "Software engineering student with hands-on experience building web, desktop and mobile applications."
    " Strongest in Java and full-stack development, with project work in application workflows, data storage and team software coursework.",
    MAIN_X, y, MAIN_W, "body")
y -= 16

y = section("Selected completed projects", MAIN_X, y, MAIN_W)
y = project("Pharmacy Management System - Desktop", "Java  |  PostgreSQL  |  Solo project, 2025",
        "Built pharmacy inventory, sales, customer, supplier and reporting workflows.", y)
y = project("Pharmacy Management System - Web", "Spring Boot  |  React  |  PostgreSQL  |  JWT, 2025",
        "Built a separate web application for medicines, prescriptions, billing and role-based access.", y)
y = project("Household Chore Manager", "Spring Boot  |  Thymeleaf  |  PostgreSQL  |  Docker, 2025",
        "Built a task-scheduling application with persistent storage and automated tests.", y)
y = project("Immunization Planner & Tracker", "Android / Java  |  Firebase  |  HL7 FHIR  |  Team coursework, 2026",
        "Worked on a team application for child vaccination schedules and records.", y)
y = project("BloodDonorSystem", "ASP.NET / C#  |  SQL Server  |  Team coursework, 2025",
        "Used C# and ASP.NET to complete a team semester project.", y)

# Sidebar content is compact and grouped by purpose.
sy = PAGE_H - 63
sy = section("Contact", 19, sy, 136, dark=True)
sy = para("Kigali, Rwanda<br/>+250 790 801 245", 19, sy, 136, "side") - 17

sy = section("Education", 19, sy, 136, dark=True)
sy = side_item("AUCA", "BSc Information Technology<br/>Major: Software Engineering<br/>2022 - present", sy)
sy = side_item("Lycée Jacques Prévert", "French Scientific Baccalaureate<br/>2016 - 2019", sy)

sy = section("Technical skills", 19, sy, 136, dark=True)
sy = side_item("Languages", "Java, JavaScript, HTML/CSS, SQL", sy)
sy = side_item("Also used", "C# in semester coursework; basic Python", sy)
sy = side_item("Frameworks", "Spring Boot, React, Node.js / Express, ASP.NET coursework", sy)
sy = side_item("Data & tools", "PostgreSQL, MySQL, SQL Server, Git, GitHub, Docker", sy)
sy = side_item("Concepts", "REST APIs, relational data modeling, object-oriented programming, testing", sy)

sy = section("Certificates", 19, sy, 136, dark=True)
sy = para(
    "<b>AUCA</b><br/>English Proficiency I &amp; II<br/>Intermediate, 90 hours<br/><br/>"
    "<b>Cisco Networking Academy</b><br/>Advanced Network Operations 2.0<br/>Networking Essentials<br/>Operating Systems Basics",
    19, sy, 136, "side_small")

# Quiet footer rule and portfolio address on the main column.
c.setStrokeColor(RULE)
c.setLineWidth(.65)
c.line(MAIN_X, 34, PAGE_W - PAD, 34)
c.setFillColor(MUTED)
c.setFont("CVSans", 7.2)
c.drawString(MAIN_X, 22, "Portfolio: bdc.is-a.dev")

if y < 40 or sy < 32:
    raise RuntimeError(f"CV content overflowed page: main={y:.1f}, sidebar={sy:.1f}")

c.save()
print(OUTPUT)
