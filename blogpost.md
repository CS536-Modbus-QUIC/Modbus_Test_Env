# Implementation and design of Modbus over QUIC protocol for ICS network

**Para 1** ... describing the problem\
Modicon Communication Bus (Modbus) is one of the most popular industrial network protocols used in the industrial control system (ICS). It was initially developed to communicate between devices on a serial layer. Over the years, it has been enhanced into several variants to run over Ethernet and Internet Protocol.  Operating Modbus on the modern IP network is becoming more prevalent among industrial controlled systems, with many ICS networks facing targeted cyber-attacks and critical impact on system continuity. The current solution runs TLS on top of TCP to provide privacy and data integrity between two communicating parties. However, the TLS handshake process requires 2-RTT between the server and client. More unfortunate is that the connection is not always reliable, some phenomenons such as connection migration and packet loss can introduce additional overhead of establishing secure connections. Our goal is to build a new Modbus variant that provides source authentication and session encryption, with lower latency connectivity than the Modbus over TCP/TLS.\
**Para 2** ... what you did?\
We design and implement a full-blown Modbus protocol running over QUIC. QUIC transport eliminates the head-of-line blocking issues inherent with TCP and provides lower-latency connection establishment than TCP/TLS.  Our implementation is based on [pymodbus](https://pymodbus.readthedocs.io/en/latest/) and [aioquic](https://github.com/aiortc/aioquic). We evaluated the connection latency for QUIC and TCP/TLS on a mininet virtual network, where we can easily change the network conditions (delay, percentages of packet loss).\
**Para 3** ... discuss the most promising plot or result\
We observe that QUIC achieves a lower connection latency than TCP/TLS across all values of added delays.  The experiments on packet loss show that  QUIC connections are much less sensitive to loss than TCP/TLS connections.


> Link to GitHub repo:  
> [Running the Modbus QUIC in the virtual network (docker is required)](https://github.com/CS536-Modbus-QUIC/Modbus_Test_Env)\
> [Running the Modbus QUIC without the virtual network](https://github.com/CS536-Modbus-QUIC/aioquic/tree/main/examples)\
> Please follow the instructions within each link to run the Modbus over QUIC client and server. 






![Connection latency for QUIC connections in case of delay](https://github.com/CS536-Modbus-QUIC/Modbus_Test_Env/blob/main/plots/QUIC_delay_v3.png)
*Connection latency for QUIC connections in case of delay*
![Connection latency for TCP/TLS connections in case of delay](https://github.com/CS536-Modbus-QUIC/Modbus_Test_Env/blob/main/plots/TLS_delay_v3.png)
*Connection latency for TCP/TLS connections in case of delay*
![Connection latency for QUIC connections in case of loss](https://github.com/CS536-Modbus-QUIC/Modbus_Test_Env/blob/main/plots/QUIC_loss_v3.png)
*Connection latency for QUIC connections in case of loss*
![Connection latency for TCP/TLS connections in case of loss](https://github.com/CS536-Modbus-QUIC/Modbus_Test_Env/blob/main/plots/TLS_loss_v3.png)
*Connection latency for TCP/TLS connections in case of loss*
