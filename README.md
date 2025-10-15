# 🚀 Proxmox MCP Server (Node.js Edition)

A Node.js-based Model Context Protocol (MCP) server that runs as a web service, allowing you to interact with multiple Proxmox hypervisors via HTTP.

## ✨ Features

- 🌐 **Multi-Server Support**: Connect to and manage multiple Proxmox servers or clusters.
- 📡 **HTTP Server**: Runs as a standalone web server, accessible over your network.
- 🌊 **HTTP Streaming**: Long-running commands (like `executeVMCommand`) stream their output in real-time using Server-Sent Events (SSE).
- 🛠️ Built with Express.js for robust HTTP handling.
- 🔐 Secure token-based authentication with Proxmox.
- 🖥️ Comprehensive management of nodes, VMs, and storage.

## 📦 Installation

### Prerequisites
- Node.js 16+ and npm
- Git
- Access to a Proxmox server with API token credentials

### Quick Install

1.  **Clone the repository and install dependencies:**
    ```bash
    git clone https://github.com/gilby125/mcp-proxmox.git
    cd mcp-proxmox
    npm install
    ```

2.  **Configure your servers:**
    Copy the `.env.example` file to `.env` and fill in your server details.
    ```bash
    cp .env.example .env
    ```

## ⚙️ Configuration

The server is configured using a `.env` file in the root of the project.

### Example `.env` file
```
# Port for the MCP HTTP server
MCP_PORT=3000

# Proxmox Server 1 Configuration
PROXMOX_SERVER_1_NAME=pve-cluster-1
PROXMOX_SERVER_1_HOST=192.168.1.10
# ... (and so on for all servers)
```

-   `MCP_PORT`: The port on which the web server will listen.
-   `PROXMOX_SERVER_{N}_NAME`: A unique name to identify the server.
-   ... (and all other server variables).

## 🚀 Running the Server

Start the web server with:
```bash
node index.js
```
The server will start and listen on the port you defined in your `.env` file (e.g., `http://localhost:3000`).

## 📡 Interacting with the Server

You can interact with the server by sending JSON-RPC requests to the `/mcp` endpoint.

### Example: Listing Tools (using `curl`)
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}' \
  http://localhost:3000/mcp
```

### Example: Calling a Standard Tool
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "proxmox_get_nodes", "arguments": {"server": "pve-cluster-1"}}}' \
  http://localhost:3000/mcp
```

### Example: Calling a Streaming Tool (like `executeVMCommand`)
For streaming tools, the server will respond with a `text/event-stream`. You can use `curl` with the `-N` (no-buffering) flag to see the events as they arrive.
```bash
curl -N -X POST -H "Content-Type: application/json" \
  -d '{"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "proxmox_execute_vm_command", "arguments": {"server": "pve-cluster-1", "node": "pve", "vmid": "100", "command": "sleep 5 && echo hello"}}}' \
  http://localhost:3000/mcp
```

You will see progress updates sent as Server-Sent Events.

# 🔧 Available Tools

All tools are called via the `/mcp` endpoint and require a `server` parameter. The `proxmox_execute_vm_command` tool is streamable.

... (tool descriptions remain the same) ...

## 📄 License

MIT License
