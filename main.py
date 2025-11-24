
import mediapipe as mp
import cv2
#from sklearn.metrics.pairwise import cosine_similarity

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
    ret, picture_bgr = cap.read()
    if not ret:
        break

    picture_rgb = cv2.cvtColor(picture_bgr, cv2.COLOR_BGR2RGB)
    
    # Process each frame with mediapipe pose
    result = pose.process(picture_rgb)

    if result.pose_landmarks:
        # Media pipe draws a connected skeleton between th  on each frame
        mp_drawing_utils.draw_landmarks(picture_bgr, result.pose_landmarks, mp_pose.POSE_CONNECTIONS) 
    
    cv2.imshow('MediaPipe Pose', picture_bgr)   
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
cap.release()
cv2.destroyAllWindows()

 
         
