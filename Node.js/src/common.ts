import { exit } from 'process';
import process = require('process');

const stdin = process.openStdin();

const getPromptResult = (prompt: string): string => {
    let result: string = null;
    console.log(prompt);
    stdin.addListener("data", (d: any) => result = d.toString().trim());
    return result;
}

export const toString = (input: any) => input.toString();

export const main = (fun: Function, transform: Function, ...prompts: string[]) => {
    const argv = process.argv;
    let args: any[] = [];
    if (argv.length > 2) {
        argv.slice(2, argv.length).forEach((arg: string) => args.push(transform(arg)));
    } else {
        throw new Error("Prompting not supported at this time");
        // prompts.forEach((prompt: string) => args.push(transform(getPromptResult(prompt))));
    }
    try {
        console.log(fun(...args));
        exit(0);
    } catch(e) {
        console.error(e);
        exit(1);
    }
} 