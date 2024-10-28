from products.models import Product
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    user_product_list = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User 
        fields = ['id', 'username', 'user_product_list']

    def get_user_product_list(self, obj):
        return ProductSerializerUser(obj.product_set.all(), many=True).data
    
    
    
class ProductSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)
    amount = serializers.SerializerMethodField(read_only=True)
    discount_price = serializers.SerializerMethodField(read_only=True)
    username = serializers.CharField(max_length=100, source='user.username', read_only=True)
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField(write_only=True)
    class Meta:
        model = Product
        fields = ['username',  'id', 'name', 'price', 'description', 'amount', 'discount_price', 'author', 'created_at', 'updated_at', 'email']
        
    
   
        
    def get_amount(self, obj):
        return obj.get_amount()  
    
    
    def get_email(self, obj):
        return []          
    
    
    def get_discount_price(self, obj):
        return obj.get_discount_price()
    
    def get_author(self, obj):
        return UserSerializer(obj.user, many=False).data
    
    
    
    
    # validation des données
   
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('The name is too short')
        return value
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        validated_data.pop('email')
        return super().create(validated_data)
    


class ProductSerializerUser(serializers.ModelSerializer):
   
    class Meta:
        model = Product
        fields = '__all__'