import cv2
from PIL import Image
from util import get_limits

# Define colors and their names
colors = {
    "Yellow": [0, 255, 255],
    "Red": [0, 0, 255],
    "Blue": [255, 0, 0],
    "Green": [0, 255, 0]
}

cap = cv2.VideoCapture(0)

# Initialize a dictionary to store the bounding boxes for smoothing
bbox_dict = {color: None for color in colors}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for color_name, bgr_color in colors.items():
        lowerLimit, upperLimit = get_limits(color=bgr_color)
        mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
        mask_ = Image.fromarray(mask)
        bbox = mask_.getbbox()

        if bbox is not None:
            x1, y1, x2, y2 = bbox
            bbox_dict[color_name] = (x1, y1, x2, y2)
        else:
            bbox_dict[color_name] = None

    # Draw rectangles and labels for detected colors
    for color_name, bbox in bbox_dict.items():
        if bbox is not None:
            x1, y1, x2, y2 = bbox
            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
            cv2.putText(frame, color_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow('frame', frame)

    # Quit condition
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
