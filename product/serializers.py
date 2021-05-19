from surprise import dump
from .models import Product, ProductDetail, Brand, Color, Size, Category, ProductImage
from django_pandas.io import read_frame
from rest_framework import serializers


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'size_name']


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'color_name', 'color_code']


class ProductDetailSerializer(serializers.ModelSerializer):
    productDetailId = serializers.CharField(source='id')

    class Meta:
        model = ProductDetail
        fields = ['productDetailId', 'quantity', 'colorName',
                  'colorId', 'colorHex', 'sizeName', 'sizeId']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name', 'id']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['brand_name', 'id']


class ProductSerializer(serializers.ModelSerializer):
    productDetails = ProductDetailSerializer(many=True)
    productImages = ProductImageSerializer(many=True)
    productName = serializers.CharField(source='product_name')
    storeId = serializers.CharField(source='store_id')

    class Meta:
        model = Product
        fields = ['id', 'productName', 'storeId', 'price', 'categoryName', 'categoryId', 'brandName', 'brandId',
                  'productDetails', 'productImages']


def predict(userId):
    filename = './final_model.sav'
    model = dump.load(filename)
    products = Product.objects.all()
    productDf = read_frame(products, fieldnames=['pk'])
    productDfCopy = productDf.copy()
    productDfCopy['Estimate_Score'] = productDfCopy['pk'].apply(
        lambda x: model[1].predict(userId, x).est)
    productDfCopy = productDfCopy.sort_values(
        by=['Estimate_Score'], ascending=False)
    listId = productDfCopy.head(4)['pk'].tolist()
    result = products.filter(id__in=listId)
    return result
