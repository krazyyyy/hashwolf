from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator


from .models import User, Product

# Create your views here.
def index(request):
    try:
        product = Product.objects.all().order_by('?')
        paginator = Paginator(product, 12)

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