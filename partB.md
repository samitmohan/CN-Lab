# How to do Part B

Full Duplex : Switches, Routers
Half Duplex : Hubs

Open in NCTU mode (OS) 
1) open 3 terminals : dispatcher, coordinator, nctunsclient
2) Draw network topology (acc to question)
3) Click on edit, ADD : select full duplex, log stats
4) Add commands -:
    Host 1 : stg -u 1024 100 1.0.1.2
    Host 2 : rtf -u -w log1
5) Playback : Run Simulation : Go to draw graph : graph of inputoutputthroughput.

For TCP Exp 2
Host : stcp -p 7000 -l 1024 1.0.1.6
Client : rtcp -p 7000 -l 1024


For Exp 3  : same commands
For Exp 4 : UDP(1) + TCP(2)
    stg -u 1024 100 1.0.1.3
    rtg -u -w log1
    stcp -p 7000 -l 1024 1.0.1.3
    rtcp -p 7000 -l 1024

Exp 5 : No commands, topology run and click on host and ping destination node (ping 1.0.1.3 command quickly in Run Mode)

Exp 6 : watch video, draw topology
Commands : ttcp connection b/w nodes and host
    ttcp -r -u -s -p 7000