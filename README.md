# Portfolio source

The public site files are in `docs/` on the repository's main branch. `docs/CNAME` points to `bdc.is-a.dev`. The older `portfolio-main.zip` and extracted `portfolio-main` folder under AUCA/Portfolio are historical copies; edit this Git checkout for future site changes.

## Update the CV

Edit `build_cv.py`, then run it with Python and ReportLab from the repository root. It writes `docs/files/Ndjogou_David_CV.pdf`; the current copy is also saved in `AUCA/Portfolio/Ndjogou_David_CV.pdf` for application uploads. The website's `/cv/` page and homepage link to this download name.

## Update the website

Edit `docs/index.html` for the narrative, projects, skills, and contact details. Edit `docs/cv/index.html` for the CV page. `docs/cv.html` redirects older links to `/cv/`. Preview the site at desktop and mobile widths before committing and publishing.

The Java desktop pharmacy project is separate from the Spring Boot/React web project. Its source currently contains a hard-coded local database password and must be cleaned before it is published.
