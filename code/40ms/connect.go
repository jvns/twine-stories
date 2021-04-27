package main

import "fmt"
import "net"
import "sync"
import "bufio"

func main() {
	var wg sync.WaitGroup
	for i := 1; i < 5; i++ {
		wg.Add(1)
		go send_request(&wg)
	}
	wg.Wait()
}

func send_request(wg *sync.WaitGroup) {
	defer wg.Done()
	target := "mysterybox-1404:8000"
	raddr, err := net.ResolveTCPAddr("tcp", target)
	conn, err := net.DialTCP("tcp", nil, raddr)
	conn.SetNoDelay(false)
	if err != nil {
		fmt.Println("error", err)
		return
	}
	fmt.Fprintf(conn, "GET / HTTP/1.0\r\n")
	fmt.Fprintf(conn, "Host: example.com\r\n\r\n")
	bufio.NewReader(conn).ReadString('\n')
}
