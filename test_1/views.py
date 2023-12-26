from django.shortcuts import render
from test_1.models import Category
from test_1.models import Page
from test_1.forms import CategoryForm
from test_1.forms import PageForm


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        page = Page.objects.filter(category=category)
        context_dict["pages"] = page
        context_dict["category"] = category
    except Category.DoesNotExist:
        context_dict["page"] = None
        context_dict["category"] = None

    return render(request, 'test_1/category.html', context_dict)


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!",
                    'categories': category_list,
                    'pages': page_list}

    return render(request, 'test_1/index.html', context=context_dict)


def add_category(request):
    form = CategoryForm
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)

    return render(request, 'test_1/add_category.html', {'form': form})
