import { expect } from "chai";
import "mocha";
import {
    inOrderBranchPrediction,
    inOrderHeuristic,
    inOrderReadability,
    wordInOrderBranchPrediction,
    wordInOrderReadability
} from "../src/inOrder";

describe("inOrder", () => {
    const alphaWords = ["almost", "bit", "billowy", "biopsy"];
    const alphaTextInput = alphaWords.join(" ");
    const alphaTextResult = alphaWords.join(" - in order\n") + " - in order";
    const nonAlphaWords = ["chef", "dig", "nope", "false"];
    const nonAlphaTextInput = nonAlphaWords.join(" ");
    const nonAlphaTextResult = nonAlphaWords.join(" - not in order\n") + " - not in order";
    describe("word function tests", () => {
        describe("wordInOrderBranchPrediction", () => {
            it("should return true if a word's characters are in alphabetical order", () => {
                alphaWords.map((word) => wordInOrderBranchPrediction(word)).forEach((result) => expect(result).true);
            });
            it("should return false if a word's characters are not in alphabetical order", () => {
                nonAlphaWords.map((word) => wordInOrderBranchPrediction(word)).forEach((result) => expect(result).false);
            });
        });
        describe("wordInOrderReadability", () => {
            it("should return true if a word's characters are in alphabetical order", () => {
                alphaWords.map((word) => wordInOrderReadability(word)).forEach((result) => expect(result).true);
            });
            it("should return false if a word's characters are not in alphabetical order", () => {
                nonAlphaWords.map((word) => wordInOrderReadability(word)).forEach((result) => expect(result).false);
            });
        });
    });
    describe("text function tests", () => {
        describe("inOrderBranchPrediction", () => {
            it("should display ' - in order\\n' if a word's characters are in alphabetical order", () => {
                expect(inOrderBranchPrediction(alphaTextInput)).to.equal(alphaTextResult);
            });
            it("should display ' - not in order\\n' if a word's characters are in alphabetical order", () => {
                expect(inOrderBranchPrediction(nonAlphaTextInput)).to.equal(nonAlphaTextResult);
            });
        });
        describe("inOrderReadability", () => {
            it("should display ' - in order\\n' if a word's characters are in alphabetical order", () => {
                expect(inOrderReadability(alphaTextInput)).to.equal(alphaTextResult);
            });
            it("should display ' - not in order\\n' if a word's characters are in alphabetical order", () => {
                expect(inOrderReadability(nonAlphaTextInput)).to.equal(nonAlphaTextResult);
            });
        });
        describe("inOrderHeuristic", () => {
            it("should display ' - in order\\n' if a word's characters are in alphabetical order", () => {
                expect(inOrderHeuristic(alphaTextInput)).to.equal(alphaTextResult);
            });
            it("should display ' - not in order\\n' if a word's characters are in alphabetical order", () => {
                expect(inOrderHeuristic(nonAlphaTextInput)).to.equal(nonAlphaTextResult);
            });
        });
    });
});
