# 🌾 Rice Image Classification – Machine Learning Project

This project builds a machine learning model to classify rice varieties using image processing and computer vision techniques.  
The goal is to automate rice grain identification, improving efficiency in agriculture, food processing, and quality inspection.

---

## 📌 Overview
The project applies:
- Image preprocessing
- Feature extraction using HOG (Histogram of Oriented Gradients)
- Model training and evaluation
- Hyperparameter tuning

---

## 📂 Dataset
- **Dataset:** Rice Image Dataset  
- **Total Images:** 75,000  
- **Classes:** 5 rice varieties  

### 🌾 Rice Types
- Arborio  
- Basmati  
- Ipsala  
- Jasmine  
- Karacadag  

---

## 🧹 Data Preprocessing
- Loaded rice images  
- Resized images to **64 × 64 pixels**  
- Converted images to grayscale  
- Applied HOG feature extraction  

---

## 🔧 Feature Engineering
**HOG Parameters:**
- Orientations: 9  
- Pixels per cell: 8 × 8  
- Cells per block: 2 × 2  
- Normalization: L2-Hys  

👉 Each image is converted into a feature vector of approximately **1764 features**

---

## ⚙️ Train-Test Split
- **80% Training Data**
- **20% Testing Data**

Additional steps:
- Label Encoding  
- Feature scaling using StandardScaler  

---

## 🤖 Models & Performance

| Model            | Accuracy |
|------------------|----------|
| Random Forest    | 97.98%   |
| SVM              | 97.92%   |
| XGBoost          | 97.70%   |
| KNN              | 96.72%   |
| Gradient Boost   | 96.39%   |
| Decision Tree    | 92.60%   |

🏆 **Best Model:** Random Forest (~98% accuracy)

---

## ⚙️ Hyperparameter Tuning
- Used **GridSearchCV**  
- Optimized Random Forest parameters  
- Final accuracy: **~97.88%**

---

## 🚀 Deployment
The trained model was saved using Joblib for deployment.

Saved files:
- `best_model.pkl`
- `scaler.pkl`
- `label_encoder.pkl`

📌 *Note: Model files are provided in the Releases section.*

---

## 🌍 Applications
- Rice quality inspection  
- Agricultural automation  
- Food industry sorting systems  
- Research tools  

---

## ⚠️ Challenges
- Large dataset processing  
- Feature extraction time  
- Model tuning  
- Lighting variations and image noise  

---

## 🔮 Future Improvements
- Implement Deep Learning (CNN) for better performance  
- Improve robustness to lighting variations  

---

## 🛠️ Tech Stack
- Python  
- OpenCV  
- Scikit-learn  
- HOG Feature Extraction  
- Random Forest  
- Streamlit  

---

## 🤝 Contribution
Contributions are welcome!



