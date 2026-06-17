from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Data konten portfolio (mudah diubah tanpa menyentuh template)
# ---------------------------------------------------------------------------
PROFILE = {
    "name": "Alfi Hidayatur",
    "role": "Data Analyst",
    "location": "Surabaya, ID",
    "email": "hi.alfihidayatur@email.com",
    "linkedin": "https://www.linkedin.com/in/alfi-hidayatur/",
    "github": "https://github.com/alfiiiii/",
    "tagline": (
        "Get to know my professional journey, expertise, and areas of interest"
    ),
    "stats": [
        {"num": "1+",  "label": "Years Exp."},
        {"num": "10+", "label": "Projects"},
        {"num": "3x",  "label": "Industries"},
    ],
    "hero_skills": ["Python", "SQL", "Power BI", "Tableau", "Machine Learning", "ETL"],
    "tags": [
        "Python", "Forecasting Analysis", "Database",
        "Data Visualization", "Machine Learning", "SQL",
    ],
}

SKILLS = [
    {"icon": "🐍", "category": "Programming & Query", "list": ["Python", "SQL"]},
    {"icon": "📊", "category": "Visualization",       "list": ["Microsoft Power BI", "Tableau", "Microsoft Excel"]},
    {"icon": "⚙️", "category": "Data Engineering",    "list": ["Pentaho PDI", "MySQL"]},
    {"icon": "🛠️", "category": "Environment",         "list": ["Google Colab", "VS Code"]},
]

EXPERIENCE = [
    {
        "period": "January 2026 — Present",
        "role": "Digital Marketing Staff",
        "company": "PT Gajah Mitra Cemerlang",
        "points": [
            "Analyzed campaign performance across Shopee promotions, voucher programs, and Google Ads",
            "Evaluated key metrics including CTR, conversion rate, and ROAS",
            "Identified trends in customer behavior and campaign effectiveness",
            "Translated data into actionable insights to optimize marketing strategies",
            "Supported campaign improvements to increase conversion and overall performance",
        ],
    },
    {
        "period": "March 2024 — July 2024",
        "role": "Data Security & IT Governance Intern",
        "company": "PT PAL Indonesia",
        "points": [
            "Implemented COBIT 5 framework to strengthen IT governance",
            "Prepared IT audit reports with improvement recommendations",
            "Ensured alignment with industry standards and compliance requirements",
        ],
    },
    {
        "period": "August 2023 — January 2024",
        "role": "Database Developer Intern",
        "company": "BPS Kota Surabaya",
        "points": [
            "Designed database schema for statistical data management",
            "Oversaw database development and maintenance",
            "Created efficient SQL queries ensuring seamless functionality",
        ],
    },
]

PROJECTS = [
    {
        "num": "01",
        "title": "Flask-Based Stock Price Prediction Web App",
        "desc": ("Built a web-based application delivering stock price predictions through "
                 "an intuitive interface. Designed the frontend in HTML/CSS and implemented "
                 "Flask backend to integrate the prediction model. Users can input data, "
                 "generate forecasts, visualize results, and export PDF reports."),
        "tags": ["Flask", "HTML", "CSS", "Fuzzy Time Series", "LSTM"],
        "github": "#", "demo": "#",
    },
    {
        "num": "02",
        "title": "Hybrid Fuzzy Time Series + LSTM for Stock Prediction",
        "desc": ("Developed a hybrid forecasting model combining Fuzzy Time Series and "
                 "LSTM to capture both pattern-based and sequential behavior in stock "
                 "price data based on integracy of fuzzy logic with deep learning for stable, "
                 "interpretable results."),
        "tags": ["Python", "Fuzzy Time Series", "Fuzzy Rules", "LSTM"],
        "github": "#", "demo": "#",
    },
    {
        "num": "03",
        "title": "Market Basket Analysis",
        "desc": ("Combined K-Means clustering and Apriori association rule mining to segment transactions and identify product purchasing patterns for targeted marketing strategies."),
        "tags": ["Python", "Pandas", "Apriori", "Microsoft Power BI", "K-Means"],
        "github": "#", "demo": "#",
    },
    {
        "num": "04",
        "title": "Budget Optimization Analysis",
        "desc": ("Developed a predictive model using XGBoost to estimate campaign ROAS based on advertising performance metrics such as CTR, CPC, impressions, clicks, and conversions. The analysis helped identify high-potential campaigns and support more effective budget allocation decisions."),
        "tags": ["Python", "Prophet", "BigQuery"],
        "github": "#", "demo": "#",
    },
        {
        "num": "05",
        "title": "PDF Encryption & Decryption System",
        "desc": ("Developed a PDF security platform that enables password-protected encryption and decryption using AES and DES algorithms."),
        "tags": ["Python", "Flask", "AES", "DES", "Pypdf"],
        "github": "#", "demo": "#",
    },
        {
        "num": "06",
        "title": "Database Developer / Backend Developer for the Digital Integrated Statistics Service Platform",
        "desc": ("Designed the database architecture and implemented the Weighted Tree Similarity algorithm to improve document matching and information retrieval within the Digital Integrated Statistics Service Platform."),
        "tags": ["Python", "PostgreSQL", "SQL", "Weighted Tree Similarity", "NLP", "TF-IDF"],
        "github": "#", "demo": "#",
    },
        {
        "num": "07",
        "title": "Reinforcement Learning Based on Deep Q Learning For Atari GYM",
        "desc": ("Developed and optimized a Deep Q-Learning Network (DQN) model through hyperparameter tuning and performance evaluation in the Crazy Climber environment."),
        "tags": ["Python", "Deep Q-Learning Network", "Reinforcement Learning", "Hyperparameter Tuning", "Model Optimization"],
        "github": "#", "demo": "#",
    },
        {
        "num": "08",
        "title": "Cycle GAN Neural Transfer Image Processing",
        "desc": ("Applied preprocessing techniques including augmentation and normalization, developed a CycleGAN model for image-to-image transformation, and evaluated the quality and accuracy of the generated outputs."),
        "tags": ["Python", "Cycle GAN", "Generative Adversarial Networks", "Data Augmentation", "Deep Learning"],
        "github": "#", "demo": "#",
    },
        {
        "num": "09",
        "title": "Star Schema Modelling Based on Extract, Transform, Load",
        "desc": ("Designed a Star Schema and ETL process for docking data using Pentaho Data Integration, then created interactive Power BI dashboards to visualize operational insights."),
        "tags": ["ETL Process", "Pentaho Data Integration", "Microsoft Power BI"],
        "github": "#", "demo": "#",
    },
        {
        "num": "10",
        "title": "Forecasting Ship Docking Demand for Smarter Port Operations",
        "desc": ("Designed and implemented an ARIMA-based forecasting model to predict ship docking volumes and support efficient port management. By analyzing historical docking patterns and evaluating model performance, the project provides valuable insights into future operational demand. The forecasting results enable more proactive planning, better allocation of docking resources, and enhanced operational efficiency within maritime logistics environments."),
        "tags": ["Python", "ARIMA", "Time Series Forecasting", "Forecast Accuracy Evaluation"],
        "github": "#", "demo": "#",
    },
        {
        "num": "11",
        "title": "Wine Quality Prediction",
        "desc": ("Developed a wine quality classification model using the Naïve Bayes algorithm by analyzing wine attributes and calculating class probabilities to predict quality categories."),
        "tags": ["Python", "Naive Bayes", "Probability Calculation"],
        "github": "#", "demo": "#",
    },
        {
        "num": "12",
        "title": "Insurance Claim Risk Prediction",
        "desc": ("Developed a customer risk classification model using the K-Nearest Neighbors (KNN) algorithm to analyze customer attributes and predict appropriate insurance claim risk levels for data-driven decision-making."),
        "tags": ["Python", "K-Nearest Neighboars", "Risk Assessment", "Customer Segmentation"],
        "github": "#", "demo": "#",
    },
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        profile=PROFILE,
        skills=SKILLS,
        experience=EXPERIENCE,
        projects=PROJECTS,
    )


@app.route("/api/contact", methods=["POST"])
def contact():
    """Endpoint sederhana untuk menerima pesan dari form kontak (opsional)."""
    data = request.get_json(silent=True) or request.form
    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip()
    message = (data.get("message") or "").strip()

    if not name or not email or not message:
        return jsonify(ok=False, error="Semua field wajib diisi."), 400

    # TODO: simpan ke DB / kirim email. Untuk sekarang kita log saja.
    app.logger.info("New contact: %s <%s> — %s", name, email, message)
    return jsonify(ok=True, message="Terima kasih, pesan sudah terkirim!")


if __name__ == "__main__":
    app.run(debug=True)
