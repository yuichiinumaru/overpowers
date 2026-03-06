from guidance.models import Transformers

lm = Transformers(
    "microsoft/Phi-4-mini-instruct",
    device="cuda"  # Or "cpu"
)
