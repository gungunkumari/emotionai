import cv2
import numpy as np
import torch

from pytorch_grad_cam import GradCAM
from pytorch_grad_cam.utils.image import show_cam_on_image


class EmotionGradCAM:

    def __init__(self, model, target_layer):

        self.model = model
        self.cam = GradCAM(
            model=model,
            target_layers=[target_layer],
        )

    def generate(self, image_tensor):

        self.model.eval()

        grayscale_cam = self.cam(
            input_tensor=image_tensor
        )[0]

        image = image_tensor.squeeze().permute(1, 2, 0).cpu().numpy()

        image = (image - image.min()) / (image.max() - image.min())

        visualization = show_cam_on_image(
            image,
            grayscale_cam,
            use_rgb=True,
        )

        return visualization