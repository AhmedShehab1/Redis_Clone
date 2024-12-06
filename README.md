# Redis Clone in Python  

## Overview  
This is a lightweight Redis clone implemented in Python, designed to emulate core Redis functionalities while providing a clean and modular codebase for extensibility. Currently, the project supports essential Redis commands such as `PING`, `ECHO`, `SET`, `GET`, and `CONFIG GET`. 

The project is built with a focus on clean Object-Oriented Design (OOD), leveraging classes like `CommandHandler`, `RedisParser`, and `Server` for separation of concerns and maintainability. Future iterations aim to incorporate advanced features such as RDB persistence, replication, and more Redis commands.

---

## Features  
- **Basic Redis Commands**  
  - `PING`: Test connectivity.  
  - `ECHO <message>`: Return the given message.  
  - `SET <key> <value> [EX seconds] [PX milliseconds] [NX|XX]`:  
    - Store a key-value pair with optional expiration time.  
    - Options:
      - `PX milliseconds`: Set the key to expire after a specified number of milliseconds.  
  - `GET <key>`: Retrieve the value for a given key.  
  - `CONFIG GET <pattern>`: Retrieve configuration parameters matching a pattern. 

- **Clean Architecture**  
  - Modular design with classes for command handling, parsing, and server management.  
  - Built with extensibility in mind for adding new features and commands.  

- **Threaded Server**  
  - Supports concurrent client connections using Python's `threading` module.  

---

## Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/AhmedShehab1/Redis_Clone.git
   python3 -m Redis_Clone.main
   ```
## Usage
**Interacting with the Redis Clone**
You can use any Redis client or telnet to interact with the server.

Example:

1. Start the server:

```bash
python3 -m Redis_Clone.main
```
2. Use telnet to connect to the server:

```bash
telnet localhost 6379
```
3. Issue commands:

PING

+PONG

ECHO Hello

"Hello"

SET mykey myvalue

+OK

GET mykey

"myvalue"

---

## Design Principles
+ **Object-Oriented Design (OOD):**
The code is structured into cohesive, reusable classes for ease of understanding and maintenance.

Key components include:

  + CommandHandler: Processes and executes incoming commands.
  + RedisParser: Parses client input into Redis command format.
  + Server: Manages client connections and command routing.
+ Threading:
Supports multiple clients by handling each connection in a separate thread.

--- 

## Planned Features
+ Persistence

  + Implement Redis Database (RDB) file-based persistence to save key-value data.

+ Advanced Commands

  + Support for additional commands like DEL, EXISTS, EXPIRE, etc.

+ Replication
  + Implement master-slave replication for high availability.
    
+ Custom Configuration
  + Extend CONFIG command for dynamic server tuning.
