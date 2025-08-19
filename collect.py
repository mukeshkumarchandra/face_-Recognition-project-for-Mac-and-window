import cv2
import os
import face_recognition

# Folder to save captured faces
SAVE_DIR = '/Users/mukeshkumarchandra/Desktop/uv- video/mkcode/knowns'

# Ask for name
name = input("Enter the name for this face: ").strip()

# Create folder if it doesn't exist
os.makedirs(SAVE_DIR, exist_ok=True)

# Start webcam
video = cv2.VideoCapture(0)
if not video.isOpened():
    raise RuntimeError("❌ Could not open webcam. Grant Camera permission in macOS Settings.")

print("📸 Press 's' to save the face image, 'q' to quit.")

while True:
    ret, frame = video.read()
    if not ret:
        continue

    rgb_frame = frame[:, :, ::-1]  # Convert BGR to RGBq
    face_locations = face_recognition.face_locations(rgb_frame, model="hog")

    # Draw rectangle around detected faces
    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    cv2.imshow("Face Capture", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s') and face_locations:
        # Save the first detected face image
        (top, right, bottom, left) = face_locations[0]
        face_img = frame[top:bottom, left:right]
        save_path = os.path.join(SAVE_DIR, f"{name}.jpg")
        cv2.imwrite(save_path, face_img)
        print(f"✅ Saved {save_path}")
        break

    elif key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

