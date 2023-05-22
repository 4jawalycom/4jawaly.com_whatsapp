const axios = require('axios');

const domain = 'https://wa-116.4jawaly.com/';
const token = 'Wb2B1cUy59';
const phone = '19292439373';
const body = 'test msg from node js';
const quotedMsgId = '';

// Check if required fields are empty
if (!token) {
    console.log('token: It must not be a null value');
    return;
}

if (!phone) {
    console.log('phone: It must not be a null value');
    return;
}

if (!body) {
    console.log('body: It must not be a null value');
    return;
}

const params = {
    token,
    phone,
    body,
    quotedMsgId,
};

axios.post(domain + 'api/v1/message/text', params)
    .then((response) => {
        const { code, message, id } = response.data;
        console.log('code:', code);
        console.log('message:', message);
        console.log('id:', id);
    })
    .catch((error) => {
        if (error.response) {
            const { code, message } = error.response.data;
            console.log('Error:', code);
            console.log('message:', message);
        } else {
            console.log('Error:', error.message);
        }
    });
