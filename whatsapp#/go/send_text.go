package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

type Message struct {
	Token         string `json:"token"`
	Phone         string `json:"phone"`
	Body          string `json:"body"`
	QuotedMsgID   string `json:"quotedMsgId"`
}

type Response struct {
	Code    int    `json:"code"`
	Message string `json:"message"`
	ID      string `json:"id"`
}

func main() {
	domain := "https://wa-XXX.4jawaly.com/"
	message := Message{
		Token:       "XXXXXXXX",
		Phone:       "19292439373",
		Body:        "test msg from Go",
		QuotedMsgID: "",
	}

	// Check if required fields are empty
	if message.Token == "" {
		fmt.Println("token: It must not be a null value")
		return
	}

	if message.Phone == "" {
		fmt.Println("phone: It must not be a null value")
		return
	}

	if message.Body == "" {
		fmt.Println("body: It must not be a null value")
		return
	}

	// Convert message to JSON
	jsonData, err := json.Marshal(message)
	if err != nil {
		fmt.Println("Error marshaling JSON:", err)
		return
	}

	// Send POST request
	url := domain + "api/v1/message/text"
	resp, err := http.Post(url, "application/json", bytes.NewBuffer(jsonData))
	if err != nil {
		fmt.Println("Error sending POST request:", err)
		return
	}
	defer resp.Body.Close()

	// Read response body
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println("Error reading response body:", err)
		return
	}

	// Check response status code
	if resp.StatusCode == http.StatusOK {
		var response Response
		err = json.Unmarshal(body, &response)
		if err != nil {
			fmt.Println("Error unmarshaling JSON response:", err)
			return
		}

		fmt.Println("code:", response.Code)
		fmt.Println("message:", response.Message)
		fmt.Println("id:", response.ID)
	} else {
		var errorResponse Response
		err = json.Unmarshal(body, &errorResponse)
		if err != nil {
			fmt.Println("Error unmarshaling JSON error response:", err)
			return
		}

		fmt.Println("Error:", resp.StatusCode)
		fmt.Println("message:", errorResponse.Message)
	}
}
