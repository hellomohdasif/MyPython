try:

    wait = WebDriverWait(driver, 10)
    men_menu = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                            '#yDmH0d > div.NBxL9e.iWO5td > div > div.I7OXgf.B6r3ub.JKIKje.ZEeHrd.Inn9w.iWO5td > span > div > div.noiLqd > div.uxEN2b > div.W9wDc.D3oBEe.x4uME.uQUqpd.svmwUe.CDELXb > div.n9IS1.oJeWuf.rXTzdc > span > span > svg')))
    print("Found")


except:

    print("not Found")
    abc4.clear()
    abc4.send_keys(randomChar + "-" + mega)
    nice = abc4.get_attribute('value')