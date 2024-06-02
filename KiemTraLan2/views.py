from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from KiemTraLan2.forms import DanhMucForm,ThongTinBuoiTiec,ThongTinLienHeForm
from .models import DanhMuc,SanPham
# Create your views here.
def dsdm(request):
    form = DanhMucForm()
    if request.method == 'POST':
        form = DanhMucForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')  # type: ignore # Thay thế bằng URL tương ứng của bạn
    else:
       data = {
            'form':form,
            'DanhMuc' : DanhMuc.objects.all(),
       }
    return render(request, 'DSDanhMuc.html', data)

def xemchitietdm(request, MaDanhMuc):
    data = {
       'products' : SanPham.objects.all().filter(MaDanhMuc = MaDanhMuc),
    }
    return render(request, 'DSSanPham.html',data)

def dssp(request):
    data = {
            'products' : SanPham.objects.all(),
       }
    return render(request, 'DSSanPham.html', data)


def xemchitiet(request, MaSanPham):
    product = get_object_or_404(SanPham, pk=MaSanPham)
    return render(request, 'ChiTietSanPham.html', {'product': product})


def themvaogiohang(request, product_id):
    product = get_object_or_404(SanPham, pk=product_id)
    quantity = int(request.POST.get('quantity', 1))

    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += quantity
    else:
        cart[str(product_id)] = {
            'product_id': product_id,
            'name': product.TenSanPham,
            'price': product.Gia,
            'quantity': quantity
        }

    request.session['cart'] = cart
    return redirect('donhang')

def donhang(request):
    cart = request.session.get('cart', {})
    cart_items = []

    for item_id, item_data in cart.items():
        product = get_object_or_404(SanPham, pk=item_id)
        cart_items.append({
            'product': product,
            'quantity': item_data['quantity'],
            'item_price': item_data['price'] * item_data['quantity']
        })

    total_quantity = sum(item['quantity'] for item in cart_items)
    total_price = sum(item['item_price'] for item in cart_items)

    return render(request, 'Giohang.html', {
        'cart_items': cart_items,
        'total_quantity': total_quantity,
        'total_price': total_price
    })

def hoanthanh(request):
    if request.method == 'POST' or request.method == 'GET':
        request.session['cart'] = {}

    return redirect('donhang')


def ThemThongTinBuoiTiec(request):
    formttnd = ThongTinLienHeForm()
    formbuoitiec = ThongTinBuoiTiec()
    data={
        'ttnd' : formttnd,
        'ttbt' : formbuoitiec,
    } # type: ignore
    return render(request, 'ThongTinDatTiec.html', data)