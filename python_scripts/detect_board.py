import os

model_file = "/proc/device-tree/model"

if os.path.exists(model_file):
    with open(model_file, "r") as f:
        board = f.read().replace("\x00", "").strip()

    print("Board:", board)
else:
    print("Board information not found")
