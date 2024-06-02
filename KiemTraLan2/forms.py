import os
from django import forms # type: ignore

from TranVanTinh_2001216219 import settings # type: ignore
from .models import DanhMuc
class DanhMucForm(forms.Form):
    TenDanhMuc = forms.CharField(label='Tên Danh Mục',max_length=100)
    def clean_TenDanhMuc(self):
        TenDanhMuc = self.cleaned_data['TenDanhMuc']
        try:
            DanhMuc.objects.get(TenDanhMuc = TenDanhMuc)
        except DanhMuc.DoesNotExist:
            return TenDanhMuc
        raise forms.ValidationError("Danh mục đã tồn tại! ")
    def save(self):
        DanhMuc.objects.create(TenDanhMuc = self.cleaned_data['TenDanhMuc'])

class ThongTinLienHeForm(forms.Form):
    TenDanhMuc = forms.CharField(label='Họ tên bé',max_length=100)
    TenNguoiDat = forms.CharField(label='Họ tên người đặt',max_length=100)
    SoDienThoai = forms.CharField(label='số điện thoại',max_length=100)
    Email = forms.CharField(label='email',max_length=100)

class ThongTinBuoiTiec(forms.Form):
    diadiem = (
        ('diaiem', 'tphcm'),
        ('diadiem', 'hanoi'),
    )
    diadiem1 = (
        ('diaiem', 'tan phu'),
        ('diadiem', 'tan binh'),
    )
    diadiem2 = (
        ('diaiem', 'phu tho'),
        ('diadiem', ' tay thanh'),
    )
    
    LoaiTiec = (
        ('sinhnhat', 'tiệc sinh nhật'),
        ('lienhoan', 'tiệc liên hoan'),
    )
    LoaiTiec = forms.MultipleChoiceField(choices=LoaiTiec,
                                                    widget=forms.RadioSelect,
                                                    required=False)
    ngay = forms.DateField(widget=forms.SelectDateWidget())
    soluong = forms.IntegerField(min_value=0)
    
    tp = forms.ChoiceField(choices=diadiem)
    quan = forms.ChoiceField(choices=diadiem1)
    diachi = forms.ChoiceField(choices=diadiem2)
    
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), required=False)