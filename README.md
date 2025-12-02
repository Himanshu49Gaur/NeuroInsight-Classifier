# NeuroInsight Classifier

---

## 1. **Introduction**
- Alzheimer’s Disease (AD) is a progressive neurodegenerative disorder and a leading cause of dementia globally, gradually affecting memory, cognitive thinking, and behavioral abilities.
- Early diagnosis is crucial in slowing the progression of cognitive deterioration and supporting timely patient treatment planning.
- Traditional radiology-based diagnosis relies heavily on expert radiologists manually analyzing MRI scans, which can be time-consuming, subjective, and error-prone.
- This project presents an **AI-powered deep learning approach** using MRI brain scan classification to automate Alzheimer diagnosis, enabling faster and more accurate support for medical professionals.

---

## 2. **Problem Statement**
- Manual MRI analysis struggles with consistency and scalability due to the increasing number of dementia patients.
- Misinterpretation or delayed diagnosis leads to late treatment initiation, reducing patient recovery quality.
- Medical centers face radiologist shortages and require automated systems for evaluation.
- Therefore, there is a need for a **reliable, automated classification system** capable of detecting Alzheimer’s disease progression accurately and efficiently.

---

## 3. **Objectives**
- To build a high-performance Alzheimer classification model using deep learning.
- To classify MRI images into multiple severity categories of dementia.
- To automate and improve diagnostic reliability compared to manual visual assessment.
- To deliver a reproducible research-ready workflow for clinical and academic use.
- To measure performance using scientific evaluation metrics and visual comparison methods.

---

## 4. **Proposed Solution**
- A **Convolutional Neural Network (CNN)** architecture based on **ResNet-50 transfer learning** is trained on labeled Alzheimer MRI datasets.
- The model learns structural brain abnormalities associated with different dementia stages.
- It predicts MRI classes categorized into:
  - **Non-Demented**
  - **Very Mild Demented**
  - **Mild Demented**
  - **Moderate Demented**
- Optimization and GPU acceleration are used to ensure model accuracy and efficiency.
- The solution provides a complete end-to-end training, testing, evaluation, and visualization pipeline inside a single Jupyter notebook.

---

## 5. **Methodology**
### 🔹 *Step 1 – Dataset Acquisition*
- Alzheimer MRI dataset obtained from **OASIS / Kaggle Brain MRI public dataset**.
- Contains labeled MRI scans categorized by dementia severity for supervised training.

### 🔹 *Step 2 – Data Preprocessing*
- MRI images resized to **224×224 pixels** for CNN compatibility.
- Pixel normalization applied to improve training stability.
- Dataset split into **80% training** and **20% validation** partitions.
- Data augmentation (random rotation, flipping, shifting) applied to address class imbalance.

### 🔹 *Step 3 – Model Architecture*
- Utilizes **ResNet-50 pretrained on ImageNet** to leverage powerful feature extraction.
- Final fully connected layers redefined for 4-class classification.
- Core components:
  - Loss Function: **Cross-Entropy**
  - Optimizer: **Adam**
  - Batch Normalization & Dropout to reduce overfitting
  - CUDA GPU acceleration for improved performance

### 🔹 *Step 4 – Model Training*
- Runs for multiple epochs with real-time monitoring of training & validation curves.
- Learning rate scheduling and early stopping strategies used.
- Uses PyTorch DataLoader pipeline for efficient mini-batch processing.
