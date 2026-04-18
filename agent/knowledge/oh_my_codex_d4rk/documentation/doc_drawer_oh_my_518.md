i-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
}

pre {
  margin: 1rem 0;
  padding: 1rem;
  border-radius: 8px;
  border: 1px solid var(--border);
  background: #010409;
  overflow-x: auto;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
}

th,
td {
  text-align: left;
  border: 1px solid var(--border);
  padding: 0.65rem;
  vertical-align: top;
}

th {
  background: #161b22;
}

.muted {
  color: var(--muted);
}

footer {
  border-top: 1px solid var(--border);
  padding: 1.2rem 0 2rem;
  color: var(--muted);
}

@media (max-width: 700px) {
  .brand {
    width: 100%;
    margin-right: 0;
  }

  .hero {
    padding: 1.3rem;
  }
}