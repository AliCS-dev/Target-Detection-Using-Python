# Target Detection Using Python

A work-in-progress project for detecting objects/targets in video streams using **OpenCV** and **imutils**.  
This is currently a basic frame-by-frame video processing script that applies grayscale conversion, Gaussian blurring, and Canny edge detection to identify contours.

## 📌 Current Status

- ✅ Reads video from file (via `argparse`)
- ✅ Converts frames to grayscale
- ✅ Applies Gaussian blur
- ✅ Performs edge detection with Canny
- ✅ Finds contours
- 🚧 **To-do**: Add object detection logic, filtering noise, tracking targets, and drawing bounding boxes.

## 🛠 Requirements

- Python 3.x
- OpenCV
- imutils

Install dependencies:

```bash
pip install opencv-python imutils
▶ Usage
Run the script from the terminal:

bash
Copy
Edit
python target_detection.py --video path/to/video.mp4
Example:

bash
Copy
Edit
python target_detection.py --video sample.mp4
📂 Project Structure
bash
Copy
Edit
Target-Detection-Using-Python/
│
├── target_detection.py   # Main detection script
├── README.md             # Project documentation (this file)
└── requirements.txt      # Dependencies (to be added)
📝 To-Do List
 Add logic to highlight detected targets

 Implement bounding boxes and labels

 Add real-time webcam detection option

 Optimize detection parameters

 Save processed video output

 Create a GUI interface (optional)

📅 Development Log
Day 1: Basic video reading, grayscale conversion, blur, edge detection, and contour finding implemented.

Day 2+: To be updated daily...

⚠ This project is still in early development — results will improve over time as detection logic is added.
EOF
```
