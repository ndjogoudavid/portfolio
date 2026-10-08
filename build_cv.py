"""Build the verified, one-page software engineering CV."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Flowable,
    HRFlowable,
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "docs/files/NDJOGOU_MPIRA_OKOUMBA_DAVID_LOIC_CV.pdf"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

FONT_DIR = Path(r"C:\Windows\Fonts")
pdfmetrics.registerFont(TTFont("CVArial", str(FONT_DIR / "arial.ttf")))
pdfmetrics.registerFont(TTFont("CVArial-Bold", str(FONT_DIR / "arialbd.ttf")))
pdfmetrics.registerFontFamily("CVArial", normal="CVArial", bold="CVArial-Bold")

INK = colors.HexColor("#222222")
NAVY = colors.HexColor("#222222")
ACCENT = colors.HexColor("#557C63")  # Soft evergreen accent for the energy focus.
MUTED = colors.HexColor("#5F6368")
RULE = colors.HexColor("#D7D8DA")

doc = SimpleDocTemplate(
    str(OUTPUT),
    pagesize=A4,
    leftMargin=17 * mm,
    rightMargin=17 * mm,
    topMargin=14 * mm,
    bottomMargin=14 * mm,
    title="NDJOGOU MPIRA OKOUMBA David Loic - CV",
    author="NDJOGOU MPIRA OKOUMBA David Loic",
)
# SimpleDocTemplate's default frame has 6 pt of internal padding on each side.
# Match table widths to the actual usable frame so entry titles and dates align
# with paragraphs and section rules instead of spilling past the left margin.
WIDTH = A4[0] - doc.leftMargin - doc.rightMargin - 12

styles = {
    "name": ParagraphStyle("name", fontName="CVArial-Bold", fontSize=20, leading=23, textColor=NAVY, spaceAfter=2),
    "headline": ParagraphStyle("headline", fontName="CVArial-Bold", fontSize=9.2, leading=11.7, textColor=ACCENT, spaceAfter=5),
    "contact": ParagraphStyle("contact", fontName="CVArial", fontSize=8.55, leading=11.5, textColor=MUTED),
    "entry": ParagraphStyle("entry", fontName="CVArial-Bold", fontSize=10, leading=12.7, textColor=INK),
    "date": ParagraphStyle("date", fontName="CVArial-Bold", fontSize=8.6, leading=11.5, textColor=NAVY, alignment=TA_RIGHT),
    "meta": ParagraphStyle("meta", fontName="CVArial", fontSize=8.65, leading=11.5, textColor=MUTED, spaceAfter=2),
    "body": ParagraphStyle("body", fontName="CVArial", fontSize=9.05, leading=12.2, textColor=INK),
    "bullet": ParagraphStyle("bullet", fontName="CVArial", fontSize=9.05, leading=12.2, textColor=INK, leftIndent=12, firstLineIndent=-10, spaceAfter=2),
    "link": ParagraphStyle("link", fontName="CVArial", fontSize=8.3, leading=10.6, textColor=ACCENT),
}


def p(text, style):
    return Paragraph(text, styles[style])


class SectionHeading(Flowable):
    def __init__(self, title):
        super().__init__()
        self.title = title.upper()
        self.height = 20

    def wrap(self, available_width, available_height):
        self.width = available_width
        return available_width, self.height

    def draw(self):
        self.canv.setFillColor(ACCENT)
        self.canv.rect(0, 3, 3, 14, stroke=0, fill=1)
        self.canv.setFillColor(NAVY)
        self.canv.setFont("CVArial-Bold", 9.8)
        self.canv.drawString(11, 5.5, self.title)
        label_width = pdfmetrics.stringWidth(self.title, "CVArial-Bold", 9.8)
        self.canv.setStrokeColor(RULE)
        self.canv.setLineWidth(0.65)
        self.canv.line(22 + label_width, 10, self.width, 10)


def section(title):
    return [Spacer(1, 10), SectionHeading(title), Spacer(1, 4)]


def entry_header(title, date):
    row = Table(
        [[p(title, "entry"), p(date, "date")]],
        colWidths=[WIDTH - 97, 97],
    )
    row.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
    ]))
    return row


def project(title, date, stack, bullets, source=None):
    content = [entry_header(title, date), p(stack, "meta")]
    content.extend(p("- " + bullet, "bullet") for bullet in bullets)
    if source:
        content.append(p(
            '<b>Source:</b> <link href="https://github.com/ndjogoudavid/pharmacy-management_25713" color="#557C63">'
            "github.com/ndjogoudavid/pharmacy-management_25713</link>",
            "link",
        ))
    content.append(Spacer(1, 8))
    return KeepTogether(content)


story = [
    HRFlowable(width="100%", thickness=1.5, color=ACCENT, spaceAfter=10),
    p("NDJOGOU MPIRA OKOUMBA David Loic", "name"),
    p("SOFTWARE ENGINEERING STUDENT  |  KIGALI, RWANDA", "headline"),
    p(
        '+250 790 801 245&nbsp;&nbsp;|&nbsp;&nbsp;'
        '<link href="mailto:ndjogoudaviddev@gmail.com" color="#53636C">ndjogoudaviddev@gmail.com</link>',
        "contact",
    ),
    p(
        '<link href="https://bdc.is-a.dev" color="#53636C">bdc.is-a.dev</link>'
        '&nbsp;&nbsp;|&nbsp;&nbsp;'
        '<link href="https://github.com/ndjogoudavid" color="#53636C">github.com/ndjogoudavid</link>'
        '&nbsp;&nbsp;|&nbsp;&nbsp;'
        '<link href="https://www.linkedin.com/in/ndjogoudavid" color="#53636C">linkedin.com/in/ndjogoudavid</link>',
        "contact",
    ),
    Spacer(1, 5),
    HRFlowable(width="100%", thickness=0.7, color=RULE),
    *section("Education"),
    KeepTogether([
        entry_header("Adventist University of Central Africa (AUCA)", "2022 - Present"),
        p("BSc Information Technology, major in Software Engineering | Kigali, Rwanda", "meta"),
        Spacer(1, 4),
        p(
            "<b>Relevant coursework:</b> Data Structures and Algorithms; Probability and Statistics; "
            "Multivariable Calculus and ODE; Object-Oriented Programming; Software Testing Techniques.",
            "body",
        ),
        Spacer(1, 7),
        entry_header("Lycee Jacques Prevert", "2012 - 2019"),
        p("French Scientific Baccalaureate | Gabon", "meta"),
    ]),
    *section("Selected technical projects"),
    project(
        "Pharmacy Management System | Web",
        "2025",
        "Independent project  |  Spring Boot, React, PostgreSQL, JWT",
        [
            "Built a React interface and Spring Boot API for medicine records, prescriptions, and billing.",
            "Implemented JWT authentication and distinct admin, pharmacist, and patient roles.",
        ],
        source=True,
    ),
    project(
        "Pharmacy Management System | Desktop",
        "2025",
        "Independent project  |  Java Swing, PostgreSQL",
        [
            "Developed desktop screens for inventory, sales, customers, suppliers, and reports.",
            "Connected the Java application to PostgreSQL for record management and sales reporting.",
        ],
    ),
    project(
        "Household Chore Manager",
        "2025",
        "Independent project  |  Spring Boot, Thymeleaf, PostgreSQL, Docker",
        [
            "Built admin and member workflows to create chores, assign tasks, and track completion.",
            "Added service and web-layer tests for assignment ownership, status changes, and admin access.",
        ],
    ),
    *section("Technical skills"),
    p("<b>Languages:</b> Java, JavaScript, SQL; C# (coursework), Python (basic)", "body"),
    p("<b>Web and backend:</b> Spring Boot, React, Thymeleaf, Node.js / Express, REST APIs", "body"),
    p("<b>Data and tools:</b> PostgreSQL, MySQL, SQL Server, Git, GitHub, Docker", "body"),
    p("<b>Foundations:</b> Object-oriented programming, relational modeling, testing, access control", "body"),
    *section("Certifications and training"),
    p("<b>AUCA English Language Centre:</b> English Proficiency Certificate I &amp; II, Intermediate (90 hours), 2025", "body"),
    p("<b>Cisco Networking Academy:</b> Advanced Network Operations 2.0; Networking Essentials; Operating Systems Basics", "body"),
]

doc.build(story)
print(OUTPUT)
