import axios from 'axios';

const domain = 'https://wa-XXX.4jawaly.com/';
const token = 'XXXXXXX';
const phone = '19292439373';
const body = 'test msg from type';
const quotedMsgId = '';

// Check if required fields are empty
if (!token) {
    console.log('token: It must not be a null value');
    process.exit(0);
}

if (!phone) {
    console.log('phone: It must not be a null value');
    process.exit(0);
}

if (!body) {
    console.log('body: It must not be a null value');
    process.exit(0);
}

const url = `${domain}api/v1/message/text`;

const params = {
    token,
    phone,
    body,
    quotedMsgId,
};

axios
    .post(url, params, { headers: { 'Accept': 'application/json' } })
    .then((response) => {
        const result = response.data;
        const code = result.code;
        const message = result.message;
        const id = result.id;

        console.log(`code: ${code}`);
        console.log(`message: ${message}`);
        console.log(`id: ${id}`);
    })
    .catch((error) => {
        const response = error.response;
        if (response) {
            const code = response.data.code;
            const message = response.data.message;

            console.log(`Error: ${code}`);
            console.log(`message: ${message}`);
        } else {
            console.log('Error: Failed to make the request');
        }
    });
