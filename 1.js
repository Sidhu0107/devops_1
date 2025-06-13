import { Builder, Browser, By, Key } from 'selenium-webdriver'

async function searchGoogle() {
  // Create a new driver
  let driver = await new Builder().forBrowser(Browser.EDGE).build();
  await driver.get('https://www.google.com');
  
  // Search
  const searchBox = await driver.findElement(By.name('q'));
  await searchBox.sendKeys('Selenium Node.js', Key.RETURN);

  // Close the browser after waiting 10 seconds
  await driver.sleep(10*1000);
  await driver.quit();
}

searchGoogle();
