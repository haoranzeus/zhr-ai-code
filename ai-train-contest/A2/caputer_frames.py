import os
import cv2

def capture_frames(video_path, output_folder, frame_interval=30):
    os.makedirs(output_folder, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
      print(f"Error open video: {video_path}")
      return
    frame_count = 0
    saved_count = 0
    while True:
      ret, frame = cap.read()
      if not ret:
        break
      if frame_count % frame_interval == 0:
        output_path = os.path.join(output_folder, f"frame_{saved_count:04d}.jpg")
        # 实际保存的代码
        cv2.imwrite(output_path, frame)
        print(f"saved: {output_path}")
        saved_count += 1
      frame_count += 1
    print(f"捕获完毕， 总计保存{saved_count}张图片")
    cap.release()
    
    
if __name__ == "__main__":
    VIDEO_PATH = r"D:\work\workspace\ai-train-contest\code_practice\A2\mydata\video\video.mp4"
    OUTPUT_FOLDER = r"D:\work\workspace\ai-train-contest\practice\practice1\codes\A2\tmp"
    capture_frames(VIDEO_PATH, OUTPUT_FOLDER, frame_interval=30)