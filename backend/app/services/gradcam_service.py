from pathlib import Path
import uuid

import cv2
import numpy as np
import torch
from PIL import Image


class GradCAMService:
    def __init__(self, model):
        self.model = model
        self.model.eval()

        self.gradients = None
        self.activations = None

        # Last convolution layer of your CNN
        target_layer = self.model.features[12]

        target_layer.register_forward_hook(self.forward_hook)
        target_layer.register_full_backward_hook(self.backward_hook)

    def forward_hook(self, module, input, output):
        self.activations = output

    def backward_hook(self, module, grad_input, grad_output):
        self.gradients = grad_output[0]

    def generate(
        self,
        input_tensor,
        predicted_class,
        original_image_path,
    ):
        self.model.zero_grad()

        output = self.model(input_tensor)

        score = output[:, predicted_class]

        score.backward()

        gradients = self.gradients.detach().cpu().numpy()[0]
        activations = self.activations.detach().cpu().numpy()[0]

        weights = np.mean(gradients, axis=(1, 2))

        cam = np.zeros(activations.shape[1:], dtype=np.float32)

        for i, w in enumerate(weights):
            cam += w * activations[i]

        cam = np.maximum(cam, 0)

        cam = cv2.resize(cam, (224, 224))

        cam = cam - cam.min()

        cam = cam / (cam.max() + 1e-8)

        heatmap = np.uint8(255 * cam)

        heatmap = cv2.applyColorMap(
            heatmap,
            cv2.COLORMAP_JET
        )

        original = cv2.imread(original_image_path)

        original = cv2.resize(original, (224, 224))

        overlay = cv2.addWeighted(
            original,
            0.6,
            heatmap,
            0.4,
            0
        )

        output_dir = Path("outputs/gradcam")
        output_dir.mkdir(parents=True, exist_ok=True)

        filename = f"{uuid.uuid4()}.png"

        save_path = output_dir / filename

        cv2.imwrite(str(save_path), overlay)

        return str(save_path)