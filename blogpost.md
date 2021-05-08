
# Implementation and design of Modbus QUIC protocol for ICS network

**Para 1** ... describing the problem\
Modicon Communication Bus (Modbus) is an application layer protocol for client-server communication between a supervisory server and a controlled device in the industrial control system (ICS) network. The popularity of Modbus is mainly due to its real-time performance, and the trade-off is that Modbus has no security features. Notwithstanding that the ICS devices are usually constrained in terms of memory, CPU, and power capacities, adding security layers such as TLS imposes high overhead.  Our goal is to build a new Modbus variant that provides source authentication and session encryption, with much less overhead than the current Modbus/TCP TLS solution.\
**Para 2** ... what you did?\
We design and implement a full-blown Modbus protocol running over QUIC. QUIC transport eliminates the head-of-line blocking issues inherent with TCP and provides lower-latency connection establishment than TCP/TLS.  Our implementation is based on [pymodbus](https://pymodbus.readthedocs.io/en/latest/) and [aioquic](https://github.com/aiortc/aioquic). We evaluated the connection latency for QUIC and TCP TLS on a MININET virtual network, where we can easily change the network conditions (delay, percentages of packet loss). \ 
**Para 3** ... discuss the most promising plot or result\
We observer that QUIC achieves a lower connection latency than TCP/TLS across all values of added delays.  The experiments on packet loss show that  QUIC connections are much less sensitivet o loss than TCP/TLS connections.\


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
