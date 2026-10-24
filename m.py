import cv2

video_path = r"C:\Users\jdhar\Downloads\11988321_2160_3840_60fps.mp4"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Video not found!")
else:
    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 30

    print("Video opened successfully!")

    # Normal motion
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Normal Video", frame)

        if cv2.waitKey(max(1, int(1000 / fps))) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Slow motion
    cap = cv2.VideoCapture(video_path)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Slow Motion", frame)

        if cv2.waitKey(max(1, int(1000 / fps * 2))) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Fast motion
    cap = cv2.VideoCapture(video_path)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Fast Motion", frame)

        if cv2.waitKey(max(1, int(1000 / fps / 2))) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
