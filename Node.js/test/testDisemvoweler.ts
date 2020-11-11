import { expect } from "chai";
import "mocha";
import { disemvowelArrays, disemvowelStrings } from "../src/disemvoweler";

describe("disemvoweler", () => {
    const simpleInput = "Hello World!";
    const simpleOutput = "HllWrld eoo";
    const complexInput = "The quick brown fox jumped over the lazy dog";
    const complexOutput = "Thqckbrwnfxjmpdvrthlzydg euiooueoeeao";
    describe("disemvowelArrays", () => {
        it("handles a simple case correctly", () => {
            expect(disemvowelArrays(simpleInput)).to.equal(simpleOutput);
        });
        it("handles a complex case correctly", () => {
            expect(disemvowelArrays(complexInput)).to.equal(complexOutput);
        });
    });
    describe("disemvowelStrings", () => {
        it("handles a simple case correctly", () => {
            expect(disemvowelStrings(simpleInput)).to.equal(simpleOutput);
        });
        it("handles a complex case correctly", () => {
            expect(disemvowelStrings(complexInput)).to.equal(complexOutput);
        });
    });
});
