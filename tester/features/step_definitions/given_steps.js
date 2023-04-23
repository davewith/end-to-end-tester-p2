"use strict";

const { Given } = require("@cucumber/cucumber");
const percySnapshot = require("@percy/selenium-webdriver");

var firstTime = true;

Given(/^I'm on the (.+) page$/, async function (page) {
    await this.driver.get(`http://localhost:3000/${page}`);
    if (firstTime) {
        await percySnapshot(this.driver, `Load ${page}`);
        firstTime = false;
    }
});
