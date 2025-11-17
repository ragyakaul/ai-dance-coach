
import mediapipe as mp
import cv2


# Input and output paths
danceVideoPath = "/Users/ragyakaul/Desktop/Code/pythonprojects/aidancecoach"
outputPath = "/Users/ragyakaul/Desktop/Code/pythonprojects/aidancecoach"


# Initialize the Libraries 
# Use the pose estimation module conveniently
mp_pose = mp.solutions.pose 
# Creating a pose estimator object
pose = mp_pose.Pose() 
 # Draw the skeleton, joints and visualise pose on video frames
mp_drawing_utils = mp.solutions.drawing_utils



# Open the source video file
cap = cv2.VideoCapture("dance_video.MOV")


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process each frame with mediapipe pose
    result = pose.process(frame_rgb)

    if result.pose_landmarks:
        # Media pipe draws a connected skeleton between th  on each frame
        mp_drawing_utils.draw_landmarks(frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS) 
    
    cv2.imshow('MediaPipe Pose', frame)   
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
