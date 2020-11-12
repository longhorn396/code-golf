import { ArgType, compareSubfs, mainSubf as main } from "./common";

export interface IFibonacciOutput {
    i: number;
    fibonacciNumber: number;
    sequence: number[];
};

export const dumbFibonacci = (i: number): IFibonacciOutput => {
    if (i <= 1) {
        return { i, fibonacciNumber: 0, sequence: [0] };
    } else if (i === 2) {
        return { i, fibonacciNumber: 1, sequence: [0, 1] };
    }
    const result1 = dumbFibonacci(i - 1);
    const result2 = dumbFibonacci(i - 2);
    const fibonacciNumber = result1.fibonacciNumber + result2.fibonacciNumber;
    const sequence: number[] = result1.sequence;
    sequence.push(fibonacciNumber);
    return { i, fibonacciNumber, sequence };
};

export const lessDumbFibonacci = (i: number): IFibonacciOutput => {
    if (i <= 1) {
        return { i, fibonacciNumber: 0, sequence: [0] };
    } else if (i === 2) {
        return { i, fibonacciNumber: 1, sequence: [0, 1] };
    }
    const result = lessDumbFibonacci(i - 1);
    const { sequence } = result;
    const len = sequence.length;
    const fibonacciNumber = sequence[len - 1] + sequence[len - 2];
    return { i, fibonacciNumber, sequence };
};

export const iterativeFibonacci = (i: number): IFibonacciOutput => {
    if (i <= 1) {
        return { i, fibonacciNumber: 0, sequence: [0] };
    }
    const sequence = [0, 1];
    while (i > sequence.length) {
        const len = sequence.length;
        sequence.push(sequence[len - 1], sequence[len - 2]);
    }
    return { i, fibonacciNumber: sequence[sequence.length - 1], sequence };
};

export const recursiveFibonacci = (i: number, sequence: number[] = null): IFibonacciOutput => {
    if (i <= 1) {
        return { i, fibonacciNumber: 0, sequence: [0] };
    } else if (i === 2) {
        return { i, fibonacciNumber: 1, sequence: [0, 1] };
    }
    if (sequence === null) {
        sequence = [0, 1];
    }
    if (i > sequence.length) {
        const len = sequence.length;
        sequence.push(sequence[len - 1], sequence[len - 2]);
        return recursiveFibonacci(i, sequence);
    }
    return { i, fibonacciNumber: sequence[sequence.length - 1], sequence };
};

/* istanbul ignore if */
if (require.main === module) {
    main({
        dumb: dumbFibonacci,
        lessDumb: lessDumbFibonacci,
        iterative: iterativeFibonacci,
        recursive: recursiveFibonacci,
        compare: compareSubfs
    }, ArgType.INT, (x: number) => x >= 1, "Number");
}
