import joblib
import spacy  # type: ignore


class Setup:
    """Loads the model and required dependencies. Prepares the model for making predictions
    """
    __nlp = spacy.load("en_core_web_sm")

    def __init__(self) -> None:
        # load model
        self.__model = joblib.load(
            "./machine_learning/spam_text_class/logistic_regression.pkl")
        # load tfidf vectorizer
        self.__tfidf_vect = joblib.load(
            "./machine_learning/spam_text_class/tfidf_vectorizer.pkl")

    def predict(self, text: str) -> float:
        # clean the text
        text_clean = self.__remove_junk(self.__nlp(text))
        # transform it to vectors
        text_vect = self.__tfidf_vect.transform([text_clean])
        # make predictions
        predictions = self.__model.predict_proba(text_vect.reshape(1, -1))

        # return spam probability
        return predictions[0, 1]

    def __remove_junk(self, doc) -> str:
        # will hold cleaned text
        cleaned = ""

        # iterating through all the tokens
        for token in doc:
            # junk
            if token.is_space or token.is_punct or token.is_stop:
                pass
            # data
            else:
                # add base form of token
                cleaned += ' '
                cleaned += token.lemma_

        # return clean text
        return cleaned
