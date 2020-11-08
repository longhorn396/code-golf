import { expect } from "chai";
import "mocha";
import { coinFlipReduce } from "../src/coinFlip";

describe("coinFlip", () => {
    const flipsToTest: number = 5;
    const resultLines = coinFlipReduce(flipsToTest).split("\n");
    it("displays the correct number of flip results", () => {
        expect(resultLines[0].split(", ").length).to.equal(flipsToTest);
    });
    it("displays the correct sums of flip results", () => {
        expect(parseInt(resultLines[1].charAt(0)) + parseInt(resultLines[1].charAt(9))).to.equal(flipsToTest);
    });
});
