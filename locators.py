from selenium.webdriver.common.by import By

class Locators():
    # --- Navbar Locators ---
    HOME_NAVBAR = (By.LINK_TEXT, "Home")
    TANYA_JAWAB_NAVBAR = (By.LINK_TEXT, "Tanya Jawab")
    CARA_KERJA_NAVBAR = (By.LINK_TEXT, "Cara Kerja")
    TESTIMONI_NAVBAR = (By.LINK_TEXT, "Testimoni")
    HUBUNGI_KAMI_NAVBAR = (By.LINK_TEXT, "Hubungi Kami")
    ABOUT_US_NAVBAR = (By.LINK_TEXT, "About Us")
    MASUK_BUTTON = (By.LINK_TEXT, "Masuk")
    DAFTAR_BUTTON = (By.LINK_TEXT, "Daftar")

    # --- Home Page Locators ---
    HOME_PAGE_TITLE = (By.CSS_SELECTOR, ".content-toko > span")
    DAFTAR_SEKARANG_JUGA_BUTTON = (By.LINK_TEXT, "/verify")
    GOOGLE_PLAY_BUTTON = (By.LINK_TEXT, "https://evermos.page.link/download-android")
    APP_STORE_BUTTON = (By.LINK_TEXT, "#")

    # --- Tanya Jawab Page Locators ---
    NEXT_PAGE_BUTTON = (By.CSS_SELECTOR, "#tanyaJawab > div.content-carousel > div > div.dekstop-content > div > div.VueCarousel-navigation > button.VueCarousel-navigation-button.VueCarousel-navigation-prev.VueCarousel-navigation--disabled")
    PREVIOUS_PAGE_BUTTON = (By.CSS_SELECTOR, "#tanyaJawab > div.content-carousel > div > div.dekstop-content > div > div.VueCarousel-navigation > button.VueCarousel-navigation-button.VueCarousel-navigation-next")
    DOT_BUTTON_1 = (By.CSS_SELECTOR, "#tanyaJawab > div.content-carousel > div > div.dekstop-content > div > div.VueCarousel-pagination > div > button.VueCarousel-dot.VueCarousel-dot--active")
    DOT_BUTTON_2 = (By.CSS_SELECTOR, "#tanyaJawab > div.content-carousel > div > div.dekstop-content > div > div.VueCarousel-pagination > div > button:nth-child(2)")
    DOT_BUTTON_3 = (By.CSS_SELECTOR, "#tanyaJawab > div.content-carousel > div > div.dekstop-content > div > div.VueCarousel-pagination > div > button:nth-child(3)")
    DOT_BUTTON_4 = (By.CSS_SELECTOR, "#tanyaJawab > div.content-carousel > div > div.dekstop-content > div > div.VueCarousel-pagination > div > button:nth-child(4)")
    DOT_BUTTON_5 = (By.CSS_SELECTOR, "#tanyaJawab > div.content-carousel > div > div.dekstop-content > div > div.VueCarousel-pagination > div > button:nth-child(5)")
    DOT_BUTTON_6 = (By.CSS_SELECTOR, "#tanyaJawab > div.content-carousel > div > div.dekstop-content > div > div.VueCarousel-pagination > div > button:nth-child(6)")
    TANYA_JAWAB_TEXT = (By.CSS_SELECTOR, ".header-section:nth-child(1) > p")

    # --- Cara Kerja Page Locators ---
    CARA_KERJA_PAGE_TITLE = (By.CSS_SELECTOR, "#caraKerja > div.con-wide > div.cara-kerja > span")

    # --- Testimoni Page Locators ---
    TESTIMONI_PAGE_TITLE = (By.CSS_SELECTOR, "#testimoni > div > div.testimoni > span")
    MULAI_BERIKHTIAR_BUTTON = (By.LINK_TEXT, "/verify")
    PREVIOUS_TESTIMONI_BUTTON = (By.CSS_SELECTOR, "#testimoni > div > div.dekstop-content > div > div.VueCarousel-navigation > button.VueCarousel-navigation-button.VueCarousel-navigation-prev.VueCarousel-navigation--disabled")
    NEXT_PAGE_TESTIMONI_BUTTON = (By.CSS_SELECTOR, "#testimoni > div > div.dekstop-content > div > div.VueCarousel-navigation > button.VueCarousel-navigation-button.VueCarousel-navigation-next")

    # --- Hubungi Kami Page Locators ---
    HUBUNGI_KAMI_PAGE_TITLE = (By.CSS_SELECTOR, "#hubungiKami > div > div.title > span")
    NEW_PHONE_NUMBER_INPUT = (By.CSS_SELECTOR, "#hubungiKami > div > div.form-daftar > div.input-field > input")
    CHECKLIST_SETUJUI = (By.CSS_SELECTOR, "#hubungiKami > div > div.form-daftar > div.checkbox > label > span")
    SAYA_INGIN_PUNYA_BISNIS_SENDIRI = (By.CSS_SELECTOR, "#hubungiKami > div > div.form-daftar > a > button")



    # --- Login Page Locators ---
    LOGIN_INPUT_PHONE_NUMBER = (By.CSS_SELECTOR, "#__layout > div > div:nth-child(2) > form > label:nth-child(1) > span.inputText__inner > input")
    LOGIN_INPUT_PASSWORD = (By.CSS_SELECTOR, "#__layout > div > div:nth-child(2) > form > label:nth-child(2) > span.inputText__inner > input")
    CHECKLIST_INGATKAN = (By.CSS_SELECTOR, "#__layout > div > div:nth-child(2) > form > div > label > input[type=checkbox]")
    AUTH_LOGIN_BUTTON = (By.CSS_SELECTOR, "#__layout > div > div:nth-child(3) > button")
