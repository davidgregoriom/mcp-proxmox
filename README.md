# 🚀 Proxmox MCP Server (Node.js Edition)

A Node.js-based Model Context Protocol (MCP) server for interacting with multiple Proxmox hypervisors, providing a clean interface for managing nodes, VMs, and containers.

## ✨ Features

- 🌐 **Multi-Server Support**: Connect to and manage multiple Proxmox servers or clusters from a single instance.
- 🛠️ Built with the official MCP SDK for Node.js.
- 🔐 Secure token-based authentication with Proxmox.
- 🖥️ Comprehensive node and VM management.
- 💻 VM console command execution (elevated mode).
- 📊 Real-time resource monitoring.
- 🎨 Rich markdown-formatted output.
- ⚡ Fast Node.js performance.

## 📦 Installation

### Prerequisites
- Node.js 16+ and npm
- Git
- Access to a Proxmox server with API token credentials

### Quick Install

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/gilby125/mcp-proxmox.git
    cd mcp-proxmox
    ```

2.  **Install dependencies:**
    ```bash
    npm install
    ```

3.  **Create your configuration file:**
    Copy the `.env.example` file to a new file named `.env` and fill in your server details.
    ```bash
    cp .env.example .env
    ```

## ⚙️ Configuration

The server is configured using a `.env` file in the root of the project. You can define multiple servers by numbering the environment variables.

### Example `.env` file
```
# Proxmox Server 1 Configuration
PROXMOX_SERVER_1_NAME=pve-cluster-1
PROXMOX_SERVER_1_HOST=192.168.1.10
PROXMOX_SERVER_1_PORT=806
PROXMOX_SERVER_1_USER=root@pam
PROXMOX_SERVER_1_TOKEN_NAME=mcp_token
PROXMOX_SERVER_1_TOKEN_VALUE=your-token-value-for-server-1
PROXMOX_SERVER_1_ALLOW_ELEVATED=true

# Proxmox Server 2 Configuration
PROXMOX_SERVER_2_NAME=pve-node-standalone
PROXMOX_SERVER_2_HOST=10.0.0.5
PROXMOX_SERVER_2_PORT=8006
PROXMOX_SERVER_2_USER=root@pam
PROXMOX_SERVER_2_TOKEN_NAME=mcp_token
PROXMOX_SERVER_2_TOKEN_VALUE=your-token-value-for-server-2
PROXMOX_SERVER_2_ALLOW_ELEVATED=false
```

### Configuration Details
-   `PROXMOX_SERVER_{N}_NAME`: A unique name to identify the server.
-   `PROXMOX_SERVER_{N}_HOST`: The IP address or hostname.
-   `PROXMOX_SERVER_{N}_PORT`: The API port (defaults to `8006`).
-   `PROXMOX_SERVER_{N}_USER`: The user, including the realm (e.g., `root@pam`).
-   `PROXMOX_SERVER_{N}_TOKEN_NAME`: The name of the API token.
-   `PROXMOX_SERVER_{N}_TOKEN_VALUE`: The secret value of the API token.
-   `PROXMOX_SERVER_{N}_ALLOW_ELEVATED`: Set to `true` to enable features requiring higher permissions.

### Permission Levels
-   **Basic Mode** (`ALLOW_ELEVATED=false`): For safe, read-only operations.
-   **Elevated Mode** (`ALLOW_ELEVATED=true`): Enables advanced operations like executing commands in a VM.

## 🚀 Running the Server

### Direct Execution
```bash
node index.js
```

### MCP Client Integration
For clients like Claude Code, add this to your MCP configuration:
```json
{
  "mcpServers": {
    "mcp-proxmox": {
      "command": "node",
      "args": ["index.js"],
      "cwd": "/absolute/path/to/mcp-proxmox"
    }
  }
}
```
**Note:** The server automatically loads the `.env` file from the project root.

# 🔧 Available Tools

All tools now require a `server` parameter to specify which Proxmox instance to target.

---

### `proxmox_get_nodes`
-   **Description**: Lists all nodes in a Proxmox cluster.
-   **Parameters**:
    -   `server` (string, required): The name of the server to target.

---

### `proxmox_get_node_status`
-   **Description**: Gets detailed status for a specific node.
-   **Parameters**:
    -   `server` (string, required): The name of the server to target.
    -   `node` (string, required): The name of the node.

---

### `proxmox_get_vms`
-   **Description**: Lists all VMs and containers on a server or a specific node.
-   **Parameters**:
    -   `server` (string, required): The name of the server to target.
    -   `node` (string, optional): Filter by a specific node.
    -   `type` (string, optional): Filter by type (`qemu`, `lxc`, or `all`).

---

### `proxmox_get_vm_status`
-   **Description**: Gets detailed status for a specific VM or container.
-   **Parameters**:
    -   `server` (string, required): The name of the server to target.
    -   `node` (string, required): The node where the VM is located.
    -   `vmid` (string, required): The ID of the VM or container.
    -   `type` (string, optional): The type (`qemu` or `lxc`).

---

### `proxmox_execute_vm_command`
-   **Description**: Executes a command in a VM or container (requires elevated permissions). This tool streams progress updates.
-   **Streaming Behavior**:
    -   For QEMU VMs, the tool sends progress messages while waiting for the command to finish, as the Proxmox API returns the full output only upon completion.
    -   For LXC containers, the output is returned directly in a single message.
-   **Parameters**:
    -   `server` (string, required): The name of the server to target.
    -   `node` (string, required): The node where the VM is located.
    -   `vmid` (string, required): The ID of the VM or container.
    -   `command` (string, required): The command to execute.
    -   `type` (string, optional): The type (`qemu` or `lxc`).

---

### `proxmox_get_storage`
-   **Description**: Lists storage pools on a server or a specific node.
-   **Parameters**:
    -   `server` (string, required): The name of the server to target.
    -   `node` (string, optional): Filter by a specific node.

---

### `proxmox_get_cluster_status`
-   **Description**: Gets the overall status of a Proxmox cluster.
-   **Parameters**:
    -   `server` (string, required): The name of the server to target.

## 📁 Project Structure

```
mcp-proxmox/
├── index.js                  # Main MCP server implementation
├── .env.example              # Example environment file
├── package.json              # Node.js dependencies and scripts
└── README.md                 # This documentation
```

## 📄 License

MIT License
