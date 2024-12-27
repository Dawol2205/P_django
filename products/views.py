from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from .models import Product, Hashtag
from .forms import ProductForm
from django.http import JsonResponse
from django.urls import reverse
from django.contrib import messages

@login_required
def delete(request, pk):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        product = get_object_or_404(Product, pk=pk)
        if request.user == product.user:
            product.delete()
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error', 'message': '권한이 없습니다.'}, status=403)
    return redirect('products:index')

def index(request):
    sort = request.GET.get('sort', 'latest')
    search = request.GET.get('search', '')
    
    products = Product.objects.all()
    
    if search:
        products = products.filter(
            Q(title__icontains=search) |
            Q(content__icontains=search) |
            Q(user__username__icontains=search) |
            Q(hashtags__name__icontains=search)
        ).distinct()
    
    if sort == 'popularity':
        products = products.order_by('-likes', '-created_at')
    else:
        products = products.order_by('-created_at')
        
    context = {
        'products': products,
        'sort': sort,
        'search': search,
    }
    return render(request, 'products/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            
            # 해시태그 처리
            hashtag_names = form.cleaned_data['hashtags'].split(',')
            for name in hashtag_names:
                name = name.strip()
                if name:
                    hashtag, created = Hashtag.objects.get_or_create(name=name)
                    product.hashtags.add(hashtag)
            
            return redirect('products:detail', product.pk)
    else:
        form = ProductForm()
    return render(request, 'products/form.html', {'form': form})

def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.view_count += 1
    product.save()
    
    context = {
        'product': product,
    }
    return render(request, 'products/detail.html', context)

@login_required
def update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user != product.user:
        return redirect('products:detail', pk)
        
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            # 해시태그 처리
            product = form.save(commit=False)
            product.save()
            
            # 기존 해시태그 삭제
            product.hashtags.clear()
            
            # 새로운 해시태그 추가
            hashtag_input = form.cleaned_data.get('hashtags', '')
            if hashtag_input:
                hashtag_names = [tag.strip() for tag in hashtag_input.split(',')]
                for name in hashtag_names:
                    if name:
                        hashtag, created = Hashtag.objects.get_or_create(name=name)
                        product.hashtags.add(hashtag)
                    
            return redirect('products:detail', product.pk)
    else:
        form = ProductForm(instance=product)
        # 기존 해시태그를 폼에 표시
        form.fields['hashtags'].initial = ','.join([tag.name for tag in product.hashtags.all()])
    
    context = {
        'form': form,
        'product': product,
    }
    return render(request, 'products/form.html', context)

def search_hashtags(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        query = request.GET.get('query', '')
        hashtags = Hashtag.objects.filter(name__icontains=query)[:5]
        data = [{'id': tag.id, 'name': tag.name} for tag in hashtags]
        return JsonResponse(data, safe=False)
    return JsonResponse({'error': 'Invalid request'}, status=400)

@login_required
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user == product.user:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            product.delete()
            return JsonResponse({
                'status': 'success',
                'message': '물품이 성공적으로 삭제되었습니다.',
                'redirect_url': reverse('products:index')  # reverse import 필요
            })
        product.delete()
        messages.success(request, '물품이 성공적으로 삭제되었습니다.')
        return redirect('products:index')
    messages.error(request, '삭제 권한이 없습니다.')
    return redirect('products:detail', pk)

@login_required
def like(request, pk):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        product = get_object_or_404(Product, pk=pk)
        if request.user in product.likes.all():
            product.likes.remove(request.user)
            is_liked = False
        else:
            product.likes.add(request.user)
            is_liked = True
            
        context = {
            'is_liked': is_liked,
            'like_count': product.likes.count(),
        }
        return JsonResponse(context)
    return redirect('products:detail', pk)