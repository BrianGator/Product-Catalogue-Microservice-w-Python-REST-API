import { test, expect } from '@playwright/test';

test('has title', async ({ page }) => {
  await page.goto('http://localhost:3000');
  await expect(page).toHaveTitle(/Product Store Admin Interface/);
});

test('create product via UI', async ({ page }) => {
  await page.goto('http://localhost:3000');
  await page.fill('#product_name', 'Playwright Phone');
  await page.fill('#product_description', 'Tested with Playwright');
  await page.fill('#product_price', '500');
  await page.selectOption('#product_category', 'ELECTRONICS'); // Category may vary based on implementation
  await page.click('#create-btn');
  
  const flash = page.locator('#flash_message');
  await expect(flash).toHaveText(/Success/);
});
