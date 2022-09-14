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
            case "text" || "email":
                return 'string'
            case "number":
                return 'number'
        }
    }
}

export const createFile = (name, data) => {
    const stream = createWriteStream(`forms/${name}`)
    stream.write(data)
}

export const getBase = (basePath) => fs.readFileSync(__dirname + basePath).toString()