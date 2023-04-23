"use strict";

const { When } = require("@cucumber/cucumber");
const { By } = require("selenium-webdriver");
const percySnapshot = require("@percy/selenium-webdriver");

When(
    "I attempt to log in using {string} and {string}",
    async function (email, password) {
        await this.driver.findElement(By.id("email")).sendKeys(email);
        await this.driver.findElement(By.id("password")).sendKeys(password);
        await this.driver.findElement(By.css('button[type="submit"]')).click();
        await percySnapshot(this.driver, `Log in with ${email} & ${password}`);
        this.driver.whenLogin = `${email} & ${password}`;
    }
);
