from django.db import models

# Create your models here.
class DanhMuc(models.Model):
    MaDanhMuc = models.AutoField(primary_key=True)
    TenDanhMuc = models.CharField(max_length=255)

    def __str__(self):
        return self.TenDanhMuc
class SanPham(models.Model):
    MaSanPham = models.AutoField(primary_key=True)
    MaDanhMuc = models.ForeignKey(DanhMuc, on_delete=models.CASCADE)
    TenSanPham = models.CharField(max_length=255)
    MoTa = models.TextField()
    Gia = models.FloatField()
    HinhAnhDaiDien = models.ImageField(upload_to='')

    def __str__(self):
        return self.TenSanPham
class KhachHang(models.Model):

    MaKhachHang = models.AutoField(primary_key=True)
    Ten = models.CharField(max_length=100)
    TenBe = models.CharField(max_length=100)
    SoDienThoai = models.CharField(max_length=20)
    Email = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        return self.Ten

class DonHang(models.Model):
    MaDonHang = models.AutoField(primary_key=True)
    MaKhachHang = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    NgayDatHang = models.DateField()
    TongTien = models.DecimalField(max_digits=10, decimal_places=2)
    DiaChiGiaoHang = models.CharField(max_length=255)
    TrangThai = models.BooleanField(default=False)
    def __str__(self):
        return str(self.MaDonHang)
    
class ChiTietDonHang(models.Model):
    MaChiTietDonHang = models.AutoField(primary_key=True)
    MaDonHang = models.ForeignKey(DonHang, on_delete=models.CASCADE)
    MaSanPham = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    SoLuong = models.IntegerField()
    DonGia = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.MaDonHang} - {self.MaSanPham}"