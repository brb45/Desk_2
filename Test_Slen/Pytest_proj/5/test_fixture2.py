# version 1.
#----------------------------------------------------
@pytest.fixture
def supplier(db):
    s = Supplier(
        ref=random_ref(),
        name=random_name(),
        country="US",
    )
    db.add(s)
    yield s
    db.remove(s)

@pytest.fixture()
def product(db, supplier):
    p = Product(
        ref=random_ref(),
        name=random_name(),
        supplier=supplier,
        net_price=9.99,
    )
    db.add(p)
    yield p
    db.remove(p)

# And now you're writing a new test and you suddenly realise you need to customise your default "supplier" fixture:

def test_US_supplier_has_total_price_equal_net_price(product):
    assert product.total_price == product.net_price

def test_EU_supplier_has_total_price_including_VAT(supplier, product):
    supplier.country = "FR" # oh, this doesn't work
    assert product.total_price == product.net_price * 1.2

# For whatever reason, maybe because you need to set the supplier.country before you add things to the DB,
# or before you instantiate product objects, you need to be able to adjust the country field on your supplier feature.

# version 2.
#----------------------------------------------------
# Option 1: More fixtures
# We can just create more fixtures, and try do do a bit of DRY by extracting out common logic:

def _default_supplier():
    return Supplier(
        ref=random_ref(),
        name=random_name(),
    )

@pytest.fixture
def us_supplier(db):
    s = _default_supplier()
    s.country = "US"
    db.add(s)
    yield s
    db.remove(s)

@pytest.fixture
def eu_supplier(db):
    s = _default_supplier()
    s.country = "FR"
    db.add(s)
    yield s
    db.remove(s)
# That's just one way you could do it, maybe you can figure out ways to reduce
# the duplication of the db.add() stuff as well, but you are going to have to have a different,
# named fixture for each customisation of Supplier, and eventually you may decide that doesn't scale.
# us_supplier, eu_supplier, asia_supplier, ch_supplier, etc etc, too many fixtures!
# I'd like just one, customisable fixture please.

# version 3.
#----------------------------------------------------
# Option 2: factory fixtures
# Instead of a fixture returning an object directly, it can return a function that creates an object,
# and that function can take arguments:

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
# The problem with this is that, once you start, you tend to have to go all the way,
# and make all of your fixture hierarchy into factory functions:

def test_EU_supplier_has_total_price_including_VAT(make_supplier, product):
    supplier = make_supplier(country="FR")
    product.supplier = supplier # OH, now this doesn't work, because it's too late again
    assert product.total_price == product.net_price * 1.2
# And so...

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
# That works, but firstly now everything is a factory-fixture,
# which makes them more convoluted, and secondly, your tests are filling up with extra calls to
# make_things, and you're having to embed some of the domain knowledge of what-depends-on-what
# into your tests as well as your fixtures.

# version 4
# Option 3: "normal" fixture parametrization
@pytest.mark.parametrize('n', [1, 2, 3])
def test_doubling(n):
    assert n * 2 < 6 # will pass twice and fail once

# A slightly less well-known feature is that you can parametrize fixtures as well.
# You need to use the special request fixture to access your parameters:

@pytest.fixture(params=['US', 'FR'])
def supplier(db, request):
    s = Supplier(
        ref=random_ref(),
        name=random_name(),
        country=request.param
    )
    db.add(s)
    yield s
    db.remove(s)

def test_US_supplier_has_no_VAT_but_EU_supplier_has_total_price_including_VAT(product):
    # this test is magically run twice, but:
    if product.supplier.country == 'US':
        assert product.total_price == product.net_price
    if product.supplier.country == 'FR':
        assert product.total_price == product.net_price * 1.2

###########################
# using pytest parametrization to override nested default-value fixtures
# @pytest.fixture
# def supplier(db):
#     s = Supplier(
#         ref=random_ref(),
#         name=random_name(),
#         country="US",
#     )
#     db.add(s)
#     yield s
#     db.remove(s)


@pytest.fixture()
def country():
    return "US"

@pytest.fixture
def supplier(db, country):
    s = Supplier(
        ref=random_ref(),
        name=random_name(),
        country=country,
    )
    db.add(s)
    yield s
    db.remove(s)

@pytest.fixture()
def product(db, supplier):
    p = Product(
        ref=random_ref(),
        name=random_name(),
        supplier=supplier,
        net_price=9.99,
    )
    db.add(p)
    yield p
    db.remove(p)

@pytest.mark.parametrize('country', ["US"])
def test_US_supplier_has_total_price_equal_net_price(product):
    assert product.total_price == product.net_price

@pytest.mark.parametrize('country', ["EU"])
def test_EU_supplier_has_total_price_including_VAT(product):
    assert product.total_price == product.net_price * 1.2