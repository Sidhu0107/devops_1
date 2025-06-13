import { Builder, Browser, By } from 'selenium-webdriver';

async function getLinkCount() {
  const driver = await new Builder().forBrowser(Browser.EDGE).build();
  await driver.get('https://www.npmjs.com/package/selenium-webdriver');
  
  const links = await driver.findElements(By.tagName('a'));
  console.log(`Number of links: ${links.length}`);

  // Optional
  for (let link of links) {
    console.log(await link.getAttribute('href'));
  }

  await driver.sleep(10*1000);
  await driver.quit();
}

getLinkCount();