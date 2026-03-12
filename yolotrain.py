from ultralytics import Yolo

model = YOLO('yolo11n.pt')

yaml_path = 'data.yaml'

if __name__ == '__main__':
    results = model.train(data=yaml_path, epoch=10, imgsz=640)
