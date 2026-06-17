# Portfolio Alfi Hidayatur — Flask

Struktur:
```
portfolio/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    └── css/
        └── style.css
```

## Cara menjalankan
```bash
pip install -r requirements.txt
python app.py
```
Buka http://127.0.0.1:5000

Semua konten (profil, skills, pengalaman, proyek) diatur di dictionary
`PROFILE`, `SKILLS`, `EXPERIENCE`, dan `PROJECTS` di `app.py` — edit di sana
tanpa perlu mengubah template.
