package main

import (
	"encoding/json"
	"fmt"
	"os"
	"time"
)

type Resource struct {
	ID           int       `json:"id"`
	Name         string    `json:"name"`
	Provider     string    `json:"provider"`
	Type         string    `json:"type"`
	Created      time.Time `json:"created"`
	Updated      time.Time `json:"updated"`
	CpuUtil      float32   `json:"cpu_util"`
	MemUtil      float32   `json:"mem_util"`
	TotalSpaceGb int       `json:"total_space_gb"`
	FreeSpaceGb  float32   `json:"free_space_gb"`
}

func importJSONDataFromFile(fileName string, result interface{}) (isOK bool) {
	isOK = true
	content, err := os.ReadFile(fileName)
	if err != nil {
		fmt.Print("Error:", err)
		isOK = false
	}
	err = json.Unmarshal(content, result)
	if err != nil {
		isOK = false
		fmt.Print("Error:", err)
	}
	return
}
