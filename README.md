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

