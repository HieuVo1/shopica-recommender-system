from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    updated_by = models.CharField(max_length=45, blank=True, null=True)
    category = models.ForeignKey('Category', models.DO_NOTHING)
    store_id = models.IntegerField()
    brand = models.ForeignKey('Brand', models.DO_NOTHING)

    @property
    def categoryId(self):
        return self.category.id

    @property
    def categoryName(self):
        return self.category.category_name

    @property
    def brandName(self):
        return self.brand.brand_name

    @property
    def brandId(self):
        return self.brand.id

    class Meta:
        managed = False
        db_table = 'product'
        unique_together = (('id', 'category', 'store_id', 'brand'),)


class ProductDetail(models.Model):
    quantity = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    product = models.ForeignKey(
        Product, related_name='productDetails', on_delete=models.CASCADE)
    productSize = models.ForeignKey('Size', models.DO_NOTHING,db_column ="size_id")
    productColor = models.ForeignKey('Color', models.DO_NOTHING ,db_column ="color_id")

    @property
    def sizeId(self):
        return self.productSize.id

    @property
    def size(self):
        return self.productSize.size_name

    @property
    def colorId(self):
        return self.productColor.id

    @property
    def color(self):
        return self.productColor.color_name

    @property
    def colorHex(self):
        return self.productColor.color_code

    class Meta:
        managed = False
        db_table = 'product_detail'
        unique_together = (('id', 'product', 'productSize', 'productColor'),)


class ProductImage(models.Model):
    image = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    product = models.ForeignKey(
        Product, related_name='productImages', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'product_image'
        unique_together = (('id', 'product'),)


class Color(models.Model):
    color_name = models.CharField(max_length=45)
    color_code = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'color'


class Size(models.Model):
    size_name = models.CharField(max_length=45)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'size'


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    image = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    updated_by = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brand'
