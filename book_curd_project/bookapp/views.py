from django.shortcuts import render,redirect
from bookapp.models import Book


# Create your views here.
def index(request):
    books=Book.objects.all()
    # print(type(books))
    # print(books)
    context={}
    context['books']=books
    return render(request,'index.html',context)

def addBook(request):
    print('method: ',request.method)
    if request.method=='GET':
        return render(request,'addbook.html')
    else:
        t=request.POST['Book_Name']
        a=request.POST['Author_Name']
        p=request.POST['Price']
        print(t,a,p)
        book=Book.objects.create(title=t,author=a,price=p)
        book.save()
        return redirect('/')
    
def deleteBook(request,bookid):
    book=Book.objects.filter(id=bookid)
    book.delete()
    return redirect('/')

def updateBook(request,bookid):
    if request.method=="GET":
        book=Book.objects.get(id=bookid)
        context={"book":book}
        return render(request,'updatebook.html',context)
    else: #post
        t=request.POST['Book_Name']
        a=request.POST['Author_Name']
        p=request.POST['Price']
        print(t,a,p)
        book=Book.objects.filter(id=bookid)
        book.update(title=t,author=a,price=p)
        return redirect('/')