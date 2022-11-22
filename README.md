# mkg

Codegen CLI tool for React Typescript projects

Includes Formik + Yup support for generating forms

Don't think about form or inputs state, writing boilerplate like labels, typescript interfaces or error displays. Just style the form to your liking and write the dead simple Yup validations, and Formik gives you a type-safe object so you can post to your back-end or anything you would like.

Example: 

    mkg form register --errors --placeholder name,email:email,age:number

Result:

**src/forms/RegisterForm.tsx**
```tsx
import { Formik, Field, Form, FormikHelpers } from 'formik';
import * as Yup from 'yup';

const CadastroSchema = Yup.object().shape({
    nome: Yup.string(),
    email: Yup.string(),
    age: Yup.number()
});

interface RegisterValues {
    nome: string
    email: string
    age: number
}

const RegisterForm = () => {

    const handleSubmit = (values: RegisterValues, 
    { setSubmitting }: FormikHelpers<RegisterValues>) => {
        console.log(values)
    }

    return (
        <div>
            <h1>Register</h1>
            <Formik
                initialValues={{
                    nome: '',
                    email: '',
                    age: 0
                }}
                validationSchema={RegisterSchema}
                onSubmit={handleSubmit}>
                {({ errors, touched }) => (
                <Form>
                    <Field id="nome" type="text" name="nome" placeholder="nome" />
                    {errors.nome && touched.nome ? (
                        <div>{errors.nome}</div>
                    ) : null}
                    <Field id="email" type="email" name="email" placeholder="email" />
                    {errors.email && touched.email ? (
                        <div>{errors.email}</div>
                    ) : null}
                    <Field id="age" type="number" name="age" placeholder="age" />
                    {errors.age && touched.age ? (
                        <div>{errors.age}</div>
                    ) : null}
                    <button type="submit">Submit</button>
                </Form>
                )}
            </Formik>
        </div>
    );
}

export default RegisterForm;
```

---

## Installation

Windows

```bash
cmd /k "git clone https://github.com/tcc-ets/codegen.git && cd codegen && pip install . && cd .. && rmdir /s /q codegen"
```