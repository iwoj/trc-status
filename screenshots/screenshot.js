const puppeteer = require('puppeteer');

(async () => {
  // Launch a headless browser
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  
  // Create a new page
  const page = await browser.newPage();
 
  // Custom user agent
  const customUA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36';
 
  // Set custom user agent
  await page.setUserAgent(customUA);

  const dateObj = new Date();
  const month = dateObj.getUTCMonth() + 1; //months from 1-12
  const day = dateObj.getUTCDate();
  const year = dateObj.getUTCFullYear();
  const newdate = year + "-" + month + "-" + day;

  // Set the viewport size
  await page.setViewport({ width: 1024, height: 768 });

  // Catch console errors and log them (optional)
  page.on('console', msg => {
    if (msg.type() === 'error') {
      console.error('Error:', msg.text());
    }
  });

  // Open a webpage
  await page.goto('https://trcprogress.ca', { waitUntil: 'networkidle2' });

  // Wait for a few seconds to ensure the page is fully loaded
  await page.evaluate(() => new Promise(resolve => setTimeout(resolve, 10000))); // Wait for 5 seconds

  // Take a screenshot
  await page.screenshot({ path: 'trcprogress-'+newdate+'.png', fullPage: true });

  // Close the browser
  await browser.close();
})();

