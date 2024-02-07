

from transformers import pipeline, logging
logging.set_verbosity_error()
import tensorflow as tf


def sentiment_analyzer(text):
    analyze = pipeline("text-classification", model="mehassan/finbert-finetuned")
    return analyze(text)