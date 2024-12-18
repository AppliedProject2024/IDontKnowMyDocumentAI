import firebase_admin
from firebase_admin import credentials, auth

#global variable to track initialization of firebase app
firebase_initialized = False

def initFirebaseApp():
    #initialize firebase app if not already initialized
    global firebase_initialized
    if firebase_initialized:
        #create a firebase app if not already created
        cred = credentials.Certificate(r"C:\Users\keith\OneDrive\Desktop\IDKMD\firebase_credentials.json")
        #initialize firebase app
        firebase_admin.initialize_app(cred)
        #set flag to True
        firebase_initialized = True

def registerUser(email, password):
    #initialize firebase app
    initFirebaseApp()
    try:
        #create user with email and password
        user = auth.create_user(email = email, password = password)
        return f"user {user.email} created successfully"
    except Exception as e:
        return f"Error registering user: {e}"