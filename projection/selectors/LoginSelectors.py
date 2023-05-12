from selenium.webdriver.common.by import By

class Login_Selectors:
      
    logInButton = (By.XPATH,'//*[@data-cy="login"]')
    signUpButton = (By.XPATH,'//*[@data-cy="signup"]')
    emailTxt = (By.XPATH,'//*[@data-cy="email"]')
    passwordTxt = (By.XPATH,'//*[@data-cy="password"]')
    loginTxt = (By.XPATH,'//*[contains(@class,"hXodji")]')