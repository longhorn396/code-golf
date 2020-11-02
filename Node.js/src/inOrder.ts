import { main, ArgType } from './common';

export const inOrder = (text: string): string => {
    const results: string[] = text.split(" ").map((word: string) => {
        const order: boolean = wordInOrder(word);
        const result: string = `${word} -${order ? '' : ' not'} in order`;
        return result;
    });
    return results.join("\n");
};

// TODO: branch prediction vs simplicity?
export const wordInOrder = (word: string): boolean => {
    const characters = word.split("");
    for (let i = 0; i < characters.length - 1; i++) {
        if (characters[i] <= characters[i + 1]) {
            continue;
        }
        return false;
    }
    return true;
};

main(inOrder, ArgType.STRING, "What word(s)?");
