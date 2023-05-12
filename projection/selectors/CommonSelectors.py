from selenium.webdriver.common.by import By

class Common_Selectors:
      
    emailspan = (By.XPATH,'//*[contains(@class,"hDQizy")]/span')
    profileLi = (By.XPATH,'//*[contains(@class,"qyqSY")]/li[1]/a')
    logOutLi = (By.XPATH,'//*[contains(@class,"qyqSY")]/li[2]/a')
    userNametxt = (By.XPATH,'//*[contains(@class,"profile__Title-sc-14ovosn-1 cpPjoh")]')
    roletxt = (By.XPATH,'//*[contains(@class,"profile__SubTitle-sc-14ovosn-2 lehiIs")]')
    biotxt = (By.XPATH,'//*[contains(@class,"profile__ProfilePageContainer-sc-14ovosn-0")]/div/p')
    editButton = (By.XPATH,'//*[contains(@class,"profile__ProfilePageContainer-sc-14ovosn-0")]/button[2]')
    updateButton = (By.XPATH,'//*[contains(@class,"button__ButtonText-sc-1tzab1-0") and text()="Update"]')
    userNameInput = (By.NAME, 'name')
    roleInput = (By.NAME, 'role')
    bioInput = (By.XPATH,'//*[@class="TextArea-sc-1feqde6-0 cddZrm"]')
   
