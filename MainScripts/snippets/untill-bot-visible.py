element = WebDriverWait(driver, 10).until(
    EC.invisibility_of_element_located((By.CSS_SELECTOR,
                                        '#edit-submitted-other-receipts--19 > div > div.form-item.webform-component.webform-component-multiple-file.webform-component--other-receipts--18 > div.file-widget.form-managed-file.clearfix > div > div')))
