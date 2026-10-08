# Portfolio source

The public site files are in `docs/` on the repository's main branch. `docs/CNAME` points to `bdc.is-a.dev`. The older `portfolio-main.zip` and extracted `portfolio-main` folder under AUCA/Portfolio are historical copies; edit this Git checkout for future site changes.

## Update the CV

Edit `build_cv.py`, then run it with Python and ReportLab from the repository root. It writes `docs/files/NDJOGOU_MPIRA_OKOUMBA_DAVID_LOIC_CV.pdf`. Also copy the generated PDF to `AUCA/Portfolio/NDJOGOU_MPIRA_OKOUMBA_DAVID_LOIC_CV.pdf` for application uploads. The website's `docs/cv.html` and homepage already link to that filename.

## Update the website

Edit `docs/index.html` for the narrative, projects, skills, and contact details. Edit `docs/cv.html` for the CV preview and download page. Open `docs/index.html` locally to review both desktop and mobile layouts before committing and publishing.

The Java desktop pharmacy project is separate from the Spring Boot/React web project. Its source currently contains a hard-coded local database password and must be cleaned before it is published.
