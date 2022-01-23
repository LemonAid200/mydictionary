import re
import firebase_admin
import googletrans

from urbandictionaryapi import UrbanDictionary
from googletrans import Translator
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("personaldictonary-firebase-adminsdk-bs22e-028bf63e69.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://personaldictonary-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# set the database
ref = db.reference('py/')
users = ref.child('users')


# print(ref.get())
# print(users)





# delete the user
def delete_the_user(username):
    user = users.child(str(username))
    user.delete()
    
 #returns storege of a user 
def get_users_data(username):
    username = str(username)
    return  ref.child('users').child(username).get()

# answer = ref.child('users').child('757438981').get()


#adds data to the users profile
def add_data(username, input, answer):
    user = users.child(str(username))
    user.update({
        input: answer
    })

translator = Translator()


def translatethis(text):
    text = str(text)
    try:
        if translator.detect(text).lang == 'ru':
            resLang = 'en'
        else:
            resLang = 'ru'
        textResult = translator.translate(text, dest=resLang)
        print(textResult)
        return (text + ' → ' + textResult.text)
    except:
        raise Exception('Версия переводчика не актуальна')

print(UrbanDictionary.search('thing'))
print(UrbanDictionary.author())
