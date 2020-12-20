< form
autocomplete = "false"

class ="modules-login-components-SignIn-components-Form-___style__sign-up-form___2z3Ug" >

    < div class ="core-forms-components-___input__input-wrapper___17k2k" >
        < div class ="ui textfield invalid">

<label for="email">Email Address</label>
    <input autocomplete="true" id="email" type="email" class="input" placeholder="user @ domain.com" value="">"
"<i aria-hidden="true" class="ui icon close - circle -fill"></i>"
    </div>"
    "<div class="core - forms - components - ___input__error - message___3ZeWU">Required field</div></div>" \
    "<div class="
ui
buttons
"><button class="
ui
button
primary
disabled
" disabled=""

type = "submit" > Next < / button > < a


class ="forgot-password ui button flat" href="/signin/password/forgot" > Forgot Password < / a > < a class ="sign-up ui button default" href="/signup" > Create an Account < / a > < / div > < / form >

# create driver
# load webdriver
# load webpage(login url)
# locator for email address
# send_keys (email address)
# click on email locator
# find locator of new page
# locate successful message welcome : assert


def test_email(url, email):
    driver = webdriver.Chrome()
    driver.get(url)
    locator = driver.find_element_by_id("email")
    locator.send_keys(email)
    welcome_page = driver.find_element_by_id("welcome")
    assert welcome.title == "welcome"


menu.json

{"menu": {
    "id": "file",
    "value": "File",
    "popup": {
        "menuitem": [
            {"value": "New", "onclick": "CreateNewDoc()"},
            {"value": "Open", "onclick": "OpenDoc()"},
            {"value": "Close", "onclick": "CloseDoc()"}
        ]
    }
}}

{[(<>)]}
True
# input is a string, consisting of  {[(<>)]} and letters


{{]} False

load
json
a
python
dict
json.load(open("menu.json", 'r")


def match(string):














































