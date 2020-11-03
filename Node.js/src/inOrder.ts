import { ArgType, mainSubf as main } from './common';

export const inOrderBranchPrediction = (text: string): string => {
    const results: string[] = text.split(" ").map((word: string) => {
        const order: boolean = wordInOrderBranchPrediction(word);
        const result: string = `${word} -${order ? '' : ' not'} in order`;
        return result;
    });
    return results.join("\n");
};

export const wordInOrderBranchPrediction = (word: string): boolean => {
    const characters = word.split("");
    for (let i = 0; i < characters.length - 1; i++) {
        if (characters[i] <= characters[i + 1]) {
            continue;
        }
        return false;
    }
    return true;
};

export const inOrderReadability = (text: string): string => {
    const results: string[] = text.split(" ").map((word: string) => {
        const order: boolean = wordInOrderReadability(word);
        const result: string = `${word} -${order ? '' : ' not'} in order`;
        return result;
    });
    return results.join("\n");
};

export const wordInOrderReadability = (word: string): boolean => {
    const characters = word.split("");
    for (let i = 0; i < characters.length - 1; i++) {
        if (characters[i] > characters[i + 1]) {
            return false;
        }
    }
    return true;
};

main({
    branchPrediction: inOrderBranchPrediction,
    readability: inOrderReadability
}, ArgType.STRING, (value: string) => value.length, "What word(s)?");
