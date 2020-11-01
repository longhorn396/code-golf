import { exit } from 'process';
import process = require('process');
import readline = require('readline-sync');

const getPromptResult = (prompt: string): string => {
    return readline.question(`${prompt}\n`);
}

export const toString = (input: any) => input.toString();

export const main = (fun: Function, transform: Function, ...prompts: string[]) => {
    const argv = process.argv;
    let args: any[] = [];
    if (argv.length > 2) {
        argv.slice(2, argv.length).forEach((arg: string) => args.push(transform(arg)));
    } else {
        prompts.forEach((prompt: string) => args.push(transform(getPromptResult(prompt))));
    }
    try {
        console.log(fun(...args));
        exit(0);
    } catch(e) {
        console.error(e);
        exit(1);
    }
} 