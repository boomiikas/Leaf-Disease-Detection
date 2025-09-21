# 🌱 Leaf Disease Detection  

This project is a **Deep Learning-based Potato Leaf Disease Classifier** built using **TensorFlow** and deployed with **Gradio**.  
**DEMO LINK :** https://huggingface.co/spaces/boomiikas/Leaf-Disease-Detection
**Source :** https://www.kaggle.com/datasets/emmarex/plantdisease

It can classify potato leaf images into three categories:  
- **Potato___Early_blight** 🍂  
- **Potato___Late_blight** 🍁  
- **Potato___healthy** 🌿  

---

## 📊 Model Training Details  

- **Architecture**: Custom CNN built with TensorFlow/Keras  
- **Batch Size**: `64`  
- **Epochs**: `32`  
- **Training Accuracy**: `95.48%`  
- **Validation Accuracy**: `89.53%`  

The trained model is saved as:  
```bash
best_potato_cnn.h5
```

---

## 🚀 Project Structure  

```
Leaf-Disease-Detection/
│── app.py               # Gradio app for deployment
│── best_potato_cnn.h5   # Trained CNN model
│── requirements.txt     # Python dependencies
│── README.md            # Project documentation
```

---

## ⚙️ Installation  

Clone the repository and install dependencies:  

```bash
git clone https://github.com/boomiikas/Leaf-Disease-Detection.git
cd Leaf-Disease-Detection
pip install -r requirements.txt
```

---

## ▶️ Running the App  

```bash
python app.py
```

The Gradio app will launch, and you can open it in your browser.  

---
## App Screenshot

<img width="1915" height="827" alt="image" src="https://github.com/user-attachments/assets/56e4c737-eefa-47c0-8fee-a31c8551c2a3" />

---

## 🖼️ Usage  

1. Upload a potato leaf image (`.jpg`, `.png`).  
2. The model predicts whether the leaf is **Early Blight**, **Late Blight**, or **Healthy**.  
3. The UI is styled with **custom HTML & CSS** for better UX.  

---

## 📦 Requirements  

Listed in **requirements.txt**:  
- tensorflow  
- gradio  
- pillow  
- numpy  

---

## ✨ Example Prediction  

| Input Image | Predicted Output |
|-------------|------------------|
| Healthy Leaf 🌿 | `Potato___healthy (98%)` |
| Early Blight 🍂 | `Potato___Early_blight (92%)` |
| Late Blight 🍁 | `Potato___Late_blight (95%)` |

---

## 📜 License  

This project is licensed under the MIT License.  
