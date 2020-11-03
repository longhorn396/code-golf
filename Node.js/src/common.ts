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
};

export const mainSubf = (funs: any, argType: ArgType, check: Function, ...prompts: string[]) => {
    const subfNames: string[] = Object.keys(funs);
    let subfName: string = null;
    let args: any[] = [];
    const argTypeParsers = argTypeParseMap[argType];
    if (argv.length > 2) {
        subfName = argv[2];
    } else {
        console.log("What subfunction would you like to do?")
        subfName = askPrompt(`Options: ${subfNames.join(", ")}`, question);
    }
    if (subfNames.includes(subfName)) {
        if (argv.length > 3) {
            argv.slice(3, argv.length).forEach((arg: string) => args.push(argTypeParsers.argv(arg)));
        } else {
            prompts.forEach((prompt: string) => args.push(askPrompt(prompt, argTypeParsers.prompt)));
        }
        if (args.every((value: any) => check(value))) {
            // TODO: Compare
            console.log(funs[subfName](...args));
            exit(0);
        } else {
            throw new Error("Make sure you pass in valid arguments");
        }
    } else {
        throw new Error("Make sure you pass in a valid subfunction");
    }
};
