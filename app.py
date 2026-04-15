from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Francis Kago — App Docker</title>
  <link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;700;800&display=swap" rel="stylesheet"/>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --bg:       #0a0a0f;
      --surface:  #12121a;
      --border:   #1e1e2e;
      --accent:   #00f5a0;
      --accent2:  #00d4ff;
      --text:     #e8e8f0;
      --muted:    #6b6b8a;
      --danger:   #ff4b6e;
    }

    body {
      background: var(--bg);
      color: var(--text);
      font-family: 'Syne', sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 2rem;
      overflow-x: hidden;
    }

    /* Grille d'arrière-plan */
    body::before {
      content: '';
      position: fixed;
      inset: 0;
      background-image:
        linear-gradient(rgba(0,245,160,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,245,160,0.03) 1px, transparent 1px);
      background-size: 40px 40px;
      pointer-events: none;
      z-index: 0;
    }

    /* Blob lumineux */
    body::after {
      content: '';
      position: fixed;
      top: -200px; left: -200px;
      width: 600px; height: 600px;
      background: radial-gradient(circle, rgba(0,245,160,0.06) 0%, transparent 70%);
      pointer-events: none;
      z-index: 0;
      animation: blobMove 12s ease-in-out infinite alternate;
    }

    @keyframes blobMove {
      from { transform: translate(0,0); }
      to   { transform: translate(400px, 300px); }
    }

    .container {
      position: relative;
      z-index: 1;
      max-width: 820px;
      width: 100%;
    }

    /* BADGE DOCKER */
    .badge-docker {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(0,212,255,0.08);
      border: 1px solid rgba(0,212,255,0.25);
      color: var(--accent2);
      font-family: 'Space Mono', monospace;
      font-size: 0.7rem;
      letter-spacing: 0.15em;
      padding: 6px 14px;
      border-radius: 2px;
      margin-bottom: 2.5rem;
      animation: fadeDown 0.5s ease both;
    }

    .badge-docker::before {
      content: '▶';
      font-size: 0.6rem;
    }

    /* TITRE */
    .title {
      font-size: clamp(2.8rem, 6vw, 4.5rem);
      font-weight: 800;
      line-height: 1.05;
      letter-spacing: -0.03em;
      margin-bottom: 1rem;
      animation: fadeDown 0.6s ease 0.1s both;
    }

    .title .accent { color: var(--accent); }
    .title .name   { color: var(--accent2); }

    .subtitle {
      font-family: 'Space Mono', monospace;
      font-size: 0.85rem;
      color: var(--muted);
      margin-bottom: 3rem;
      animation: fadeDown 0.6s ease 0.2s both;
    }

    /* CARDS */
    .cards {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 1px;
      background: var(--border);
      border: 1px solid var(--border);
      margin-bottom: 2rem;
      animation: fadeUp 0.7s ease 0.3s both;
    }

    .card {
      background: var(--surface);
      padding: 1.8rem;
      transition: background 0.2s;
    }

    .card:hover { background: #16162a; }

    .card-label {
      font-family: 'Space Mono', monospace;
      font-size: 0.65rem;
      letter-spacing: 0.2em;
      color: var(--muted);
      text-transform: uppercase;
      margin-bottom: 0.6rem;
    }

    .card-value {
      font-size: 1.4rem;
      font-weight: 700;
      color: var(--text);
    }

    .card-value.green { color: var(--accent); }
    .card-value.blue  { color: var(--accent2); }
    .card-value.red   { color: var(--danger); }

    /* STATUS BAR */
    .status-bar {
      display: flex;
      align-items: center;
      gap: 12px;
      background: var(--surface);
      border: 1px solid var(--border);
      padding: 1rem 1.5rem;
      margin-bottom: 2rem;
      animation: fadeUp 0.7s ease 0.4s both;
    }

    .dot {
      width: 8px; height: 8px;
      border-radius: 50%;
      background: var(--accent);
      box-shadow: 0 0 8px var(--accent);
      animation: pulse 2s ease-in-out infinite;
    }

    @keyframes pulse {
      0%, 100% { opacity: 1; transform: scale(1); }
      50%       { opacity: 0.5; transform: scale(0.8); }
    }

    .status-text {
      font-family: 'Space Mono', monospace;
      font-size: 0.78rem;
      color: var(--accent);
    }

    .status-time {
      margin-left: auto;
      font-family: 'Space Mono', monospace;
      font-size: 0.7rem;
      color: var(--muted);
    }

    /* TERMINAL BLOCK */
    .terminal {
      background: #08080e;
      border: 1px solid var(--border);
      border-left: 3px solid var(--accent);
      padding: 1.5rem;
      margin-bottom: 2rem;
      animation: fadeUp 0.7s ease 0.5s both;
    }

    .terminal-line {
      font-family: 'Space Mono', monospace;
      font-size: 0.78rem;
      line-height: 2;
      color: var(--muted);
    }

    .terminal-line .prompt { color: var(--accent); }
    .terminal-line .cmd    { color: var(--text); }
    .terminal-line .out    { color: var(--accent2); }

    /* FOOTER */
    .footer {
      font-family: 'Space Mono', monospace;
      font-size: 0.65rem;
      color: var(--muted);
      text-align: center;
      letter-spacing: 0.1em;
      animation: fadeUp 0.7s ease 0.6s both;
    }

    .footer span { color: var(--accent2); }

    /* ANIMATIONS */
    @keyframes fadeDown {
      from { opacity: 0; transform: translateY(-16px); }
      to   { opacity: 1; transform: translateY(0); }
    }

    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(16px); }
      to   { opacity: 1; transform: translateY(0); }
    }
  </style>
</head>
<body>
  <div class="container">

    <div class="badge-docker">CONTENEUR DOCKER ACTIF — PORT 5000</div>

    <h1 class="title">
      Bonjour à tous,<br>
      <span class="accent">Application</span><br>
      par <span class="name">Mbassi Elessa</span>
    </h1>

    <p class="subtitle">// Déployé avec Docker · Flask · Python 3.9</p>

    <div class="cards">
      <div class="card">
        <div class="card-label">Statut</div>
        <div class="card-value green">● En ligne</div>
      </div>
      <div class="card">
        <div class="card-label">Framework</div>
        <div class="card-value blue">Flask 3.x</div>
      </div>
      <div class="card">
        <div class="card-label">Plateforme</div>
        <div class="card-value">Docker</div>
      </div>
      <div class="card">
        <div class="card-label">Date de déploiement</div>
        <div class="card-value" style="font-size:1rem">{{ date }}</div>
      </div>
    </div>

    <div class="status-bar">
      <div class="dot"></div>
      <span class="status-text">Conteneur opérationnel — Aucune erreur détectée</span>
      <span class="status-time">{{ time }}</span>
    </div>

    <div class="terminal">
      <div class="terminal-line">
        <span class="prompt">$ </span>
        <span class="cmd">docker build -t franciskago-flask-app .</span>
      </div>
      <div class="terminal-line">
        <span class="out">✔ Successfully built · Image prête</span>
      </div>
      <div class="terminal-line">
        <span class="prompt">$ </span>
        <span class="cmd">docker run -p 5000:5000 franciskago-flask-app</span>
      </div>
      <div class="terminal-line">
        <span class="out">✔ Running on http://0.0.0.0:5000</span>
      </div>
    </div>

    <div class="footer">
      CC1 · CONDUITE DE PROJET · AGILE / DEVOPS / KANBAN ·
      <span>KEYCE INFORMATIQUE & IA</span>
    </div>

  </div>
</body>
</html>
"""

@app.route('/')
def home():
    now = datetime.now()
    return render_template_string(
        HTML_TEMPLATE,
        date=now.strftime("%d/%m/%Y"),
        time=now.strftime("%H:%M:%S")
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
