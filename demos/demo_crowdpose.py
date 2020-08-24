from xtcocotools.coco import COCO
from xtcocotools.cocoeval import COCOeval
import numpy as np

gt_file = '../annotations/example_crowdpose_val.json'
preds = '../annotations/example_crowdpose_preds.json'

sigmas = np.array([
            .79, .79, .72, .72, .62, .62, 1.07, 1.07, .87, .87, .89, .89, .79,
            .79
        ]) / 10.0

cocoGt = COCO(gt_file)
cocoDt = cocoGt.loadRes(preds)
cocoEval = COCOeval(cocoGt, cocoDt, 'keypoints_crowd', sigmas, use_area=False)
cocoEval.evaluate()
cocoEval.accumulate()
cocoEval.summarize()
