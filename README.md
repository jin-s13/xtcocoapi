# Extended COCO API (xtcocotools)

## Introduction
COCO has become a standard annotation format for the task of person keypoint detection, and is widely used for multiple datasets.
Our Extended COCO API is developed based on [@cocodataset/cocoapi](https://github.com/cocodataset/cocoapi). 

We aim to provide a unified evaluation tools to support multiple human pose-related datasets, including [COCO](http://cocodataset.org/), [CrowdPose](https://github.com/Jeff-sjtu/CrowdPose), [AI Challenger](https://github.com/AIChallenger/AI_Challenger_2017) and so on.

We provide a simple [demo_crowdpose](demos/demo_crowdpose.py) to evaluate on CrowdPose dataset; and [demo_coco](demos/demo_coco.py) to evaluate on COCO dataset.

## Installation
To install from pip:
```shell
pip install xtcocotools
```

To install from source:
```shell
make
```
