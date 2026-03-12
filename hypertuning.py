from ultralytics import YOLO

model = YOLO('yolo11n.pt')
yaml_path = './dataset/data.yaml'

if __name__ == '__main__':
    model.tune(data=yaml_path, epochs=10, iterations=3, device="mps",
               lr0=1e-4, lrf=1e-2, optimizer='AdamW', plots=False, 
               save=False, val=False)
