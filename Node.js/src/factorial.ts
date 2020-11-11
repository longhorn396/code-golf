import { ArgType, compareSubfs, mainSubf as main } from "./common";

/**
 * @description Iterative factorial solution using a for loop.
 *
 * @param {number} num - Number to compute factorial.
 * @returns Factorial of `num`.
 */
export const forLoopFactorial = (num: number): number => {
    let result = 1;
    for (let i = 2; i <= num; i++) {
        result *= i;
    }
    return result;
};

/**
 * @description Iterative factorial solution using a while loop.
 *
 * @param {number} num - Number to compute factorial.
 * @returns Factorial of `num`.
 */
export const whileLoopFactorial = (num: number): number => {
    let result = 1;
    while (num > 1) {
        result *= num--;
    }
    return result;
};

/**
 * @description Recursive factorial solution.
 *
 * @param {number} num - Number to compute factorial.
 * @returns Factorial of `num`.
 */
export const recursiveFactorial = (num: number): number => {
    if (num >= 2) {
        return num * recursiveFactorial(--num);
    }
    return 1;
};

/**
 * @description Tail recursive factorial solution.
 *
 * @param {number} num - Number to compute factorial.
 * @param {number} result - Tail recursive result carrier.
 * @returns Factorial of `num`.
 */
export const tailFactorial = (num: number, result: number = 1): number => {
    if (num >= 2) {
        return tailFactorial(num - 1, num * result);
    }
    return result;
};

/**
 * @description Iterative factorial solution using an array similar to a Python2 range.
 *
 * @param {number} num - Number to compute factorial.
 * @returns Factorial of `num`.
 */
export const arrayFactorial = (num: number): number => {
    let result = 1;
    for (const x of Array.from(new Array(num - 1), (x, i) => i + 2)) {
        result *= x;
    }
    return result;
};

/**
 * @description Factorial solution reducing an array similar to a Python2 range.
 *
 * @param {number} num - Number to compute factorial.
 * @returns Factorial of `num`.
 */
export const reduceFactorial = (num: number): number => {
    return Array.from(new Array(num - 1), (x, i) => i + 2).reduce((prev: number, curr: number) => prev * curr);
};

/* istanbul ignore if */
if (require.main === module) {
    main({
        forloop: forLoopFactorial,
        whileloop: whileLoopFactorial,
        recursive: recursiveFactorial,
        tail: tailFactorial,
        array: arrayFactorial,
        reduce: reduceFactorial,
        compare: compareSubfs
    }, ArgType.INT, (num: number) => num >= 0 && num < 996, "Number");
}
