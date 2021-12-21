package gocg

import (
	"errors"
	"fmt"
	"os"
	"reflect"
)

func FindSubf(subfs interface{}) (string, error) {
	var subf string
	keys := reflect.ValueOf(subfs).MapKeys()
	if len(os.Args) > 1 {
		subf = os.Args[1]
	} else {
		fmt.Println("What subfunction would you like to do?")
		fmt.Println("Options: ", keys)
		fmt.Scanln(&subf)
	}
	for _, key := range keys {
		if subf == key.Interface().(string) {
			return subf, nil
		}
	}
	return "", errors.New("No matching subfunction for " + subf)
}
