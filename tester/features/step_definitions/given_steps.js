"use strict";

const { Given } = require("@cucumber/cucumber");

Given(/^I'm on the (.+) page$/, async function (page) {
    await this.driver.get(`http://localhost:3000/${page}`);
});
