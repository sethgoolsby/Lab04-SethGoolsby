import pickle

notes = []

# TODO: Using the pickle module...

# A. If notes.pickle exists, read it in using pickle and assign the content to
#   the notes variable
try: 
	notes = pickle.load(open("notes.pickle","rb")) 
except Exception:
	pass

# B. Print out notes
print(notes)
# C. Read in a string from the user using input() and append it to notes
notes += input("Enter in something to your notes")
# D. Save notes to notes.pickle
with open("notes.pickle","wb") as f:
	pickle.dump(notes,f)