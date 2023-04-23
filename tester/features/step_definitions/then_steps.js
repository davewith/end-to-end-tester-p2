"use strict";

var assert = require("assert");
const { Then } = require("@cucumber/cucumber");
const { By, until } = require("selenium-webdriver");
const percySnapshot = require("@percy/selenium-webdriver");

Then("I should see a message with {string}", async function (expectedText) {
    const actualDiv = await this.driver.wait(
        until.elementLocated(By.id("user-message")),
        5000
    );
    const actualText = await actualDiv.getText();

    assert.ok(
        actualText.toLowerCase().includes(expectedText.toLowerCase()),
        `Expected ${expectedText} in body`
    );
    await percySnapshot(this.driver, `Message after ${this.driver.whenLogin}`);
});
