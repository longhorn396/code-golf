import { ArgType, main } from "./common";

export const disemvowel = (text: string): string => {
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

/* istanbul ignore if */
if (require.main === module) {
    main(disemvowel, ArgType.STRING, "What word(s)?");
}
