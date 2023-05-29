package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"net/url"
)

type Params struct {
	Token       string `json:"token"`
	Phone       string `json:"phone"`
	Body        string `json:"body"`
	QuotedMsgId string `json:"quotedMsgId"`
	Filename    string `json:"filename"`
}

func main() {
	domain := "https://wa-XXX.4jawaly.com/"
	params := Params{
		Token:       "XXXXXXXXX",
		Phone:       "19292439373",
		Body:        "https://cdn-dev.4jawaly.com/spam-regulation.pdf",
		QuotedMsgId: "",
		Filename:    "filename.pdf",
	}

	if params.Token == "" {
		fmt.Println("token: It must not be a null value")
		return
	}

	if params.Phone == "" {
		fmt.Println("phone: It must not be a null value")
		return
	}

	if params.Body == "" {
		fmt.Println("body: It must not be a null value")
		return
	}

	url := domain + "api/v1/message/file"
	headers := map[string]string{
		"Accept": "application/json",
	}

	data, err := json.Marshal(params)
	if err != nil {
		fmt.Println(err)
		return
	}

	resp, err := http.Post(url, "application/json", bytes.NewBuffer(data))
	if err != nil {
		fmt.Println(err)
		return
	}
	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println(err)
		return
	}

	var result map[string]interface{}
	err = json.Unmarshal(body, &result)
	if err != nil {
		fmt.Println(err)
		return
	}

	code := result["code"].(string)
	if resp.StatusCode == http.StatusOK {
		fmt.Println("code:", code)
		fmt.Println("message: تم الارسال بنجاح")
		fmt.Println("id:", result["id"].(string))
	} else {
		fmt.Println("code:", code)
		fmt.Println("message:", result["message"].(string))
	}
}
