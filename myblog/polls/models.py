from django.db import models

#   notes = Note.objects.all() -- take all notes
#
#   note = Note(title='Заголовок', content='Содержимое заметки')
#   note.save() -- make new note
#
#   note = Note.objects.get(id=1)
#   note.delete() -- delete note
#
#

class Note(models.Model):
    note = models.CharField(max_length=400)
