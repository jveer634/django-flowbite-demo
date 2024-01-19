import factory
from .models import Todo


from factory.faker import faker

FAKE = faker.Faker()

class TodoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Todo
    
    title = factory.Faker("sentence", nb_words=5)
    content=factory.Faker("text")


    @factory.lazy_attribute
    def content(self):
        x= ""
        for _ in range(5):
            x += '\n' + FAKE.paragraph(nb_sentences=20) + "\n"
        return x
    
    status = factory.Iterator(["To Do",
        "In Progress",
        "Completed"])