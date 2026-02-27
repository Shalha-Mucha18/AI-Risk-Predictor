<div align="center">

# 🚗 AI-Risk-Predictor

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?logo=docker)
![AWS](https://img.shields.io/badge/AWS-EC2%20%7C%20ECR%20%7C%20S3-orange?logo=amazonaws)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-black?logo=githubactions)

An end-to-end **MLOps project** that predicts whether a vehicle insurance customer will respond positively to a cross-sell policy offer — helping insurers target the right customers and reduce marketing costs.

The model is trained on real-world customer data including demographics, vehicle details, and insurance history. It uses a **RandomForestClassifier** with **SMOTEENN** to handle class imbalance, and is evaluated against the production model in S3 before deployment.


🌐 **Live Demo:** `http://13.236.136.147:5000`

</div>

---


## 🎯 Project Workflow Summary

```
Data Ingestion ➔ Data Validation ➔ Data Transformation
      ➔ Model Training ➔ Model Evaluation ➔ Model Deployment
            ➔ CI/CD Automation (GitHub Actions + Docker + AWS)
```

---

## 📁 Project Setup and Structure

### Step 1 — Project Template
Execute `template.py` to scaffold the initial folder structure and placeholder files.

### Step 2 — Package Management
Configure local package imports in `setup.py` and `pyproject.toml`.

> 💡 See `crashcourse.txt` for a guide on these files.

### Step 3 — Virtual Environment & Dependencies

```bash
conda create -n vehicle python=3.10 -y
conda activate vehicle
pip install -r requirements.txt
pip list   # verify local packages are installed
```

---

## 📊 MongoDB Setup

### Step 4 — MongoDB Atlas Configuration
1. Sign up at [MongoDB Atlas](https://www.mongodb.com/atlas) and create a new project
2. Set up a free **M0 cluster**, configure username/password
3. Allow access from any IP: `0.0.0.0/0`
4. Copy the Python connection string (replace `<password>`)

### Step 5 — Push Data to MongoDB
- Create a `notebook/` folder, add your dataset
- Use `mongoDB_demo.ipynb` to push data to the database
- Verify under **Database → Browse Collections**

---

## 📝 Logging, Exception Handling & EDA

### Step 6 — Logging & Exception Handling
Create logging and exception modules. Test them via `demo.py`.

### Step 7 — Exploratory Data Analysis
Perform EDA and feature engineering in the `EDA and Feature Engg` notebook.

---

## 📥 Data Ingestion

### Step 8 — Data Ingestion Pipeline
- Define MongoDB connection in `configuration/mongo_db_connections.py`
- Build ingestion logic in `data_access/` and `components/data_ingestion.py`
- Update `entity/config_entity.py` and `entity/artifact_entity.py`

**Set environment variables before running:**

```bash
# Bash / Linux / macOS
export MONGODB_URL="mongodb+srv://<username>:<password>@cluster.mongodb.net/"

# PowerShell (Windows)
$env:MONGODB_URL = "mongodb+srv://<username>:<password>@cluster.mongodb.net/"
```

> **Windows users:** You can also set variables via System Properties → Environment Variables.

```bash
python demo.py
```

---

## 🔍 Data Validation, Transformation & Model Training

### Step 9 — Data Validation
Define schema in `config/schema.yaml`. Implement validation in `utils/main_utils.py`.

### Step 10 — Data Transformation
Implement transformation logic in `components/data_transformation.py`. Create `entity/estimator.py`.

### Step 11 — Model Training
Implement training in `components/model_trainer.py` using `estimator.py`.

---

## 🌐 AWS Setup

### Step 12 — IAM & Credentials
1. Create an IAM user with **AdministratorAccess** in the AWS Console
2. Set credentials as environment variables:

```bash
export AWS_ACCESS_KEY_ID="YOUR_KEY"
export AWS_SECRET_ACCESS_KEY="YOUR_SECRET"
```

3. Update `constants/__init__.py` with your S3 bucket name

### Step 13 — S3 Bucket & Model Storage
- Create an S3 bucket (e.g. `prdection1`) in `ap-southeast-2`
- Implement S3 push/pull in `cloud_storage/aws_storage.py` and `entity/s3_estimator.py`

---

## 🚀 Model Evaluation, Pusher & Prediction

### Step 14 — Model Evaluation & Model Pusher
Implement evaluation (F1 score vs. production) and model push to S3. Build the prediction pipeline and wire up `app.py`.

### Step 15 — Web UI
Add `static/` (CSS) and `templates/` (HTML/Jinja2) directories for the frontend.

---

## 🔄 CI/CD — Docker, GitHub Actions & AWS

### Step 16 — Docker & GitHub Actions
- Create `Dockerfile` and `.dockerignore`
- Add the following secrets in **GitHub → Settings → Secrets → Actions**:

| Secret | Value |
|--------|-------|
| `AWS_ACCESS_KEY_ID` | Your IAM access key |
| `AWS_SECRET_ACCESS_KEY` | Your IAM secret key |
| `AWS_DEFAULT_REGION` | `ap-southeast-2` |
| `ECR_REPO` | ECR repository name |
| `MONGODB_URL` | MongoDB Atlas connection string |

### Step 17 — EC2 & ECR Setup
1. Launch an Ubuntu EC2 instance
2. Open ports `5000`, `80`, `443`, `22` in Security Group
3. Install Docker on EC2:

```bash
sudo apt-get update && sudo apt-get install docker.io -y
sudo usermod -aG docker ubuntu
newgrp docker
```

4. Register EC2 as a **self-hosted GitHub runner**:

```bash
mkdir actions-runner && cd actions-runner
curl -o actions-runner-linux-x64.tar.gz -L \
  https://github.com/actions/runner/releases/download/v2.317.0/actions-runner-linux-x64-2.317.0.tar.gz
tar xzf ./actions-runner-linux-x64.tar.gz
./config.sh --url https://github.com/Shalha-Mucha18/AI-Risk-Predictor --token YOUR_TOKEN
./run.sh
```

### Step 18 — Final Deployment
- Ensure port `5000` is open in the EC2 Security Group
- Access the live app: `http://<your-ec2-public-ip>:5000`

---

## 📁 Project Structure

```
├── src/
│   ├── components/        # Pipeline components (ingestion, training, etc.)
│   ├── pipline/           # Training & prediction pipelines
│   ├── entity/            # Config, artifact & estimator entities
│   ├── cloud_storage/     # AWS S3 utilities
│   ├── data_access/       # MongoDB data access layer
│   └── constants/         # App-wide constants
├── templates/             # HTML templates (Jinja2)
├── static/                # CSS & static assets
├── config/                # Schema & model configs
├── notebook/              # EDA & MongoDB demo notebooks
├── .github/workflows/     # CI/CD GitHub Actions workflow
├── Dockerfile
├── app.py                 # FastAPI application entry point
└── demo.py                # Training pipeline runner
```

---

## 🛠️ Tech Stack

| Layer | Tools |
|-------|-------|
| ML | scikit-learn, imbalanced-learn (SMOTEENN) |
| API | FastAPI, Uvicorn |
| Database | MongoDB Atlas |
| Cloud | AWS S3, ECR, EC2 |
| CI/CD | GitHub Actions |
| Container | Docker |

---

## 💬 Connect

If you found this project helpful, feel free to ⭐ the repo and reach out!
