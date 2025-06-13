import { Builder, Browser } from "selenium-webdriver";

async function bfr() {
  let driver = await new Builder().forBrowser(Browser.EDGE).build();

  // Go to a page
  await driver.get('https://www.example.com');
  console.log('Example page visited');
  
  await driver.sleep(2*1000);

  await driver.navigate().back();
  console.log('Navigated back');

  await driver.sleep(2*1000);

  await driver.navigate().forward();
  console.log('Navigated forward');

  await driver.sleep(2*1000);

  await driver.navigate().refresh();
  console.log('Page refreshed');

  await driver.sleep(2*1000);
  
  await driver.quit();
  console.log('Browser closed');
}

bfr();