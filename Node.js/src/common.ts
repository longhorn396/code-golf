import { argv, exit } from 'process';
import { question, questionFloat, questionInt } from 'readline-sync';

const askPrompt = (prompt: string, readline: Function): any => {
    return readline(`${prompt}\n`)
}

export const stringPromptResults = (prompt: string): string => {
    return askPrompt(prompt, question);
}

export const floatPromptResults = (prompt: string): number => {
    return askPrompt(prompt, questionFloat);
}

export const intPromptResults = (prompt: string): number => {
    return askPrompt(prompt, questionInt);
}

export const toString = (input: any) => input.toString();

export const main = (fun: Function, transform: Function, promptResults: Function, ...prompts: string[]) => {
    let args: any[] = [];
    if (argv.length > 2) {
        argv.slice(2, argv.length).forEach((arg: string) => args.push(transform(arg)));
    } else {
        prompts.forEach((prompt: string) => args.push(promptResults(prompt)));
    }
    try {
        console.log(fun(...args));
        exit(0);
    } catch(e) {
        console.error(e);
        exit(1);
    }
} 