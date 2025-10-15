# 🚀 Proxmox MCP Server (Node.js Edition)

A Node.js-based Model Context Protocol (MCP) server that runs as a web service, allowing you to interact with multiple Proxmox hypervisors via HTTP.

## ✨ Features

- 🌐 **Multi-Server Support**: Connect to and manage multiple Proxmox servers or clusters.
- 📡 **HTTP Server**: Runs as a standalone web server using the official MCP SDK's `StreamableHTTPServerTransport`.
- 🌊 **HTTP Streaming**: Long-running commands (like `executeVMCommand`) stream their output in real-time.
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
-   `PROXMOX_SERVER_{N}_...`: All other server-specific variables.

## 🚀 Running the Server

Start the web server with:
```bash
node index.js
```
The server will start and listen on the port you defined in your `.env` file (e.g., `http://localhost:3000`). The SDK automatically handles the `/api/proxmox` endpoint.

## 📡 Interacting with the Server

You can interact with the server by sending JSON-RPC requests to the `/api/proxmox` endpoint.

### Example: Listing Tools (using `curl`)
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}' \
  http://localhost:3000/api/proxmox
```

### Example: Calling a Streaming Tool
For streaming tools, the SDK's transport handles the `text/event-stream` response automatically.
```bash
curl -N -X POST -H "Content-Type: application/json" \
  -d '{"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "proxmox_execute_vm_command", "arguments": {"server": "pve-cluster-1", "node": "pve", "vmid": "100", "command": "sleep 5 && echo hello"}}}' \
  http://localhost:3000/api/proxmox
```

# 🔧 Available Tools

All tools are called via the `/api/proxmox` endpoint. The `proxmox_execute_vm_command` tool is streamable.

... (tool descriptions remain the same) ...

## 📄 License

MIT License
