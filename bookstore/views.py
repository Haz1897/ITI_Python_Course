from django.shortcuts import render, redirect


BOOKS = [
    {
        "id": 1,
        "title": "The Pragmatic Programmer",
        "author": "David Thomas & Andrew Hunt",
        "description": "A guide to software craftsmanship covering topics from personal responsibility to career development.",
        "pages": 352,
        "price": 49.99,
    },
    {
        "id": 2,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "description": "A handbook of agile software craftsmanship focused on writing readable, maintainable code.",
        "pages": 431,
        "price": 39.99,
    },
    {
        "id": 3,
        "title": "Design Patterns",
        "author": "Gang of Four",
        "description": "Elements of reusable object-oriented software — the classic reference for software design patterns.",
        "pages": 395,
        "price": 54.99,
    },
]

_next_id = 4  


def _get_book(book_id):
    return next((b for b in BOOKS if b["id"] == book_id), None)

def book_list(request):
    return render(request, "list.html", {"books": BOOKS})

def book_detail(request, book_id):
    book = _get_book(book_id)
    return render(request, "details.html", {"book": book})

def book_create(request):
    if request.method == "POST":
        global _next_id
        new_book = {
            "id": _next_id,
            "title": request.POST.get("title", "").strip(),
            "author": request.POST.get("author", "").strip(),
            "description": request.POST.get("description", "").strip(),
            "pages": int(request.POST.get("pages", 0)),
            "price": float(request.POST.get("price", 0.0)),
        }
        BOOKS.append(new_book)
        _next_id += 1
        return redirect("book_list")
    return render(request, "form.html", {"action": "Add", "book": {}})

def book_edit(request, book_id):
    book = _get_book(book_id)

    if request.method == "POST":
        book["title"] = request.POST.get("title", "").strip()
        book["author"] = request.POST.get("author", "").strip()
        book["description"] = request.POST.get("description", "").strip()
        book["pages"] = int(request.POST.get("pages", 0))
        book["price"] = float(request.POST.get("price", 0.0))
        return redirect("book_detail", book_id=book_id)

    return render(request, "form.html", {"action": "Edit", "book": book})

def book_delete(request, book_id):
    book = _get_book(book_id)

    if request.method == "POST":
        BOOKS.remove(book)
        return redirect("book_list")

    return render(request, "confirm_delete.html", {"book": book})