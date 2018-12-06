import random
import string

from django.utils.text import slugify

# from restaurants.utils import random_string_generator

DONT_USE = ['create']


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    # Esto es para nuestro proyecto de Django y asumeque tu modelo tiene
    # una instancia con un campo slug y un tituto caracter

    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.titulo)
    if slug in DONT_USE:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)

    return slug