import path from 'path';
import { fileURLToPath } from 'url';
import fs, { createWriteStream } from 'fs';

const __filename = fileURLToPath(import.meta.url);

export const __dirname = path.dirname(__filename);

export class Field {
    constructor(fieldName, fieldType) {
        this.fieldName = fieldName
        this.fieldInputType = fieldType ? fieldType : 'text'

        this.fieldType = this.getType()
    }

    getType() {
        switch (this.fieldInputType) {
            case "text":
                return 'string'
            case "email":
                return 'string'
            case "number":
                return 'number'
            case "pass":
                this.fieldInputType = 'password'
                return 'string'
            case "date":
                return 'Date'
        }
    }
}

export const createFile = (name, data, folder) => {
    fs.mkdir(folder, { recursive: true }, (err) => {
        if (err) throw err;
    });
    const stream = createWriteStream(`${folder}${name}`)
    stream.write(data)
}


export const getBase = (basePath) => fs.readFileSync(__dirname + basePath).toString()