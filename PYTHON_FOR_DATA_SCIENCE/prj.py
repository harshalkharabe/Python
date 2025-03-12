import cv2
import numpy as np
import mediapipe as mp
import os

# Initialize Mediapipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Load all T-shirt images from the directory
tshirt_dir = "D:/TUTORIAL/PYTHON FULL STACK/PYTHON/PYTHON_FOR_DATA_SCIENCE/Shirts"
tshirt_files = sorted([f for f in os.listdir(tshirt_dir) if f.endswith(".png")])
tshirt_images = [cv2.imread(os.path.join(tshirt_dir, f), cv2.IMREAD_UNCHANGED) for f in tshirt_files]

# Track current T-shirt index
current_tshirt_index = 0

# Define button positions
left_button_pos = (50, 300)  # (x, y)
right_button_pos = (550, 300)
button_radius = 40

def overlay_transparent(background, overlay, x, y):
    """Overlay transparent image on the background."""
    h, w, _ = overlay.shape
    bh, bw, _ = background.shape

    # Ensure overlay does not go out of bounds
    if x + w > bw:
        w = bw - x
    if y + h > bh:
        h = bh - y

    overlay_resized = cv2.resize(overlay, (w, h))
    alpha = overlay_resized[:, :, 3] / 255.0  # Extract alpha channel

    for c in range(3):  # Apply blending for RGB channels
        background[y:y + h, x:x + w, c] = np.clip(
            alpha * overlay_resized[:, :, c] + (1 - alpha) * background[y:y + h, x:x + w, c], 0, 255
        )
    
    return background

# Mouse click event function
def mouse_click(event, x, y, flags, param):
    global current_tshirt_index
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if left button clicked
        if ((x - left_button_pos[0])**2 + (y - left_button_pos[1])**2) < (button_radius**2):
            current_tshirt_index = (current_tshirt_index - 1) % len(tshirt_images)
        
        # Check if right button clicked
        elif (x - right_button_pos[0])**2 + (y - right_button_pos[1])**2 < button_radius**2:
            current_tshirt_index = (current_tshirt_index + 1) % len(tshirt_images)

# Open Camera
cap = cv2.VideoCapture(0)
cv2.namedWindow("Virtual Try-On")
cv2.setMouseCallback("Virtual Try-On", mouse_click)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert to RGB for Mediapipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = pose.process(rgb_frame)

    if result.pose_landmarks:
        landmarks = result.pose_landmarks.landmark

        # Get key points
        left_shoulder = (int(landmarks[11].x * frame.shape[1]), int(landmarks[11].y * frame.shape[0]))
        right_shoulder = (int(landmarks[12].x * frame.shape[1]), int(landmarks[12].y * frame.shape[0]))
        left_hip = (int(landmarks[23].x * frame.shape[1]), int(landmarks[23].y * frame.shape[0]))
        right_hip = (int(landmarks[24].x * frame.shape[1]), int(landmarks[24].y * frame.shape[0]))

        # Calculate midpoints for better alignment
        chest_center = ((left_shoulder[0] + right_shoulder[0]) // 2, (left_shoulder[1] + right_shoulder[1]) // 2)
        torso_height = abs(left_hip[1] - chest_center[1])

        # T-shirt dimensions
        tshirt_width = abs(right_shoulder[0] - left_shoulder[0]) * 2
        tshirt_height = int(torso_height * 1.4)  # Extend slightly for better fit

        # Resize and overlay T-shirt
        tshirt_resized = cv2.resize(tshirt_images[current_tshirt_index], (tshirt_width, tshirt_height))
        frame = overlay_transparent(frame, tshirt_resized, chest_center[0] - tshirt_width // 2, chest_center[1])

    # Draw clickable buttons
    cv2.circle(frame, left_button_pos, button_radius, (255, 0, 0), -1)  # Left button
    cv2.circle(frame, right_button_pos, button_radius, (255, 0, 0), -1)  # Right button
    cv2.putText(frame, "<", (left_button_pos[0] - 15, left_button_pos[1] + 10), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)
    cv2.putText(frame, ">", (right_button_pos[0] - 15, right_button_pos[1] + 10), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)

    # Show Output
    cv2.imshow("Virtual Try-On", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()