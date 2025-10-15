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

3.  **Create the configuration file:**
    Create a file named `config.json` inside a `proxmox-config` directory in the root of the project.

## ⚙️ Configuration

The server is configured using a JSON file located at `proxmox-config/config.json`.

### Example `config.json`
```json
{
  "servers": [
    {
      "name": "pve-cluster-1",
      "host": "192.168.1.10",
      "port": 8006,
      "user": "root@pam",
      "tokenName": "mcp_token",
      "tokenValue": "your-token-value-here",
      "allowElevated": true
    },
    {
      "name": "pve-node-standalone",
      "host": "10.0.0.5",
      "port": 8006,
      "user": "root@pam",
      "tokenName": "mcp_token",
      "tokenValue": "your-other-token-value-here",
      "allowElevated": false
    }
  ]
}
```

### Configuration Details
-   `servers` (array): A list of your Proxmox server configurations.
    -   `name` (string, required): A unique name to identify the server (e.g., "lab-cluster"). This name is used in every tool call.
    -   `host` (string, required): The IP address or hostname of the Proxmox server.
    -   `port` (number, optional): The API port, defaults to `8006`.
    -   `user` (string, required): The user, including the realm (e.g., `root@pam`).
    -   `tokenName` (string, required): The name of the API token.
    -   `tokenValue` (string, required): The secret value of the API token.
    -   `allowElevated` (boolean, optional): Set to `true` to enable features requiring higher permissions. Defaults to `false`.

### Permission Levels
-   **Basic Mode** (`allowElevated: false`): For safe, read-only operations like listing nodes and VMs.
-   **Elevated Mode** (`allowElevated: true`): Enables advanced, potentially destructive operations like executing commands in a VM. Requires an API token with more permissions (e.g., `Sys.Audit`, `VM.Monitor`, `VM.Console`).

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
**Note:** Replace `/absolute/path/to/mcp-proxmox` with the actual path to your installation.

# 🔧 Available Tools

All tools now require a `server` parameter to specify which Proxmox instance to target.

---

### `proxmox_get_nodes`
-   **Description**: Lists all nodes in a Proxmox cluster.
-   **Parameters**:
    -   `server` (string, required): The name of the server to target.

---

### `proxmox_get_node_status`
-   **Description**: Gets detailed status for a specific node (requires elevated permissions).
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
-   **Description**: Executes a command in a VM or container (requires elevated permissions).
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
├── proxmox-config/
│   └── config.json           # Server configurations
├── package.json              # Node.js dependencies and scripts
└── README.md                 # This documentation
```

## 📄 License

MIT License
