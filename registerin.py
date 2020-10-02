from firebase import firebase

firebase=firebase.FirebaseApplication('https://flight-search-fadaf.firebaseio.com/',None)


Username = input("enter Username")
password = input("enter password")


data = {"Username":Username,"Password":password}

result = firebase.post('/Login/',data)
print(result)