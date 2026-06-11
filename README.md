# Health Prediction App

A full-stack application that demonstrates CRUD operations with patient records, integrates a machine learning model for health risk prediction, and provides a Streamlit frontend for visualization.

---

## 🚀 Tech Stack
- **FastAPI**: Backend REST API
- **MySQL**: Database (via SQLAlchemy ORM)
- **Streamlit**: Frontend dashboard
- **scikit-learn**: Machine learning model
- **Python-dotenv**: For environment variable management

---

## 📂 Project Structure
health-prediction-app/
│
├── backend/
│   ├── main.py          # FastAPI app
│   ├── database.py      # DB connection
│   ├── models.py        # SQLAlchemy models
│   ├── crud.py          # CRUD operations
│   ├── ml_model.py      # ML prediction logic
│   └── train_dataset.py # Training script
│
└── frontend/
└── app.py           # Streamlit UI


---

## ⚙️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/health-prediction-app.git
   cd health-prediction-app

2. **Create virtual environment**
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. **Install dependencies**
pip install -r requirements.txt

4. **Create .env file (not committed to GitHub)**

DATABASE_URL=mysql://user:password@localhost/health_db
SECRET_KEY=your_secret_here

5. **Run backend**
uvicorn backend.main:app --reload
6. **Run frontend**
streamlit run frontend/app.py

**Features**
> Create: Add new patient records
> Read: View patient records and ML predictions
> Update: Modify patient details
> Delete: Remove patient records
> Visualization: Pie chart of risk distribution

**Security Note**
No API keys or secrets are committed to GitHub.
All sensitive values must be stored in .env.

## 🔬 Model & Data
- The trained model (`health_model.pkl`) and full dataset are **not included** in this repo for size/privacy reasons.
- To train your own model:
  ```bash
  python backend/train_dataset.py
