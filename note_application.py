class NotesApplication(object):

	notes=[]
	def __init__(self, author):
		self.author= author

		def create(self, note_content):
			'''
			This function takes the note content as the parameter and adds it to the notes list of the object.
			 '''
			NotesApplication.notes.append(note_content)
			return NotesApplication.notes

		def list(self):
			'''
			This function lists out each of the notes in the notes list. i The note_id parameter below represents the respective index of each of the items in the list, the NOTE_CONTENT represent the note content and the author represents the note author
			'''
			for index in range(len(NotesApplication.note)):
				note_id= index
			

			#print ("NOTE ID: %s %s \n\n  by Author") % (note_id, NotesApplication.create())



		def get(self, note_id):
			'''
			This function takes a note_id which refers to the index of the note in the notes list and returns the content of that note as a 
			string.
			'''
			for entries in NotesApplication.notes:
				return NotesApplication.notes[note_id]

		def search(self, search_text):
			'''
			This function take a search string, search_text and returns all the notes with that text within it
			'''
			for index in range(len(NotesApplication.notes))
				if NotesApplication.notes[index].find(search_text) != -1:
					print NotesApplication.notes[index] #format!

		def delete(self, note_id): 
		'''
		 This function deletes the note at the index note_id of the notes list.
		'''
			
			if note_id in range(len(NotesApplication.notes)):
				NotesApplication.notes.pop(note_id)
				return NotesApplication.notes

		def edit(self, note_id, new_content):
		'''
		This function replaces the content in the note at note_id with new_content
		''' 
			if NotesApplication.notes[note_id] in NotesApplication.note:
				NotesApplication.notes[note_id]= new_content
			return NotesApplication.notes



