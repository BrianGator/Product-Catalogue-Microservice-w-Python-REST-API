import factory
from factory.fuzzy import FuzzyChoice, FuzzyDecimal
from service.models import Product, Category


class ProductFactory(factory.Factory):
    """Creates fake products for testing"""

    class Meta:
        model = Product

    id = factory.Sequence(lambda n: n)
    name = FuzzyChoice(
        choices=[
            "Hacker Hat",
            "Pink Cat-Ear Headphones",
            "Fujifilm Instax Mini 9",
            "Apple AirPods Pro",
            "Nintendo Switch",
            "Blue Jeans",
            "Yellow T-Shirt",
            "T-Bone Steak",
            "Waffle Maker",
            "Drill Press",
            "Angle Grinder",
        ]
    )
    description = factory.Faker("text")
    price = FuzzyDecimal(0.5, 2000.0)
    available = FuzzyChoice(choices=[True, False])
    category = FuzzyChoice(
        choices=[
            Category.AUTOMOTIVE,
            Category.CLOTHS,
            Category.FOOD,
            Category.HOUSEWARES,
            Category.TOOLS,
            Category.UNKNOWN,
        ]
    )
