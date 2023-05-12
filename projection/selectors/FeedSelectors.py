from selenium.webdriver.common.by import By

class Feed_Selectors:
      
    alloptionLi = (By.XPATH,'//*[@id="app"]/div[4]/div/div[1]/ul/li[1]')
    addToFavoritesButton = (By.XPATH,'//*[@id="Layer_1" and @class="icon__DefaultSvgIcon-mjb0o-0-Component hUkFBX"]')
    favoritesoptionLi = (By.CSS_SELECTOR,'#app > div.goal-header__BlueLinealBackground-sc-1awcmub-0.cbqFOO > div > div > ul > li:nth-child(2)')
    collectionsoptionLi = (By.CSS_SELECTOR,'#app > div.goal-header__BlueLinealBackground-sc-1awcmub-0.cbqFOO > div > div > ul > li:nth-child(3)')

    contentproviderImg = (By.XPATH,'//*[@class="content__StyledSourceImage-unkjiu-1 kcKzDL"]')

