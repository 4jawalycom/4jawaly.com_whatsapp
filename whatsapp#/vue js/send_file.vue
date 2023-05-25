<template>
    <div>
    <button @click="sendFile" > Send File < /button>
        < /div>
        < /template>

        <script>
export default {
    methods: {
        sendFile() {
            const domain = 'https://wa-XXX.4jawaly.com/';
            const token = 'XXXXXXXXX';
            const phone = '19292439373';
            const body = 'https://cdn-dev.4jawaly.com/spam-regulation.pdf';
            const quotedMsgId = '';
            const filename = 'filename.pdf';

            const params = new URLSearchParams();
            params.append('token', token);
            params.append('phone', phone);
            params.append('body', body);
            params.append('quotedMsgId', quotedMsgId);
            params.append('filename', filename);

            fetch(`${domain}api/v1/message/file`, {
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
