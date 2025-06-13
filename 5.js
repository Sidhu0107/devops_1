import { Builder, Browser, By, Key } from "selenium-webdriver";

async function test() {
  const driver = await new Builder().forBrowser(Browser.EDGE).build();
  await driver.get('https://practicetestautomation.com/practice-test-login/');

  await driver.findElement(By.id('username')).sendKeys('student', Key.RETURN);
  await driver.findElement(By.id('password')).sendKeys('Password123', Key.RETURN);
  await driver.findElement(By.id('submit')).click();

  await driver.sleep(3*1000);
  const status = await driver.findElement(By.className('post-title')).getText();
  console.log(status);

  await driver.sleep(5*1000);
  await driver.quit();
}

test();