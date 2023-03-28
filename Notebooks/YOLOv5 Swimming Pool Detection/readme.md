<div style = "border-radius:10px; color: #3ABF5A; background-color: #3A3A3A">
    <h1 style  = "padding: 8px;">Swimming Pool Detection using YOLOv5</h1>
</div>

For some tasks, there are __pretrained models__ that are already trained on huge datasets using a vast computing resource. Trying to a build a model from scratch for such tasks may be reinventing the wheel. We can simply take the pretrained model and train it on our specific data for some time and get very good accuracy withing a few hours, which would have taken us weeks or even months if we had done all the model building and training from scratch.

[YOLOv5](https://github.com/ultralytics/yolov5) is a really great open-source objection detection model. Through __transfer-learning__, this model can be easily trained to a custom dataset for detecting the feature of our interest.

This tutorial will guide us on using this model for swimming pool  detection in satellite images.
