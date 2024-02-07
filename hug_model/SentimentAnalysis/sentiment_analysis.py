

from transformers import pipeline
from transformers import AutoTokenizer, logging
tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
logging.set_verbosity_error()

def sentiment_analyzer(text):
    
    analysis = pipeline("text-classification", model="mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis")
    return analysis(text)