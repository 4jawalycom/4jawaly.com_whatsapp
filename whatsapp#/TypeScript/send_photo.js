import axios from 'axios';

const domain = "https://wa-XXX.4jawaly.com/";
const params = {
    token: "XXXXXXXX",
    phone: "19292439373",
    body: "https://i0.wp.com/www.4jawaly.com/wp-content/uploads/2019/05/itservice2_pic2.png",
    quotedMsgId: "",
    caption: "الرسالة اسفل الصورة",
    filename: "photo_name.png"
};

if (!params.token) {
    console.log("token: It must not be a null value");
    process.exit();
}

if (!params.phone) {
    console.log("phone: It must not be a null value");
    process.exit();
}

if (!params.body) {
    console.log("body: It must not be a null value");
    process.exit();
}

const url = `${domain}api/v1/message/file`;
const headers = { Accept: "application/json" };

axios.post(url, params, { headers })
    .then(response => {
        const result = response.data;
        const code = result.code;
        const message = response.status === 200 ? "تم الارسال بنجاح" : result.message;
        const id = result.id;

        console.log(`code: ${code}`);
        console.log(`message: ${message}`);
        console.log(`id: ${id}`);
    })
    .catch(error => {
        if (error.response) {
            const result = error.response.data;
            const code = result.code;
            const message = result.message;

            console.log(`code: ${code}`);
            console.log(`message: ${message}`);
        } else {
            console.log(error.message);
        }
    });
