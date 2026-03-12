Suppanat Timngarm 6688132

## Requirement
1.  Unzip the "ITCS351_Lecture08.v1i.yolov11.zip".
2.  Put the unzip contents into the "dataset" directory as structure below.

### Structure
```
.
├── best.pt
├── dataset
│   ├── data.yaml
│   ├── test
│   ├── train
│   └── valid
├── evaluation.py
├── hypertuning.py
├── ITCS351_Lecture08.v1i.yolov11.zip
├── test_car.mp4
├── yolo11n.pt
├── yolotrain.py
```

### Testing
```bash
yolo task=detect mode=predict  data=dataset/data.yaml  source=test_car.mp4 model=best.pt device=0 save=True
```
