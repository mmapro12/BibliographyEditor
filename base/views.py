from django.shortcuts import render, redirect
from .models import Book


# Create your views here.
def home(request):
    # Fetch all Book objects from the database
    books = Book.objects.all()
    
    # Pass the books to the template and render it
    context = {'books': books}
    return render(request, 'base/home.html', context)

def addBook(request):
    if request.method == 'POST':
        # Process the form data here
        author_nickname = request.POST.get('nickname') # Meşhur isim
        author_full_name = request.POST.get('name') # Tam isim
        book_name = request.POST.get('book')# Kitap Adı
        skin = request.POST.get('cilt') # Cilt
        print_place = request.POST.get('p_place') # Basım yeri
        printer = request.POST.get('printer') # Yayıncı
        print_year = request.POST.get('date') # yıl
        press = request.POST.get('press') # Baskı
        thk = request.POST.get('thk') # Tahkik

        
        # Create a new Book object and save it to the database
        book = Book(
            author_nickname=author_nickname, 
            author_full_name=author_full_name, 
            book_name=book_name, 
            skin=skin, 
            print_place=print_place, 
            printer=printer, 
            print_year=print_year, 
            press=press, 
            thk=thk,
            )
        
        # Save the book to the database
        book.save()

        # return redirect('home')

    return render(request, 'base/add_book.html')


def ranking(request, pk):
    books = Book.objects.all()
    rank = str(pk)

    context = {'books': books, 'ranking': rank}
    return render(request, 'base/ranking.html', context)

