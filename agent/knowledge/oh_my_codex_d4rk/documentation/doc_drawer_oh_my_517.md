h2,
h3 {
  line-height: 1.25;
  margin-top: 0;
}

h1 {
  font-size: clamp(1.8rem, 3.8vw, 2.8rem);
}

h2 {
  margin-top: 2rem;
  font-size: 1.5rem;
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1rem;
  margin-top: 1rem;
}

.card {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 1rem;
}

.badge {
  display: inline-block;
  background: rgba(35, 134, 54, 0.2);
  color: #7ee787;
  border: 1px solid rgba(35, 134, 54, 0.5);
  border-radius: 999px;
  padding: 0.1rem 0.55rem;
  font-size: 0.8rem;
}

code,
pre {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
}