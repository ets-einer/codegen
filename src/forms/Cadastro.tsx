import React from 'react'
import { Formik, Field, Form, FormikHelpers } from 'formik';

interface CadastroValues {
    name: string
    email: string
    idade: number
    nascimento: Date
}

const CadastroForm = () => {

    const handleSubmit = (values: CadastroValues, 
    { setSubmitting }: FormikHelpers<CadastroValues>) => {
        console.log(values)
    }

    return (
        <div>
            <h1>Cadastro</h1>
            <Formik
                initialValues={{
                    name: '',
					email: '',
					idade: 0,
					nascimento: new Date()
                }}
                onSubmit={handleSubmit}>
                <Form>
                    <label htmlFor="name">Name</label>
					<Field id="name" type="text" name="name" placeholder="name" />
					<label htmlFor="email">Email</label>
					<Field id="email" type="email" name="email" placeholder="email" />
					<label htmlFor="idade">Idade</label>
					<Field id="idade" type="number" name="idade" placeholder="idade" />
					<label htmlFor="nascimento">Nascimento</label>
					<Field id="nascimento" type="date" name="nascimento" placeholder="nascimento" />
                    <button type="submit">Submit</button>
                </Form>
            </Formik>
        </div>
    );
}

export default CadastroForm;