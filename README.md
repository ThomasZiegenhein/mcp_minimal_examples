# Minimal MCP Examples
[![Open in GitHub Codespace](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=984317769&skip_quickstart=true)

Collection of minimal end-to-end examples without 3rd party software of the [Model Context Protocol (MCP)](https://modelcontextprotocol.io).
All examples run local, in codespace, and provide a Docker for the server and a client to interact with it.

---

## 📁 Repository Structure

.\
├── python \
│ ├── tools \
│ │ ├── server.py # MCP server exposing echo()\
│ │ ├── client.py # Async client example\
│ │ ├── Dockerfile # Docker image for the server\
│ │ └── init.py\
│ ├── requirements.txt # Python dependencies\
└── LICENSE # Apache-2.0 License\

---

## ⚡ Quick Start (Local Python)

### Prerequisites

- Python ≥ 3.10
- Install dependencies:

```bash
pip install -r python/requirements.txt
```

### Running the Server and Client
#### Start the server:

```bash
python  python/tools/server.py
```

#### Client/caller
In another terminal, run the client:

```bash
python python/tools/client.py
```

Expected output:

▶  List of tools, and Hello World echo

## 🐳 Quick Start (Docker)
#### Build and Run the Docker Container

Build the Docker image:
```bash
cd /python/tools/
docker build -t mcp_echo .
```
Run the container:
    
```bash
cd /python/tools/
docker compose up -d
```

The server will be accessible at http://localhost:8800/mcp.
## 🧪 Testing with curl or Postman

MCP's streamable-http transport uses Server-Sent Events (SSE). Ensure your
client sets the Accept: text/event-stream header.
Example with curl:

```bash
curl -N -H "Accept: text/event-stream" http://localhost:8800/mcp/tools/list
```

## 🛠️ Troubleshooting

| Issue                                                                 | Cause                                           | Solution                                                                 |
|------------------------------------------------------------------------|--------------------------------------------------|--------------------------------------------------------------------------|
| `curl: (56) Recv failure: Connection reset by peer`                   | Server is bound to `127.0.0.1` inside container  | Use `host="0.0.0.0"` and expose the port with `-p 8800:8800`             |
| `Not Acceptable: Client must accept text/event-stream`               | Missing `Accept: text/event-stream` header       | Add `-H "Accept: text/event-stream"` to your HTTP request headers        |
| `Bad Request: Missing session ID`                                    | Tool was called before the client opened a session | Use `async with ClientSession(...)` before tool invocation             |

## 📄 License

This project is licensed under the Apache 2.0 License. See the LICENSE file for details.
