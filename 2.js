import { Builder, By, Browser } from "selenium-webdriver";

async function getText() {
  // Create a new driver
  let driver = await new Builder().forBrowser(Browser.EDGE).build();
  await driver.get('https://www.example.com');
  
  // Get Heading 
  let text = await driver.findElement(By.tagName('h1')).getText();
  console.log("Heading text:", text);
  
  // Get Paragraph
  text = await driver.findElement(By.tagName('p')).getText();
  console.log("Paragraph text:", text);

  // Close the browser
  await driver.sleep(5*1000);
  await driver.quit();
  return text;
}

getText();