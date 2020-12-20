from selenium import webdriver

class Browser():
    base_url = "http://localhost:8000"
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=opts)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)
    
    def quit(self):
        self.driver.quit()

    def visit(self, location=""):
        url = self.base_url + location
        self.driver.get(url)

        
        
    
    ### find_element by attribute
    # NoSuchElementException
    # <input id = "search" type = "text" name = "q" value = "" class = "input-text" maxlength = "128" autocomplete = "off" >
    # find_element_by_id()
    def test_search_text_field_max_length(self):
            # get the search textbox
        search_field = self.driver.find_element_by_id("search")

        # check maxlength attribute is set to 128
        self.assertEqual("128", search_field.get_attribute("maxlength"))

        search_field = self.driver.find_element_by_name("q")

        # class attribute is used to apply CSS to an element
        # find_element_by_class_name
        # <button type = "submit" title = "Search" class = "button" > <span > <span > Search < /span > </span > </button >

        def test_search_button_enabled(self):
            # get Search button
            search_button = self.driver.find_element_by_class_name("button")

            # check Search button is enabled
            self.assertTrue(search_button.is_enabled()
        
        # find_element_by_tag_name()

    < ul class="promos" >
      < li >
        < a href="https://magento.com/" >
        < img src="/media/wysiwyg/homepage-three-column-promo-01B.png" alt="Physical &amp; Virtual Gift Cards" >
        < / a >
      < / li >
      < li >
        < a href="http://demo.magentocommerce.com/vip.html" >
        < img src="/media/wysiwyg/homepage-three-column-promo-02.png" alt="Shop Private Sales - Members Only" >
        < / a >
        < / li >
      < li >
        < a href="http://demo.magentocommerce.com/accessories/bags-luggage.html" >
        < img src="/media/wysiwyg/homepage-three-column-promo-03.png" alt="Travel Gear for Every Occasion" >
        < / a >
        < / li >
    < / ul >

        def test_count_of_promo_banners_images(self):
        # get promo banner list
            banner_list=self.driver.find_element_by_class_name(
                                "promos")
                                   
        # get images from the banner_list
            banners=banner_list.find_elements_by_tag_name(
            "img")
        # check there are 20 tags displayed on the page
            self.assertEqual(2, len(banners))
# Xpath : query language used to search and locate nodes in XML document
# when can't find a suitable ID, name, or class attibute of an element, use Xpath to either
# find the element in absolute terms or relative to an element that does have an ID or name.

# can use defined attributes other than ID, name or class with Xpath queries.
# starts-with(), contains(), end-with();

# find_element_by_xpath()
    def test_vip_promo(self):
    # get vip promo image
    vip_promo=self.driver.\
    find_element_by_xpath(
        "//img[@alt='Shop Private Sales - Members Only']")

    # check vip promo logo is displayed on home page
    self.assertTrue(vip_promo.is_displayed())
    # click on vip promo images to open the page
    vip_promo.click()
    # check page title
    self.assertEqual("VIP",  self.driver.title)

# find_element_by_css_selector
    < div class="minicart-wrapper" >
        < p class="block-subtitle" >
            Recently added item(s)
            < a class="close skip-link-close" href="#" title="Close" >×</a >
        < / p >
        < p class="empty" > You have no items in your shopping cart. < /p >
    < / div >

     def test_shopping_cart_status(self):
         # check content of My Shopping Cart block on Home page
         # get the Shopping cart icon and click to open the # Shopping Cart section

        #  This will first find a < div > element with the header_minicart class name 
        #  and then find a < span > element under this div, which has icon as its class name.
         shopping_cart_icon=self.driver.\
         find_element_by_css_selector("div.header-minicart span.icon")
         shopping_cart_icon.click()

         # get the shopping cart status
         shopping_cart_status=self.driver.\
         find_element_by_css_selector("p.empty").text
         self.assertEqual(
             "You have no items in your shopping cart.", shopping_cart_status)
         # close the shopping cart section
         close_button=self.driver.\
         find_element_by_css_selector("div.minicart-wrapper a.close")
         close_button.click()

# find_element_by_link_text
     < a href="#header-account" class="skip-link skip-account" >
     < span class="icon" > </span >
     < span class="label" > Account < /span >
     < / a >
    def test_my_account_link_is_displayed(self):
        # get the Account link
        account_link=self.driver.find_element_by_link_text("ACCOUNT")
        # check My Account link is displayed/visible in
        # the Home page footer
        self.assertTrue(account_link.is_displayed())

# find_element_by_partial_link_text()
     def test_account_links(self):
        # get the all the links with Account text in it
        account_links=self.driver.\
        find_elements_by_partial_link_text("ACCOUNT")
        # check Account and My Account link is displayed/visible in the Home page footer
        self.assertTrue(2, len(account_links))



    

