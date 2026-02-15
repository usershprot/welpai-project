import os
import json
import random
from pathlib import Path
from openai import OpenAI

class WelpAi:
    def __init__(self):
        self.config_path = Path.home() / ".welpai_config"
        self._keys = [
            "csk-crjkkcey86dnjh3m9j8n5mymj49wekhr62nt8tf3tck5hjd5",
            "csk-4n9588jh4cyjrn8n6y8cfjk8mfw8yxe6wm9xkphnjmyny3mr",
            "csk-th8wnt28nc9tfcck6mjjmfkn4wf2f9j43v4mfe4rd3cmrcv8"
        ]
        self.models_data = {
            "gpt-oss": {"id": "gpt-oss-120b"},
            "llama-70b": {"id": "llama-3.3-70b"},
            "llama-8b": {"id": "llama3.1-8b"},
            "qwen": {"id": "qwen-3-32b"},
            "zai-glm": {"id": "zai-glm-4.7"}
        }
        self._base = "https://api.cerebras.ai/v1"
        self.client = OpenAI(
            base_url=self._base,
            api_key=random.choice(self._keys)
        )

    def get_saved_model(self):
        if self.config_path.exists():
            try:
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    return config.get("model", "gpt-oss-120b")
            except:
                pass
        return "gpt-oss-120b"

    def save_model(self, model_name):
        real_model = self.models_data.get(model_name, {}).get("id", model_name)
        config = {"model": real_model}
        with open(self.config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f)
        return real_model

    def chat(self, prompt, model=None):
        if not model:
            model = self.get_saved_model()
        try:
            response = self.client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model=model,
                max_tokens=4000
            )
            return response.choices[0].message.content
        except Exception as e:
            if "429" in str(e):
                return "❌ Слишком много запросов. Подождите немного."
            return "❌ Ошибка сервиса WelpAi. Попробуйте позже."
