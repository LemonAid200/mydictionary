import re
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("personaldictonary-firebase-adminsdk-bs22e-028bf63e69.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://personaldictonary-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# set the database
ref = db.reference('py/')
users = ref.child('users')


# #clears all data
# def clear_all_the_firebase():    
#     ref.set({})

#adds data to the users profile
def add_data(username, input, answer):
    user = users.child(str(username))
    user.update({
        input: answer
    })
    


# delete the user
def delete_the_user(username):
    user = users.child(str(username))
    user.delete()
    
 #returns storege of a user 
def get_users_data(username):
    answer = ref.child('users').child(str(username)).get()
    formated_answer = ''
    for key in answer:
        formated_answer += answer.get(key) + ' \n'
    return  formated_answer

    

    
    