"use strict";

const { When } = require("@cucumber/cucumber");
const { By } = require("selenium-webdriver");

When(
    "I attempt to log in using {string} and {string}",
    async function (email, password) {
        await this.driver.findElement(By.id("email")).sendKeys(email);
        await this.driver.findElement(By.id("password")).sendKeys(password);
        await this.driver.findElement(By.css('button[type="submit"]')).click();
    }
);
