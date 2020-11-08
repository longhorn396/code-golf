/* istanbul ignore file */

import { performance } from "perf_hooks";
import { argv, exit } from "process";
import { question, questionFloat, questionInt } from "readline-sync";

/**
 * @typedef {number | string} Primative - Either a number or a string.
 */
type Primative = number | string;

/**
 * @interface Maps ArgTypes to parsers for argv and readline-sync.
 */
interface IArgTypeParseMap {
    [key: string]: { argv: Function, prompt: Function };
};

/**
 * @interface Maps function names to a function
 */
interface IFunctionMap {
    [key: string]: Function;
};

/**
 * @interface Maps function names to a number
 */
interface ITimesMap {
    [key: string]: number;
};

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
const argTypeParseMap: IArgTypeParseMap = {
    [ArgType.FLOAT]: { argv: parseFloat, prompt: questionFloat },
    [ArgType.INT]: { argv: parseInt, prompt: questionInt },
    [ArgType.STRING]: { argv: (input: Primative) => input.toString(), prompt: question }
};

/**
 * @description Uses a `readline` function to ask `prompt` to the user.
 *
 * @param {string}   prompt   - Prompt to the user for input.
 * @param {Function} readline - Either `question`, `questionFloat`, or `questionInt` from `readline-async`.
 * @returns {Primative} The result from the user.
 */
const askPrompt = (prompt: string, readline: Function): Primative => {
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
    const args: Primative[] = [];
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
 * @param {Primative[]}       args     - Arguments to pass to each function.
 * @returns {string} Newline-deliniated list of subfunctions and their average execution times.
 */
export const compareSubfs = (funs: IFunctionMap, attempts: number, args: Primative[]): string => {
    const subfNames: string[] = Object.keys(funs);
    const spaces: number = Math.max(...subfNames.map((fun: string) => fun.length));
    const timesMap: ITimesMap = {};
    for (let i = 0; i < attempts; i++) {
        subfNames.forEach((subfName: string) => {
            const fun: Function = funs[subfName];
            let time: number = timesMap[subfName] ? timesMap[subfName] : 0;
            time -= performance.now();
            fun(...args);
            time += performance.now();
            timesMap[subfName] = time;
        });
    }
    const results: string[] = subfNames.map((subfName: string) => {
        return `${subfName.padEnd(spaces)} average ms: ${(timesMap[subfName] / attempts).toFixed(15)}`
    });
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
export const mainSubf = (funs: IFunctionMap, argType: ArgType, check: Function, ...prompts: string[]): never => {
    const subfNames: string[] = Object.keys(funs);
    let subfName: string = null;
    const args: Primative[] = [];
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
        if (args.every((value: Primative) => check(value))) {
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
