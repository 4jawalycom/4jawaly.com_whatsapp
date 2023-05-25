<template>
    <div>
    <button @click="sendMessage" > Send Message < /button>
        < /div>
        < /template>

        <script>
export default {
    methods: {
        sendMessage() {
            const domain = 'https://wa-XXX.4jawaly.com/';
            const token = 'XXXXXXXX';
            const phone = '19292439373';
            const body = 'test msg from example';
            const quotedMsgId = '';

            const params = new URLSearchParams();
            params.append('token', token);
            params.append('phone', phone);
            params.append('body', body);
            params.append('quotedMsgId', quotedMsgId);

            fetch(`${domain}api/v1/message/text`, {
                method: 'POST',
                body: params,
                headers: {
                    Accept: 'application/json',
                },
            })
                .then((response) => response.json())
                .then((data) => {
                    const code = data.code;
                    const message = 'تم الارسال بنجاح';
                    const id = data.id;

                    console.log('code:', code);
                    console.log('message:', message);
                    console.log('id:', id);
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
        },
    },
};
</script>
