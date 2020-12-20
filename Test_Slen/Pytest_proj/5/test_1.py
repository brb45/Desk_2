import pytest

class Product:
    def __init__(self, ref=None, name=None, supplier = None):
        self.ref = ref
        self.name = name
        self.supplier = supplier
    def print(self):
        print(self.ref, self.name, self.supplier)

class db:
    def __init__(self):
        self.data = []
    def add(self, product):
        self.data.append(product)
    def remove(self, product):
        self.data.remove(product)
    def size(self):
        print(len(self.data))

# working version
@pytest.fixture
def create_db():
    return db


@pytest.fixture
def make_product():
    p = Product(
        ref=100,
        name='clother'
    )

    def _make_product(db, supplier):
        p.supplier = supplier
        db.add(p)
        return p

    yield _make_product
    # db.remove(p)


def test_EU_supplier_has_total_price_including_VAT(make_product, create_db):
    supplier = "FR"
    database = create_db()
    product = make_product(database, supplier=supplier)
    database.size()
    product.print()
    assert product.supplier == supplier

def test_EU_supplier_has_total_price_including_VAT1(make_product, create_db):
    supplier = "FR"
    # database = create_db()
    product = make_product(create_db(), supplier=supplier)
    # database.size()
    product.print()
    assert product.supplier == supplier

# That works, but firstly now everything is a factory-fixture, which makes them more convoluted, and secondly, your tests are filling up with extra calls to make_things,
# and you're having to embed some of the domain knowledge of what-depends-on-what into your tests as well as your fixtures.