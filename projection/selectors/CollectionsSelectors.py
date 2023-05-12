from selenium.webdriver.common.by import By

class Collection_Selectors:
      
    mycollectionH1 = (By.XPATH,'//*[text()="My Collections"]')
    namecollectiontxt = (By.XPATH,'//*[contains(@class,"sc-fzXfMz")]/div/a[./h1]')
    collectionmarketplaceH1 = (By.XPATH,'//*[contains(@class,"gXnFso")][1]')
    subscribeButton = (By.XPATH,'//*[@class="sc-fzXfMC ccyqwp"]/*[contains(@class,"icon__BigSvgIcon-mjb0o-2-Component")]')
    subscriptionH1 = (By.XPATH,'//*[contains(@class,"gXnFso")][2]')
    createcollectionButton = (By.XPATH,'//*[contains(@class,"gXnFso")][3]')
    createcollectionDiv = (By.XPATH,'//*[contains(@class,"iACoKt")]')
    namecollectionInput = (By.NAME,'ModalName')
    changestatusSpan = (By.XPATH,'//*[contains(@class,"checkbox__CheckboxButton-egn3td-0")]')
    saveButton = (By.XPATH,'//*[contains(@class,"jnpNuA")]')
    namecollection = (By.XPATH,'//*[contains(@class,"jnpNuA")]')
    deletecollectionButton = (By.XPATH,'//*[@height="427pt"]')
    notificationcollectionDiv = (By.XPATH,'//*[@class="Toastify__toast-body"]')

