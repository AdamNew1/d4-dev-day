from mongoengine import *

# Create your models here.
connect(db='d4')

class Author(Document):
    AuthorID = StringField()
    AuthorNumber = SequenceField(min_value=1)
    Name = StringField(max_length=50)
    DOB = DateTimeField()
    Date_Added = DateTimeField()
    Books_Stored = IntField(min_value=0)
    Books = EmbeddedDocumentListField('Book')

class Book(EmbeddedDocument):
    BookID = SequenceField(min_value=1)
    Title = StringField(max_length=100)
    Publishing_Date = DateTimeField()
