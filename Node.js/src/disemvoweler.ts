import { ArgType, compareSubfs, mainSubf as main } from "./common";

/**
 * @description Separate consonants and vowels from text using Arrays internally.
 *
 * @param {string} text - Words to disemvowel.
 * @returns {string} The connsonants from the text followed by the removed vowels.
 */
export const disemvowelArrays = (text: string): string => {
    const cons: string[] = [];
    const vowels: string[] = [];
    text.split("").forEach((char: string) => {
        if ("aeiouAEIOU".includes(char)) {
            vowels.push(char);
        } else if (char >= "A" && char <= "z") {
            cons.push(char);
        }
    });
    return `${cons.join("")} ${vowels.join("")}`;
};

/**
 * @description Separate consonants and vowels from text using Strings internally.
 *
 * @param {string} text - Words to disemvowel.
 * @returns {string} The connsonants from the text followed by the removed vowels.
 */
export const disemvowelStrings = (text: string): string => {
    let cons: string = "";
    let vowels: string = "";
    text.split("").forEach((char: string) => {
        if ("aeiouAEIOU".includes(char)) {
            vowels += char;
        } else if (char >= "A" && char <= "z") {
            cons += char;
        }
    });
    return `${cons} ${vowels}`;
};

/* istanbul ignore if */
if (require.main === module) {
    main({
        arrays: disemvowelArrays,
        strings: disemvowelStrings,
        compare: compareSubfs
    }, ArgType.STRING, (value: string) => value.length, "What word(s)?");
}
