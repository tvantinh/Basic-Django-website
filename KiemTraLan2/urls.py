from django.urls import path
from . import views

urlpatterns = [
    path('', views.dsdm, name='dsdm'),
    path('dssptheodm/<int:MaDanhMuc>', views.xemchitietdm, name='ctdm'),
    path('dssp', views.dssp, name='dssp'),
    path('dssp/<int:MaSanPham>', views.xemchitiet, name='ctsp'),
    path('themvaogiohang/<int:product_id>/', views.themvaogiohang, name='themvaogiohang'),
    path('donhang', views.donhang, name='donhang'),
    path('hoanthanh', views.hoanthanh, name='hoanthanh'),
    path('ThemThongTinBuoiTiec', views.ThemThongTinBuoiTiec, name='ThemThongTinBuoiTiec'),
]