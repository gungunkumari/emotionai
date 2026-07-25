from transformers import AutoModelForCausalLM, AutoProcessor
import torch


class FlorenceExplainer:

    def __init__(self):

        self.device = (
            "cuda"
            if torch.cuda.is_available()
            else "cpu"
        )

        self.processor = AutoProcessor.from_pretrained(
            "microsoft/Florence-2-base"
        )

        self.model = AutoModelForCausalLM.from_pretrained(
            "microsoft/Florence-2-base",
            trust_remote_code=True,
        ).to(self.device)

    def explain(self, image):

        prompt = (
            "<MORE_DETAILED_CAPTION>"
        )

        inputs = self.processor(
            text=prompt,
            images=image,
            return_tensors="pt",
        ).to(self.device)

        generated = self.model.generate(
            **inputs,
            max_new_tokens=128,
        )

        result = self.processor.batch_decode(
            generated,
            skip_special_tokens=True,
        )[0]

        return result