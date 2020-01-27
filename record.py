import cv2

video_capture = cv2.VideoCapture(0)

ret, frame = video_capture.read()
h, w = frame.shape[:2]

# Create an output movie file (make sure resolution/frame rate matches input video!)
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
output_movie = cv2.VideoWriter('output.mp4', fourcc, 20.0, (w, h))

while True:
    ret, frame = video_capture.read()

    cv2.imshow('Video', frame)
    output_movie.write(frame)
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()