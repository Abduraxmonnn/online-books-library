from apps.products.serializers import ProductCreateSerializer


def create_product(reqeust):
    serializer = ProductCreateSerializer(data=reqeust.data)
    serializer.is_valid(raise_exception=True)

    name = serializer.validated_data['name']
    category = serializer.validated_data['category']
    author = serializer.validated_data['category']

    return {
        'name': name,
        'category': category,
        'author': author
    }
