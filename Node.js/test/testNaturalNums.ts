import { expect } from "chai";
import "mocha";
import { findNthNaturalNumber } from "../src/naturalNums";

describe("naturalNums", () => {
    const formatOutput = (natural: number, counting: number) => `The natural number is ${natural} in ${counting}`;
    it("Finds the correct natural numbers", () => {
        expect(findNthNaturalNumber(1, 1)).to.equal(formatOutput(1, 1));
        expect(findNthNaturalNumber(17, 20)).to.equal(formatOutput(3, 13));
        expect(findNthNaturalNumber(1986, 1000)).to.equal(formatOutput(8, 698));
    });
    it("Fails assertion if too small a number is passed", () => {
        expect(() => findNthNaturalNumber(0, 1)).to.throw();
    });
    it("Fails assertion if too small a limit is passed", () => {
        expect(() => findNthNaturalNumber(1986, 20)).to.throw();
    });
});
