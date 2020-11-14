import { ArgType, mainSubf as main } from "./common";

/**
 * @description Tests if a number is happy. Numbers are happy if the sum of the squares of their digits equals 1. Numbers are also happy if that sum is happy, and so on.
 *
 * @param {number} num - Number to test happiness.
 * @returns If the input is happy or not.
 */
export const isHappy = (num: number): boolean => {
    const set = new Set();
    while (num > 0 && !set.has(num)) {
        const numString = num.toString();
        const squares = numString.split("").map((char: string) => Math.pow(parseInt(char), 2));
        const numSum = squares.reduce((prev: number, curr: number) => prev + curr);
        if (numSum !== 1) {
            set.add(num);
            num = numSum;
        } else {
            return true;
        }
    }
    return false;
};

/**
 * @description Finds happy numbers. Numbers are happy if the sum of the squares of their digits equals 1. Numbers are also happy if that sum is happy, and so on.
 *
 * @param {number} wanted - Number of happy numbers to find.
 * @returns List of happy numbers.
 */
export const search = (wanted: number): number[] => {
    const happyNums = [];
    for (let i = 1; happyNums.length < wanted; i++) {
        if (isHappy(i)) {
            happyNums.push(i);
        }
    }
    return happyNums;
};

/* istanbul ignore if */
if (require.main === module) {
    main({
        search,
        eval: isHappy
    }, ArgType.INT, (x: number) => x > 0, "Number");
}
