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
            const token = 'XXXX';
            const phone = '19292439373';
            const body = 'https://i0.wp.com/www.4jawaly.com/wp-content/uploads/2019/05/itservice2_pic2.png';
            const quotedMsgId = '';
            const filename = 'photo_name.png';
            const sendMediaAsDocument = 1;
            const stickerName = 'stickerName';

            const params = new URLSearchParams();
            params.append('token', token);
            params.append('phone', phone);
            params.append('body', body);
            params.append('quotedMsgId', quotedMsgId);
            params.append('filename', filename);
            params.append('sendMediaAsDocument', sendMediaAsDocument);
            params.append('stickerName', stickerName);

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
