package main

import (
	"context"
	"fmt"
	"log"
	"net"
	"net/http"
	"syscall"
)

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hi there, I love %s!", r.URL.Path[1:])
}

func main() {
	http.HandleFunc("/", handler)
	config := &net.ListenConfig{Control: reusePort}
	ln, err := config.Listen(context.Background(), "tcp", ":8000") // bind to the address:port
	if err != nil {
		fmt.Println(err)
		return
	}
	log.Fatal(http.Serve(ln, nil))
}

func reusePort(network, address string, conn syscall.RawConn) error {
	return conn.Control(func(descriptor uintptr) {
		syscall.SetsockoptInt(int(descriptor), syscall.IPPROTO_TCP, syscall.TCP_QUICKACK, 0)
		syscall.SetsockoptInt(int(descriptor), syscall.SOL_SOCKET, 0xf, 0) // SO_REUSEPORT
	})
}
