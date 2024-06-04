from textSummarizer.config.configuration import ConfigrationManager
from transformers import AutoTokenizer
from transformers import pipeline


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigrationManager().get_model_evaluation_config()


    def predict(self, text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}

        pipe = pipeline("Summarization", model=self.config.model_path, tokenizer=tokenizer)

        print("Dialogue: ")
        print(text)

        output = pipe(text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Sumamry: ")
        print(output)

        return output