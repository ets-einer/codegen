import { program } from 'commander'
import formAction from './form.mjs'


program
    .name('nodecli')
    .description('React/Fastify TS code generator')
    .version('Beta')

program
    .command('form')
    .description('Generates a form')
    .argument('<formName>', 'The form component name')
    .argument('<fields>', 'Form fields. Example: name,age:number,email:email')
    .action(formAction)


program.parse()