import { argv, exit } from 'process';
import { question, questionFloat, questionInt } from 'readline-sync';

export enum ArgType {
    FLOAT = 'FLOAT',
    INT = 'INT',
    STRING = 'STRING',
};

const argTypeParseMap = {
    [ArgType.FLOAT]: { argv: parseFloat, prompt: questionFloat },
    [ArgType.INT]: { argv: parseInt, prompt: questionInt },
    [ArgType.STRING]: { argv: (input: any) => input.toString(), prompt: question }
};

const askPrompt = (prompt: string, readline: Function): any => {
    return readline(`${prompt}\n`)
};

export const main = (fun: Function, argType: ArgType, ...prompts: string[]) => {
    let args: any[] = [];
    const argTypeParsers = argTypeParseMap[argType];
    if (argv.length > 2) {
        argv.slice(2, argv.length).forEach((arg: string) => args.push(argTypeParsers.argv(arg)));
    } else {
        prompts.forEach((prompt: string) => args.push(askPrompt(prompt, argTypeParsers.prompt)));
    }
    try {
        console.log(fun(...args));
        exit(0);
    } catch(e) {
        console.error(e);
        exit(1);
    }
} 