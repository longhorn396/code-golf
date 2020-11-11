import { expect } from "chai";
import "mocha";
import { forLoopFactorial, whileLoopFactorial, recursiveFactorial, tailFactorial, arrayFactorial, reduceFactorial } from "../src/factorial";

describe("factorial", () => {
    const testInput = 5;
    const testOutput = 120;
    const testCase = (fun: Function) => () => {
        it("outputs the correct factorial", () => {
            expect(fun(testInput)).to.equal(testOutput);
        });
    };
    describe("forLoopFactorial", testCase(forLoopFactorial));
    describe("whileLoopFactorial", testCase(whileLoopFactorial));
    describe("recursiveFactorial", testCase(recursiveFactorial));
    describe("tailFactorial", testCase(tailFactorial));
    describe("arrayFactorial", testCase(arrayFactorial));
    describe("reduceFactorial", testCase(reduceFactorial));
});
