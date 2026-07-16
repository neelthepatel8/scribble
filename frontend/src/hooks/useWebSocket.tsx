import React, {useEffect, useRef} from "react";

function useWebSocket(url: string) {
    const socketRef = useRef<WebSocket | null>(null);

    useEffect(() => {
        const socket = new WebSocket(url);

        socket.onopen = () => {
            console.log("ws connection established");
        };

        socket.onmessage = (event) => {
            console.log('receieved', event.data);
        };

        socket.onerror = (error) => {
            console.error("websocket error:", error);
        };

        socket.onclose = () => {
            socket.close();
        };

        socketRef.current = socket;

    }, [url]);

}

export default useWebSocket;