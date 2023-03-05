import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification


class Setup:
    """Loads the model and required dependencies. Prepares the model for making predictions
    """
    # huggingface model
    __MODEL = "cardiffnlp/twitter-roberta-base-sentiment-latest"
    # fine tuned model
    __local_model = "./domain/models/movie_review/movie_review_model"

    def __init__(self) -> None:
        # load tokenizer
        self.__tokenizer = AutoTokenizer.from_pretrained(self.__MODEL)
        # load model
        self.__model = AutoModelForSequenceClassification.from_pretrained(
            self.__local_model)

    def __softmax(self, x):
        return(np.exp(x)/np.exp(x).sum())

    def predict(self, text: str) -> str:
        # creating tokens
        inputs = self.__tokenizer(
            text, padding=True, truncation=True, max_length=512, return_tensors='pt')
        # making prediction
        outputs = self.__model(**inputs)
        # applying softmax
        predictions = self.__softmax(outputs.logits.data.numpy())

        # return label
        return predictions[0, 1]
