import { expect } from "chai";
import "mocha";
import { disemvowel } from "../src/disemvoweler";

describe("disemvoweler", () => {
    it("handles a simple case correctly", () => {
        expect(disemvowel("Hello World!")).to.equal("HllWrld eoo");
    });
    it("handles a complex case correctly", () => {
        expect(disemvowel("The quick brown fox jumped over the lazy dog")).to.equal("Thqckbrwnfxjmpdvrthlzydg euiooueoeeao");
    });
});
