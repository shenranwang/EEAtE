# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import json
import math

class ActionAnswerQuestion(Action):

    def __init__(self):
        self.data = pd.read_csv("EFFECT training data .csv", sep=';')
        self.model = SentenceTransformer('bert-base-nli-mean-tokens')

    def name(self) -> Text:
        return "action_answer_question"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print(self.data)
        sentences = self.data.iloc[:, 0]
        user_question = tracker.latest_message['text']

        sentence_embeddings = self.model.encode([user_question] + sentences.tolist())
        similarity = cosine_similarity([sentence_embeddings[0]], sentence_embeddings[1:])
        print("Similarity of questions:", similarity[0])
        matched_question_idx = similarity[0].tolist().index(max(similarity[0]))
        response = self.data.loc[matched_question_idx]["Response Text"]
        print("Question:", self.data.loc[matched_question_idx]["Questions/Query"])
        print("Response:", response)
        if not response:
            dispatcher.utter_message(text="I do not have an answer for that.")
        else:
            dispatcher.utter_message(text=response)

        return []
