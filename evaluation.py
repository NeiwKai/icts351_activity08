from ultralytics import YOLO

# Load a model
model = YOLO("./best.pt")  # load a custom model

# Evaluate on validation or test dataset
metrics = model.val(
    data="./dataset/data.yaml",
    split="test"
)



