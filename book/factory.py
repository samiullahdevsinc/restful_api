import factory
from .models import book

from factory.faker import faker

Fake = faker.Faker()


class PostFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = book

	name = factory.Faker("sentence",nb_words=10)
	author = factory.Faker("sentence",nb_words=2)


x = PostFactory.create_batch(100)