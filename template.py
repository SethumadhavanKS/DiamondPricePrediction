import os
from pathlib import Path
packageName = 'DiamondPricePrediction'

lstOFFiles = [
    "github/workfloes/.gitkeep",
    f"src/{packageName}/__init__.py",
    f"src/{packageName}/components/__init__.py",
    f"src/{packageName}/components/dataIngestion.py",
    f"src/{packageName}/components/dataTransformation.py",
    f"src/{packageName}/components/modelTrainer.py",
    f"src/{packageName}/pipeline/__init__.py",
    f"src/{packageName}/pipeline/trainingPipeline.py",
    f"src/{packageName}/pipeline/predictionPipeline.py",
    f"src/{packageName}/logger.py",
    f"src/{packageName}/exception.py",
    f"src/{packageName}/utils/__init__.py",
    f"src/{packageName}/utils/utils.py",
    "notebooks/research.ipynb",
    "notebooks/data/.gitkeep",
    "requirements.txt",
    "setup.py",
    "init_setup.sh",
    "test.py"
]

#Creating directory
for filePath in lstOFFiles:
    filePath = Path(filePath)
    fileDir,fileName = os.path.split(filePath)

    if fileDir != "":
        os.makedirs(fileDir, exist_ok=True)
        
    #Creating file
    if(not os.path.exists(filePath)) or (os.path.getsize(filePath)==0):
        with open(filePath, "w") as f:
            pass
    else:
        print("File already exists")




