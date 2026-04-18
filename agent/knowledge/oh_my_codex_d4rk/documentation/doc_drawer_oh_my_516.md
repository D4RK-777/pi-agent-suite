op: 0;
  backdrop-filter: blur(6px);
}

.container {
  width: min(1040px, 92vw);
  margin: 0 auto;
}

.nav {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 1rem;
  padding: 0.9rem 0;
}

.brand {
  font-weight: 700;
  color: var(--text);
  margin-right: auto;
}

.nav-links {
  display: flex;
  flex-wrap: wrap;
  gap: 0.8rem;
}

.nav-links a {
  padding: 0.35rem 0.6rem;
  border-radius: 6px;
}

.nav-links a.active,
.nav-links a:hover {
  background: var(--panel);
}

main {
  padding: 2rem 0 3rem;
}

.hero {
  padding: 2rem;
  border: 1px solid var(--border);
  border-radius: 12px;
  background: linear-gradient(180deg, rgba(35, 134, 54, 0.12), rgba(22, 27, 34, 0.9));
}

h1,
h2,
h3 {
  line-height: 1.25;
  margin-top: 0;
}

h1 {
  font-size: clamp(1.8rem, 3.8vw, 2.8rem);
}