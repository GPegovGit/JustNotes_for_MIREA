from firebase_admin import credentials, db, initialize_app

cred = credentials.Certificate('firebase-sdk.json')

initialize_app(cred, {

	'databaseURL': 'https://noteapp-6d019-default-rtdb.europe-west1.firebasedatabase.app'

})
userRef = db.reference('usersPC')
noteRef = db.reference('Note')


def addNoteFB(date, id1, text, title, username):
	noteRef.push({
		'date': date,
		'id': id1,
		'notes': text,
		'title': title,
		'username': username
	})


def addUserFB(username, password):
	userRef.push({
		'username': username,
		'password': password,
		'ID': 0
	})


def delNoteFB(id, login):
	data = noteRef.get()

	for key, val in data.items():
		if id == val['id'] and login == val['username']:
			delete_note_ref = noteRef.child(key)
			delete_note_ref.delete()
