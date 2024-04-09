def user_image_path(instance, filename):
    user_id = instance.id if instance.id else 'temp'
    return f'users/{user_id}/{filename}'


def category_image_path(instance, filename):
    return f'category/{instance.name}/{filename}'

def product_image_path(instance, filename):
    return f'products/{instance.category_id.name}/{filename}'

# def news_image_path(instance , filename):
#     return f'product/{instance}'