from django.shortcuts import redirect
import uuid
import datetime
from django.shortcuts import render
import authors.models as models


def add_author(request):
    """ Creates new domains and should be restricted to high level site admins only"""
    if request.method == 'POST':
        author_name = request.POST['author_name']
        dob =  request.POST['dob']

        date_added = datetime.datetime.utcnow()
        author_id = str(uuid.uuid4())

        new_author = models.Author(AuthorID=author_id,
                                   Name=author_name,
                                   DOB=datetime.datetime.strptime(dob, '%Y%m%d'),
                                   Date_Added=date_added,
                                   Books_Stored=0)

        new_author.save()

        # todo add proper redirect here
        return redirect('/authors/authors')
    else:
        return redirect('/authors/authors')


def add_book(request):
    """ Creates new domains and should be restricted to high level site admins only"""
    author_id = request.GET.get('author_id')
    if request.method == 'POST':
        book_title = request.POST['title']
        book_date = request.POST['release_date']

        converted_date = datetime.datetime.strptime(book_date, '%Y%m%d')

        new_book = models.Book(Title=book_title,
                               Publishing_Date=converted_date)

        author = models.Author.objects.get(AuthorID=author_id)
        current_books = author.Books
        current_books.append(new_book)

        author.Books_Stored = len(current_books)

        author.save()

        # todo add proper redirect here
        return redirect(f'/authors/books?author_id={author_id}')
    else:
        return redirect(f'/authors/books?author_id={author_id}')


def view_ind_author(request):
    """ Displays individual author metadata page """
    author_id = request.GET.get('author_id')

    author = models.Author.objects.get(AuthorID = author_id)
    books = author.Books

    return render(request, 'authors/ind_author_display.html', {'author' : author,
                                                               'books':books})


def view_authors(request):
    """Displays main author page"""
    try:
        authors = models.Author.objects()
    except:
        authors = []
    return render(request, 'authors/authors.html', {'authors' : authors})
