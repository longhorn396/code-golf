import { expect } from "chai";
import "mocha";
import { IFibonacciOutput, dumbFibonacci, lessDumbFibonacci, iterativeFibonacci, recursiveFibonacci } from "../src/fibonacci";

describe("fibonacci", () => {
    const testInputs = [1, 2, 5, 10];
    const testOutputs: IFibonacciOutput[] = [
        { i: 1, fibonacciNumber: 0, sequence: [0] },
        { i: 2, fibonacciNumber: 1, sequence: [0, 1] },
        { i: 5, fibonacciNumber: 3, sequence: [0, 1, 1, 2, 3] },
        { i: 10, fibonacciNumber: 34, sequence: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] }
    ];
    const testCase = (fun: Function) => () => {
        it("outputs the correct information based on test input", () => {
            for (let i = 0; i < testInputs.length; i++) {
                expect(fun(testInputs[i])).to.deep.equal(testOutputs[i]);
            }
        });
    };
    describe("dumbFibonacci", testCase(dumbFibonacci));
    describe("lessDumbFibonacci", testCase(lessDumbFibonacci));
    describe("iterativeFibonacci", testCase(iterativeFibonacci));
    describe("recursiveFibonacci", testCase(recursiveFibonacci));
});
