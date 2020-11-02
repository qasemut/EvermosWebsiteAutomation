import unittest
from selenium import webdriver

from test_data import TestData
from locators import Locators
from pages import HomePage, TanyaJawabPage, CaraKerjaPage, TestimoniPage, HubungiKamiPage

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=TestData.CHROME)
        self.driver.maximize_window()
        # self.driver.set_window_size(1366, 768)
        # self.driver.set_window_size(320, 768) #mobile S - 320px
        # self.driver.set_window_size(375, 768)  # mobile M - 375px
        # self.driver.set_window_size(425, 768)  # mobile L - 425px
        # self.driver.set_window_size(768, 768)  # Tablet - 768px
        # self.driver.set_window_size(1024, 768)  # Laptop - 1024px
        # self.driver.set_window_size(1440, 768)  # Laptop L - 1440px


    def tearDown(self):
        self.driver.quit()

class RedirectSuccessToOtherPage(BaseTest):
    def test_redirect_page_success(self):
        """
        Test case untuk memastikan bahwa semua fungsi redirect ke semua halaman berfungsi
        """
        # --- Subtest 1 - Redirect to home page ---

        # membuat objek homepage
        self.homepage = HomePage(self.driver)

        # Step 1 - Click home page menu in navbar
        self.homepage.redirect_home_page_success()

        # Step 2 - Assertion
        with self.subTest(msg="Home"):
            element_text = self.homepage.get_text(Locators.HOME_PAGE_TITLE)
            self.assertEqual("Semua Bisa Punya Toko Online Sendiri", element_text)

        # ---Subtest 2 - Redirect to tanya jawab page

        # membuat objek tanya jawab page
        self.tanyajawabpage = TanyaJawabPage(self.driver)

        # Step 1 - Click tanya jawab menu in navbar
        self.tanyajawabpage.redirect_tanya_jawab_page_success()

        # Step 2 - Assertion
        with self.subTest(msg="TanyaJawab"):
            element_text1 = self.tanyajawabpage.get_text(Locators.TANYA_JAWAB_TEXT)
            self.assertEqual("Evermos Bekerja Sama dengan Lebih dari Ratusan Brand dan Ribuan Produk Muslim")