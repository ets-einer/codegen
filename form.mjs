import { createFile, Field, getBase } from "./common.mjs";


/**
 * 
 * @param {Field[]} fields
 */
const fieldsToJSX = (fields) => {
    fields = fields.map(field => {
        return `<input type="${field.fieldInputType}" name="${field.fieldName}" value={formObject.${field.fieldName}} onChange={handleChange} />`
    })

    return fields.join('\n\t    ')
}

/**
 * 
 * @param {Field[]} fields 
 */
const fieldsToInterface = (fields) => {
    fields = fields.map(field => {
        return `${field.fieldName}: ${field.fieldType}`
    })

    return fields.join('\n    ')
}

/**
* 
* @param {string} name
* @param {string} _fields 
*/
const parseFields = (name, _fields) => {

    /**
     * 
     * @param {string} formName 
     * @returns 
     */
    function format(formName) {
        return formName[0].toUpperCase() + formName.slice(1).toLowerCase()
    }

    const fields = _fields.split(',').map(f => {
        f = f.split(":");
        return new Field(f[0], f[1])
    });

    const baseString = getBase('/bases/Form')
        .replace(/\%FORM_NAME%/g, format(name))
        .replace(/\%INPUTS_JSX%/g, fieldsToJSX(fields))
        .replace(/\%INPUTS_INTERFACE%/g, fieldsToInterface(fields))

    createFile(format(name) + ".tsx", baseString)
}

export default parseFields;