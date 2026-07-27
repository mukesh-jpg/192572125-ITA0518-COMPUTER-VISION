import cv2

# Open the input video
cap = cv2.VideoCapture("Sample.mp4")

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(
    "M:\\COMPUTER VISION\\Lab Sessions\\py\\Fast_video.mp4",
    fourcc,
    fps,
    (width * 2, height * 2)
)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame (2x bigger)
    fast_frame = cv2.resize(frame, None, fx=2.0, fy=2.0)

    # Display
    cv2.imshow("Fast Video", fast_frame)

    # Save
    out.write(fast_frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()