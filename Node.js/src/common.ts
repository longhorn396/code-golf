/* istanbul ignore file */

import { performance } from "perf_hooks";
import { argv, exit } from "process";
import { question, questionFloat, questionInt } from "readline-sync";

/**
 * @description Argument types
 * @enum {string}
 */
export enum ArgType {
    FLOAT = "FLOAT",
    INT = "INT",
    STRING = "STRING",
};

/**
 * @type {Object.<ArgType, Object>}
 */
const argTypeParseMap = {
    [ArgType.FLOAT]: { argv: parseFloat, prompt: questionFloat },
    [ArgType.INT]: { argv: parseInt, prompt: questionInt },
    [ArgType.STRING]: { argv: (input: any) => input.toString(), prompt: question }
};

/**
 * @description Uses a `readline` function to ask `prompt` to the user.
 *
 * @param {string}   prompt   - Prompt to the user for input.
 * @param {Function} readline - Either `question`, `questionFloat`, or `questionInt` from `readline-async`.
 * @returns {string | number} The result from the user.
 */
const askPrompt = (prompt: string, readline: Function): string | number => {
    return readline(`${prompt}\n`);
};

/**
 * @description Command-line runner for modules with only one function.
 *
 * @param {Function} fun     - Function to run.
 * @param {ArgType}  argType - Argument type.
 * @param {string[]} prompts - Prompts to ask the user for input.
 */
export const main = (fun: Function, argType: ArgType, ...prompts: string[]): never => {
    const args: any[] = [];
    const argTypeParsers = argTypeParseMap[argType];
    if (argv.length > 2) {
        argv.slice(2, argv.length).forEach((arg: string) => args.push(argTypeParsers.argv(arg)));
    } else {
        prompts.forEach((prompt: string) => args.push(askPrompt(prompt, argTypeParsers.prompt)));
    }
    try {
        console.log(fun(...args));
        exit(0);
    } catch (e) {
        console.error(e);
        exit(1);
    }
};

/**
 * @description Compuets the average execution times of functions.
 *
 * @param {Object.<string, Function>} funs     - Functions to compare.
 * @param {number}                    attempts - Number of times to run each function.
 * @param {string[] | number[]}       args     - Arguments to pass to each function.
 * @returns {string} Newline-deliniated list of subfunctions and their average execution times.
 */
export const compareSubfs = (funs: any, attempts: number, args: string[] | number[]): string => {
    const subfNames: string[] = Object.keys(funs);
    const spaces: number = Math.max(...subfNames.map((fun: string) => fun.length));
    const times: any[] = subfNames.map((subfName: string) => {
        return { name: subfName, fun: funs[subfName] };
    });
    const timesMap: any = {};
    for (let i = 0; i < attempts; i++) {
        for (let j = 0; j < times.length; j++) {
            const { fun, name } = times[j];
            let time: number = timesMap[name] ? timesMap[name] : 0;
            time -= performance.now();
            fun(...args);
            time += performance.now();
            timesMap[name] = time;
        }
    }
    const results: string[] = times.map((result: any) => `${result.name.padEnd(spaces)} average ms: ${(timesMap[result.name] / attempts).toFixed(15)}`);
    return results.join("\n");
};

/**
 * @description Command-line runner for modules with multiple functions.
 *
 * @throws Error if any user input is invalid.
 *
 * @param {Object.<string, Function>} funs    - Functions to compare.
 * @param {ArgType}                   argType - Argument type.
 * @param {Function}                  check   - Function to ensure arguments are valid
 * @param {string[]}                  prompts - Prompts to ask the user for input.
 */
export const mainSubf = (funs: any, argType: ArgType, check: Function, ...prompts: string[]): never => {
    const subfNames: string[] = Object.keys(funs);
    let subfName: string = null;
    const args: any[] = [];
    const argTypeParsers = argTypeParseMap[argType];
    if (argv.length > 2) {
        subfName = argv[2];
    } else {
        console.log("What subfunction would you like to do?");
        subfName = askPrompt(`Options: ${subfNames.join(", ")}`, question) as string;
    }
    if (subfNames.includes(subfName)) {
        if (argv.length > 3) {
            argv.slice(3, argv.length).forEach((arg: string) => args.push(argTypeParsers.argv(arg)));
        } else {
            prompts.forEach((prompt: string) => args.push(askPrompt(prompt, argTypeParsers.prompt)));
        }
        if (args.every((value: any) => check(value))) {
            if (subfName === "compare") {
                const compare: Function = funs.compare;
                delete funs.compare;
                console.log(compare(funs, askPrompt("Attempts:", questionInt), args));
            } else {
                console.log(funs[subfName](...args));
            }
            exit(0);
        } else {
            throw new Error("Make sure you pass in valid arguments");
        }
    } else {
        throw new Error("Make sure you pass in a valid subfunction");
    }
};
