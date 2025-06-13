import { Builder, Browser } from "selenium-webdriver";
import { outputFile } from "fs-extra";

async function screenShot() {
  const driver = await new Builder().forBrowser(Browser.EDGE).build();
  await driver.get('https://www.example.com');

  // ScreenShot
  const screenshot = await driver.takeScreenshot();
  await outputFile('screenshot.png', screenshot, { encoding: 'base64' });

  await driver.sleep(10*1000);
  await driver.quit();
}

screenShot();