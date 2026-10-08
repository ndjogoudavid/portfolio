(() => {
  const prefersReducedMotion = window.matchMedia(
    "(prefers-reduced-motion: reduce)",
  ).matches;

  const scrollToSection = (id) => {
    const section = document.getElementById(id);
    if (!section) return false;
    section.scrollIntoView({
      behavior: prefersReducedMotion ? "auto" : "smooth",
      block: "start",
    });
    return true;
  };

  const pendingTarget = sessionStorage.getItem("portfolio-scroll-target");
  if (pendingTarget) {
    sessionStorage.removeItem("portfolio-scroll-target");
    requestAnimationFrame(() => scrollToSection(pendingTarget));
  }

  document.querySelectorAll('.site-header nav a[href*="#"]').forEach((link) => {
    link.addEventListener("click", (event) => {
      const url = new URL(link.href, window.location.href);
      const targetId = url.hash.slice(1);
      if (!targetId) return;

      event.preventDefault();
      if (url.pathname === window.location.pathname) {
        scrollToSection(targetId);
        return;
      }

      sessionStorage.setItem("portfolio-scroll-target", targetId);
      window.location.assign("/");
    });
  });
})();
