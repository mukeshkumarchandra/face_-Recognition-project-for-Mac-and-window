import os
import face_recognition
import cv2
import numpy as np

# --- Configuration and Setup ---
# Use a valid, absolute path for the known faces directory
# Make sure this path is correct for your system.
KNOWN_DIR = '/Users/mukeshkumarchandra/Desktop/uv- video/mkcode/knowns'  # Change this to your known faces directory

# Reduce frame size to speed up processing
FRAME_RESIZE = 0.25 
MODEL = "hog"

# --- Load known faces ---
# Add error handling to check if the directory exists and if there are images
if not os.path.exists(KNOWN_DIR):
    print(f"Error: The directory '{KNOWN_DIR}' does not exist.")
    exit()

known_encodings = []
known_names = []
image_files = [f for f in os.listdir(KNOWN_DIR) if f.lower().endswith((".jpg", ".jpeg", ".png"))]

if not image_files:
    print(f"No valid image files found in '{KNOWN_DIR}'. Please add some known faces.")
    exit()

for filename in image_files:
    path = os.path.join(KNOWN_DIR, filename)
    try:
        img = face_recognition.load_image_file(path)
        encodings = face_recognition.face_encodings(img)
        if encodings:
            known_encodings.append(encodings[0])
            known_names.append(os.path.splitext(filename)[0])
        else:
            print(f"Warning: Could not find a face in {filename}. Skipping.")
    except Exception as e:
        print(f"Error processing {filename}: {e}")

print(f"Loaded {len(known_encodings)} known faces.")

# --- Video Capture and Processing ---
# Use a specific video device index (e.g., 0)
video_capture = cv2.VideoCapture(0)

# Check if the camera was opened successfully
if not video_capture.isOpened():
    print("Error: Could not open video stream. Check your webcam connection or permissions.")
    exit()

print("Press 'q' to exit the video window.")

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Error: Failed to grab frame from video stream.")
        break

    # Convert the frame from BGR to RGB (face_recognition library requires RGB)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Resize frame for faster face detection
    small_frame = cv2.resize(rgb_frame, (0, 0), fx=FRAME_RESIZE, fy=FRAME_RESIZE)

    # Find all the faces and face encodings in the current frame
    face_locations = face_recognition.face_locations(small_frame, model=MODEL)
    face_encodings = face_recognition.face_encodings(small_frame, face_locations)

    face_names = []
    for encoding in face_encodings:
        if not known_encodings:
            face_names.append("Unknown")
            continue

        # Compare the current face encoding with all known face encodings
        distances = face_recognition.face_distance(known_encodings, encoding)

        # Find the best match
        best_match_index = np.argmin(distances)
        name = "Unknown"
        # The threshold for recognition. Adjust this value (0.6 is a good starting point)
        # Lower values mean a stricter match.
        if distances[best_match_index] <= 0.6:
            name = known_names[best_match_index]

        face_names.append(name)
        
    # --- Draw boxes and names on the original frame ---
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up the face locations to match the original frame size
        top = int(top / FRAME_RESIZE)
        right = int(right / FRAME_RESIZE)
        bottom = int(bottom / FRAME_RESIZE)
        left = int(left / FRAME_RESIZE)

        # Draw the box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (0, 0, 0), 1)

    # --- Display the resulting image ---
    cv2.imshow("Face Recognition", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# --- Cleanup ---
video_capture.release()
cv2.destroyAllWindows()