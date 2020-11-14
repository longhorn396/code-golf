import { expect } from "chai";
import "mocha";
import { isHappy, search } from "../src/happyNums";

describe("happyNums", () => {
    describe("isHappy", () => {
        it("returns `true` for happy numbers", () => {
            expect(isHappy(7)).to.equal(true);
            expect(isHappy(13)).to.equal(true);
        });
        it("returns `false` for not-happy numbers", () => {
            expect(isHappy(69)).to.equal(false);
            expect(isHappy(420)).to.equal(false);
        });
    });
    describe("search", () => {
        it("returns the correct happy nums", () => {
            expect(search(12)).to.deep.equal([1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68]);
        });
    });
});
