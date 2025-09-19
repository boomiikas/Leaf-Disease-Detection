import gradio as gr
import tensorflow as tf
import numpy as np
import pandas as pd
from PIL import Image

# ✅ Load trained model
model = tf.keras.models.load_model("best_potato_cnn.h5")

# Class labels (must match training order)
class_names = ["Potato___Early_blight", "Potato___Late_blight", "Potato___healthy"]

# ✅ Prediction function
def predict(image):
    img = image.resize((224, 224))   # same as training size
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)  # add batch dimension
    
    preds = model.predict(img)[0]   # shape (3,)
    
    # Map predictions to class labels
    result = {class_names[i]: float(preds[i]) for i in range(len(class_names))}
    
    # Sort results by probability (descending)
    sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    
    # For Label output
    predicted_class, confidence = sorted_result[0]
    
    # ✅ BarPlot wants DataFrame or list of dicts → use DataFrame
    df = pd.DataFrame(sorted_result, columns=["class", "confidence"])
    
    return {predicted_class: confidence}, df

# ✅ Custom HTML & CSS template
custom_css = """
body {background: #f9fafb; font-family: Arial, sans-serif;}
h1 {color: #2d3748; text-align: center;}
footer {text-align: center; margin-top: 20px; font-size: 14px; color: #718096;}
"""

custom_html = """
<h1>🌱 Potato Leaves Disease Classifier</h1>
<p style="text-align:center;">Upload a potato leaf image to detect Early Blight, Late Blight, or Healthy.</p>
"""

# ✅ Gradio Interface with bar chart
with gr.Blocks(css=custom_css) as demo:
    gr.HTML(custom_html)

    with gr.Row():
        with gr.Column():
            image_input = gr.Image(type="pil", label="Upload Potato Leaf")
            predict_btn = gr.Button("🔍 Predict")

        with gr.Column():
            top_label = gr.Label(label="Top Prediction")       # shows only best class
            bar_chart = gr.BarPlot(                           # ✅ now will render
                label="All Class Probabilities",
                x="class",
                y="confidence",
                vertical=True,
                x_label="Class",
                y_label="Probability",
                tooltip="confidence",
            )

    predict_btn.click(fn=predict, inputs=image_input, outputs=[top_label, bar_chart])

    gr.HTML("<footer>Made with  using TensorFlow & Gradio</footer>")

# ✅ Launch app
if __name__ == "__main__":
    demo.launch()
