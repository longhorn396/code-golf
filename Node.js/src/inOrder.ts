import { ArgType, compareSubfs, mainSubf as main } from './common';

/**
 * @description Test the internal alphabetical order of words. Written with branch prediction in mind.
 * 
 * @param {string} text - Words to test.
 * @returns {string} Newline-deliniated list of words and whethere or not they are in alphabetical order.
 */
export const inOrderBranchPrediction = (text: string): string => {
    const results: string[] = text.split(" ").map((word: string) => {
        const order: boolean = wordInOrderBranchPrediction(word);
        const result: string = `${word} -${order ? '' : ' not'} in order`;
        return result;
    });
    return results.join("\n");
};

/**
 * @description Test if the input word's characters are in alphabetical order. Written with branch prediction in mind.
 * 
 * @param {string} word - Word to test.
 * @returns {boolean} If the word is alphabetical or not.
 */
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

/**
 * @description Test the internal alphabetical order of words. Written with readability in mind.
 * 
 * @param {string} text - Words to test.
 * @returns {string} Newline-deliniated list of words and whethere or not they are in alphabetical order.
 */
export const inOrderReadability = (text: string): string => {
    const results: string[] = text.split(" ").map((word: string) => {
        const order: boolean = wordInOrderReadability(word);
        const result: string = `${word} -${order ? '' : ' not'} in order`;
        return result;
    });
    return results.join("\n");
};

/**
 * @description Test if the input word's characters are in alphabetical order. Written with readability in mind.
 * 
 * @param {string} word - Word to test.
 * @returns {boolean} If the word is alphabetical or not.
 */
export const wordInOrderReadability = (word: string): boolean => {
    const characters = word.split("");
    for (let i = 0; i < characters.length - 1; i++) {
        if (characters[i] > characters[i + 1]) {
            return false;
        }
    }
    return true;
};

/**
 * @description Test the internal alphabetical order of words. Uses a simple, probabability-based heuristic function on each word to guess the quicker `wordInOrder...` function to use.
 * 
 * @param {string} text - Words to test.
 * @returns {string} Newline-deliniated list of words and whethere or not they are in alphabetical order.
 */
export const inOrderHeuristic = (text: string): string => {
    const results: string[] = text.split(" ").map((word: string) => {
        const order: boolean = word.charAt(0) > 'm' ? wordInOrderReadability(word) : wordInOrderBranchPrediction(word);
        const result: string = `${word} -${order ? '' : ' not'} in order`;
        return result;
    });
    return results.join("\n");
}

main({
    branchPrediction: inOrderBranchPrediction,
    readability: inOrderReadability,
    heuristic: inOrderHeuristic,
    compare: compareSubfs
}, ArgType.STRING, (value: string) => value.length, "What word(s)?");
