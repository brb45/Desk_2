
# Not working
@pytest.fixture
def make_supplier(db):
    s = Supplier(
        ref=random_ref(),
        name=random_name(),
    )

    def _make_supplier(country):
        s.country = country
        db.add(s)
        return s

    yield _make_supplier
    db.remove(s)

def test_EU_supplier_has_total_price_including_VAT(make_supplier, product):
    supplier = make_supplier(country="FR")
    product.supplier = supplier # OH, now this doesn't work, because it's too late again
    assert product.total_price == product.net_price * 1.2

# working version
@pytest.fixture
def make_product(db):
    p = Product(
        ref=random_ref(),
        name=random_name(),
    )

    def _make_product(supplier):
        p.supplier = supplier
        db.add(p)
        return p

    yield _make_product
    db.remove(p)


def test_EU_supplier_has_total_price_including_VAT(make_supplier, make_product):
    supplier = make_supplier(country="FR")
    product = make_product(supplier=supplier)
    assert product.total_price == product.net_price * 1.2

# That works, but firstly now everything is a factory-fixture, which makes them more convoluted, and secondly, your tests are filling up with extra calls to make_things,
# and you're having to embed some of the domain knowledge of what-depends-on-what into your tests as well as your fixtures.