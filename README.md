# **APNR_And_ATCC_For_Smart_Traffic_Management_System**
This project implements Automatic Number Plate Recognition (ANPR) and Automatic Traffic Counting and Classification (ATCC) using deep learning for efficient traffic management. It enables vehicle detection, counting, and classification to optimize urban traffic flow and infrastructure planning.
## Table of Contents

- [Overview](#overview)
- [Directory Structure](#directory-structure)
- [Core Functionalities](#core-functionalities)
- [Technologies and Tools](#technologies-and-tools)
- [Installation Guide](#installation-guide)
- [How to Use](#how-to-use)
- [Results](#results)
- [License Information](#license-information)
- [Data](#data)

---

## Overview

This project employs Deep Learning and Object Detection techniques to facilitate intelligent traffic monitoring and management. The system utilizes ANPR (Automatic Number Plate Recognition) and ATCC (Automatic Traffic Counting and Classification) to:

- Optimize traffic flow
- Minimize congestion
- Improve road safety

## Directory Structure

The repository is organized as follows:


```
CV_Basics/                                # Basic learning materials on computer vision and OCR
Internship_artifacts/                                   # Agile documents, defect tracking, and unit testing
interpolated_results/test_interpolated/                    # CSV files for interpolated data visualization
number_plate_detection_model_training/               #training model to detect number plate
object_tracker/                                      # Core script for vehicle tracking in videos
pythonprograms/                                       #codes for different testing purposes
results/                                         # Initial detection CSV files for interpolation
utils/                                           # It helps for code reusability
.gitignore                                              # Specifies files and directories to be ignored by Git
add_missing_data.py                                     # Script for data interpolation
main.py                                                 # Generates initial detection data as CSV
requirements.txt                                        # List of project dependencies
visualize.py                                            # Script for video visualization using interpolated data
```


## Core Functionalities

- Recognition of vehicle license plates (ANPR)
- Classification and control of traffic (ATCC)
- Data interpolation for improved detection accuracy
- Generation of video outputs with traffic annotations

## Technologies and Tools

- **Programming Language**: Python
- **Libraries**: Listed in `requirements.txt`
- **Deep Learning**: Object detection models such as YOLO

## Installation Guide

### Prerequisites

Ensure the following are installed on your system:

- Python 3.8 or higher
- All necessary Python libraries (refer to `requirements.txt`)

### Setup Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/kurrisaimahitha/ANPR_And_ATCC_For_Smart_Traffic_Management_System.git
   ```
2. Navigate to the project folder:
   ```bash
   cd ANPR_And_ATCC_For_Smart_Traffic_Management_System
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Update the `.env` file with your secret keys.

## How to Use

1. Generate the initial detection CSV file by running `main.py`:
   ```bash
   python main.py
   ```
   - The generated file will be saved in the `results/` folder.

2. Perform data interpolation using `add_missing_data.py`:
   ```bash
   python add_missing_data.py
   ```
   - The interpolated CSV file will be saved in the `interpolated_results/` folder.

3. Visualize the results by executing `visualize.py`:
   ```bash
   python visualize.py
   ```
   - The annotated video output will be saved in the `output/` folder.


## Results

A sample output generated can be viewed here

- https://drive.google.com/file/d/1ixILM2HzAVR9AngmmGT8x74A2gZ5VWp2/view?usp=drive_link


## License Information

This project is distributed under the MIT License. Refer to the [LICENSE](LICENSE) file for more details.

## Data(video) used for testing (It's a large video, cannot be uploaded on github)

Video_link - https://drive.google.com/file/d/1ipFBmjLwo-lJMBU7F919-Ie8dxsQ9TSA/view?usp=drive_link

---

For questions or issues, visit the [Issues](https://github.com/kurrisaimahitha/Smart_Traffic_Management_System/issues) section.

