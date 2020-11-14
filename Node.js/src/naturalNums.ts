import { ArgType, main } from "./common";

/**
 * @interface Maps a number to an array of numbers.
 */
interface INumberMap {
    [key: number]: number[];
}

/**
 * @description Find the nth natural number.
 *
 * @param {number} n The Nth natural number to find.
 * @param {number} limit The maximum counting number to link together to find `n`.
 */
export const findNthNaturalNumber = (n: number, limit: number): string => {
    if (n < 1) {
        throw new Error("`n` must be greater than or equal to 1");
    }
    const numberMap: INumberMap = {};
    const numbers = [];
    let prevLength = 0;
    for (let i = 1; i <= limit; i++) {
        numbers.push(i);
        const newLength = i.toString().length + prevLength;
        for (let j = prevLength + 1; j <= newLength; j++) {
            numberMap[j] = [prevLength, newLength];
        }
        if (newLength >= n) {
            break;
        }
        prevLength = newLength;
    }
    const naturalNumberString = numbers.join("");
    if (n > naturalNumberString.length) {
        throw new Error("`limit` too small.");
    }
    return `The natural number is ${naturalNumberString[n - 1]} in ${naturalNumberString.slice(numberMap[n][0], numberMap[n][1])}`;
};

/* istanbul ignore if */
if (require.main === module) {
    main(findNthNaturalNumber, ArgType.INT, "Which natural number?", "How many counting numbers to join?");
}
