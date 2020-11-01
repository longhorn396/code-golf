import process = require('process');
import inquirer = require('inquirer');

export const main = (fun: Function, transform: Function, prompts: string[]) => {
    const argv = process.argv;
    let args: any[] = [];
    if (argv.length > 2) {
        argv.slice(3, argv.length).forEach((arg: string) => args.push(transform(arg)));
    } else {
        inquirer.prompt(prompts).then((answer: any) => args.push(transform(answer)));
    }
    try {
        console.log(fun(...args));
    } catch(e) {
        console.error(e);
    }
} 