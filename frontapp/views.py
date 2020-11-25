from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout



from .models import User, Product, Blog

# Create your views here.
def index(request):
    try:
        product = Product.objects.all().order_by('?')
        paginator = Paginator(product, 8)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except ObjectDoesNotExist:
        product = None
    return render(request, 'frontapp/index.html', {
        'product' : product,
        'products' : page_obj
    })

def products(request):
    return render(request, 'frontapp/allproducts.html',{
        'product' :Product.objects.all().order_by('?')
    })

def blog_page(request):
    try:
        blog = Blog.objects.all()
    except ObjectDoesNotExist:
        blog = None
    return render(request, 'frontapp/blogs.html', {
        'blog' : blog
    })

def blog_single(request, pk):
    blog = Blog.objects.get(id=pk)
    return render(request, 'frontapp/blog.html', {
        'blog' : blog
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "forntapp/login.html",{
                "message" : "Invalid Username and/or password"
            })
    else:
        return render(request, 'frontapp/login.html')

def register_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except:
            return render(request, 'frontapp/register.html', {
                "message" : "Username Already Taken"
            })
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'frontapp/register.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

# def how(request):
#     return render(request, 'frontapp/how.html')


# def about(request):
#     return render(request, 'frontapp/about.html')

# def product(request, pk):
#     product = Product.objects.get(id=pk)
#     return render(request, 'frontapp/product.html', {
#         'product' : product
#     })

# def likeView(request):
#     if request.method == "POST":
#         if request.method == 'POST':
#         data = json.loads(request.body)
#         user = User.objects.get(id=request.user.id)
#         post = Post.objects.get(id=data['like_id'])
#         if data['span'] == 'Like':
#             post.likes.add(user)
#         else:
#             post.likes.remove(user)
#             print(data)
#         response = dict(like=post.likes.count())
#         return JsonResponse(response, status=201)