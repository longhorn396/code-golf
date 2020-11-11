import { ArgType, main } from "./common";

/**
 * @description Simulates coin flips and returns the results.
 *
 * @param {number} numFlips - Number of coin flips to simulate.
 * @returns {string} The results of each coin flip on one line and the sums of the results on the following line.
 */
export const coinFlipReduce = (numFlips: number): string => {
    const flips = [];
    for (let i = 0; i < numFlips; i++) {
        flips.push(Math.floor(Math.random() * 2));
    }
    const numTails = flips.reduce((total: number, value: number) => total + value);
    const numHeads = flips.length - numTails;
    const result = flips.map((flip: number) => ["Heads", "Tails"][flip]).join(", ");
    return `${result}\n${numHeads} Heads; ${numTails} Tails`;
};

/* istanbul ignore if */
if (require.main === module) {
    main(coinFlipReduce, ArgType.INT, "How many coins to flip?");
}
