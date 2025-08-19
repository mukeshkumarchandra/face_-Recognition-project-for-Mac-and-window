# 🔍 Face Recognition System  

A simple **real-time face recognition system** built with Python, [`opencv-python`](https://pypi.org/project/opencv-python/), and [`face_recognition`](https://github.com/ageitgey/face_recognition).  
The system uses your webcam to detect and recognize faces based on a collection of known images stored in the `knowns/` directory.  

---

## ✨ Features  

- 🎥 **Real-Time Face Recognition** – Detects and identifies faces from a live webcam feed.  
- 🖼️ **Face Data Collection** – Utility script (`collect.py`) to capture and save images of known individuals.  
- 📦 **Organized Structure** – All known faces stored in the `knowns/` folder, automatically loaded during recognition.  
- ⚡ **Optimized for Speed** – Resizes frames to improve performance without losing accuracy.  
- 🚨 **Error Handling** – Checks for missing directories, empty datasets, and unreadable images.  

---

## 🛠️ Installation & Setup  

### 1. Clone the Repository  
```bash
git clone https://github.com/your-username/face-recognition-system.git
cd face-recognition-system
```

### 2. Create Conda Environment  
```bash
conda create -n facerec python=3.11.8
```
Press **Y** when prompted.  

Activate the environment:  
```bash
conda activate facerec
```

### 3. Install Dependencies  
```bash
pip install annotated-types==0.7.0 anyio==4.10.0 click==8.2.1 dlib==20.0.0 face-recognition==1.3.0 face_recognition_models==0.3.0 fastapi==0.116.1 idna==3.10 numpy==2.2.6 opencv-python==4.12.0.88 pandas==2.3.1 pillow==11.3.0 pydantic==2.11.7 pydantic_core==2.33.2 python-dateutil==2.9.0.post0 pytz==2025.2 six==1.17.0 sniffio==1.3.1 starlette==0.47.2 typing-inspection==0.4.1 typing_extensions==4.14.1 tzdata==2025.2 uv==0.8.11
```

---

## 🚀 Usage  

The workflow involves **collecting known faces** and then **running recognition**.  

### 1. Collect Face Data  
Run the `collect.py` script to capture face images:  
```bash
python collect.py
```
- Press **S** → Save the current frame as an image.  
- Press **Q** → Quit the collection script.  
- Images are stored in the `knowns/` folder.  
- Rename saved files to match the person’s name (e.g., `mukesh.jpg`).  

### 2. Run Face Recognition  
After collecting face data, start recognition:  
```bash
python face_recognize.py
```
- Webcam window opens.  
- Green box appears around detected faces.  
- **Recognized faces** → Name label shown.  
- **Unknown faces** → Labeled as `"Unknown"`.  
- Press **Q** → Quit recognition.  

---

## 📂 Project Structure  

```
.
├── collect.py           # Script to capture and save known faces
├── face_recognize.py    # Main script for real-time recognition
├── knowns/              # Directory for storing known face images
└── README.md            # Documentation
```

---

## ⚙️ Code Overview  

### 🔹 `collect.py` – Face Data Collector  
- Uses webcam to capture face images.  
- Saves snapshots into the `knowns/` folder.  
- Allows manual control (save/quit) via keyboard.  

### 🔹 `face_recognize.py` – Real-Time Recognition  
1. **Load Known Faces**  
   - Reads all images from `knowns/`.  
   - Extracts face encodings and stores them with labels.  
   - Skips invalid/missing faces with warnings.  

2. **Webcam Processing**  
   - Captures live video stream.  
   - Converts frames to RGB (required by `face_recognition`).  
   - Resizes frames (`FRAME_RESIZE = 0.25`) to speed up detection.  

3. **Recognition Logic**  
   - Detects faces in each frame.  
   - Compares against known encodings.  
   - Uses **face distance** metric with threshold (`0.6`) to decide matches.  

4. **Display Output**  
   - Draws bounding boxes around detected faces.  
   - Displays recognized name or `"Unknown"`.  
   - Updates in real-time.  

5. **Exit Condition**  
   - Press **Q** to terminate gracefully.  

---

## 📌 Notes  

- Collect multiple images per person for better accuracy.  
- Use clear, well-lit images for reliable recognition.  
- You can tweak the recognition threshold (`0.6`) in `face_recognize.py`:  
  - Lower → Stricter match (fewer false positives).  
  - Higher → More tolerant (may mislabel).  
- Works best with a good webcam and proper lighting.  

---

## 🖥️ Demo (Optional)  

📷 *(You can add screenshots or a short demo GIF here once you test it on your system)*  
