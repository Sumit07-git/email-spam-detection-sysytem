import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import streamlit as st

class SpamDetector:
    def __init__(self):
        self.data= None
        self.model= None
        self.cv= None

    def load_and_train(self):
        """Load and train model"""
        try:



            self.data=pd.read_csv("spam.csv")

            self.data.drop_duplicates(inplace=True)
            self.data['Category']= self.data['Category'].replace(['ham','spam'],['Not Spam','Spam'])

            mess= self.data['Message']
            cat= self.data['Category']

            (mess_train,mess_test,cat_train,cat_test)= train_test_split(mess,cat,test_size=0.2)

            self.cv= CountVectorizer(stop_words= 'english')
            features=self.cv.fit_transform(mess_train)

        #model

            self.model= MultinomialNB()
            self.model.fit(features, cat_train)

            return True
        
        except Exception as e:
            st.error(f"Error in loading data: {e}")
            return False

#prdict

    def predict(self,message):
        input_message= self.cv.transform([message]).toarray()


        result=self.model.predict(input_message)
        return result[0]


    def get_stats(self):
        if self.data is not None:
            total=len(self.data)
            spam=len(self.data[self.data['Category']== 'Spam'])
            safe=len(self.data[self.data['Category']== 'Not Spam'])

            return {

                'total': total,
                'spam': spam,
                'safe': safe
            }
        return{'total': 0,'spam': 0, 'safe':0}
        






