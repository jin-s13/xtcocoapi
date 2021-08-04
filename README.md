# Extended COCO API (xtcocotools)

## News

[2021.08.04] Release xtcocotools v1.10. Update installation dependencies.

[2021.07.22] Release xtcocotools v1.9. Merge some useful PRs from cocoapi.

[2021.05.19] Release xtcocotools v1.8. Fix CrowdPose evaluation.

[2021.03.22] Release xtcocotools v1.7. Support multi-part scores for COCO-WholeBody Dataset.

[2020.10.17] Release xtcocotools v1.6. Fix CrowdPose stats.

[2020.9.14] Release xtcocotools v1.5. Support COCO-WholeBody Dataset.

[2020.8.25] Release xtcocotools v1.0. Support COCO, AIChallenger, and CrowdPose Dataset.

## Introduction

COCO has become a standard annotation format for the task of person keypoint detection, and is widely used for multiple datasets.
Our Extended COCO API is developed based on [@cocodataset/cocoapi](https://github.com/cocodataset/cocoapi). 

We aim to provide a unified evaluation tools to support multiple human pose-related datasets, including [COCO](http://cocodataset.org/), [COCO-WholeBody](https://github.com/jin-s13/COCO-WholeBody), [CrowdPose](https://github.com/Jeff-sjtu/CrowdPose), [AI Challenger](https://github.com/AIChallenger/AI_Challenger_2017) and so on.

xtcocotools has been used in [MMPose](https://github.com/open-mmlab/mmpose) framework.

We provide a simple [demo_crowdpose](demos/demo_crowdpose.py) to evaluate on CrowdPose dataset; 
[demo_coco](demos/demo_coco.py) to evaluate on COCO dataset;
and [demo_coco_wholebody](demos/demo_coco_wholebody.py) to evaluate on COCO-WholeBody dataset;

## Requirements

- Linux (Windows is not officially supported)
- Python 3.6+ (Lower versions are not fully tested)

## Installation

To install from pip:
```shell
pip install xtcocotools
```

To install from source:
```shell
pip install -r requirements.txt
python setup.py install
```
