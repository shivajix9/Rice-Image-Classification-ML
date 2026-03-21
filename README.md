🌾 Rice Image Classification – Machine Learning Project
This project builds a machine learning model to classify rice varieties using image processing and computer vision techniques. The goal is to automate rice grain identification, which can help improve efficiency in agriculture, food processing, and quality inspection. 
rice image
The project applies image preprocessing, feature extraction using HOG (Histogram of Oriented Gradients), model training, and hyperparameter tuning to achieve high classification accuracy.

📂 Dataset
Dataset: Rice Image Dataset
Total Images: 75,000
Number of Classes: 5 rice varieties
Rice Types
Arborio
Basmati
Ipsala
Jasmine
Karacadag

🧹 Data Preprocessing
Steps performed before training the models:
Loaded rice images
Resized images to 64 × 64 pixels
Converted images to grayscale
Applied HOG feature extraction to capture texture and shape patterns

🔧 Feature Engineering
HOG (Histogram of Oriented Gradients) parameters used:
Orientations: 9
Pixels per cell: 8 × 8
Cells per block: 2 × 2
Normalization: L2-Hys
Result:
Each image converted into a feature vector of ~1764 features. 

⚙️ Train-Test Split
Dataset was divided into:
80% Training Data
20% Testing Data
Additional preprocessing:
Label Encoding for target classes
StandardScaler for feature scaling 

🤖 Machine Learning Models Used
The following models were implemented and compared:
| Model          | Accuracy |
| -------------- | -------- |
| Random Forest  | 97.98%   |
| SVM            | 97.92%   |
| XGBoost        | 97.70%   |
| KNN            | 96.72%   |
| Gradient Boost | 96.39%   |
| Decision Tree  | 92.60%   |

Best Model: Random Forest (~98% accuracy) 

⚙️ Hyperparameter Tuning
GridSearchCV was used to optimize Random Forest parameters and improve performance.
Final accuracy after tuning: ~97.88%. 

🚀 Model Deployment
The trained model was saved using Joblib for deployment.
Saved files:
best_model.pkl
scaler.pkl
label_encoder.pkl

🌍 Applications
Rice quality inspection
Agricultural automation
Food industry sorting systems
Agriculture research tools 

⚠️ Challenges
Processing large image datasets
Feature extraction time
Model tuning
Handling lighting variations and image noise 

🔮 Future Improvements
Implement Deep Learning models (CNN) for better feature extraction and performance.

🛠 Tools & Technologies
Python
OpenCV / Image Processing
Scikit-learn
HOG Feature Extraction
Random Forest
Streamlit


