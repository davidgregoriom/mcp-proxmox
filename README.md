# 🚀 Proxmox MCP Server

A Model Context Protocol (MCP) server for interacting with multiple Proxmox hypervisors or clusters, providing a clean interface for managing nodes, VMs, and storage.

## ✨ Features

- 🌐 **Multi-Server Support**: Connect to and manage multiple Proxmox servers or clusters from a single instance.
- 🛠️ Built with the official MCP SDK for Python.
- 🔐 Secure token-based authentication with Proxmox.
- 🖥️ Comprehensive management of nodes, VMs, storage, and clusters.
- 💻 VM console command execution via QEMU Guest Agent.
- 🎨 Rich markdown-formatted output.

## 📦 Installation

### Prerequisites
- Python 3.8+
- Access to one or more Proxmox servers with API token credentials.

### Quick Install

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/gilby125/mcp-proxmox.git
    cd mcp-proxmox
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.in
    ```

3.  **Create a configuration file:**
    Create a file named `config.json` and place it in the root of the project or a known location.

4.  **Set the environment variable:**
    Create a `.env` file in the project root and add the following line, pointing to your configuration file:
    ```
    PROXMOX_MCP_CONFIG=/path/to/your/config.json
    ```
    For example: `PROXMOX_MCP_CONFIG=./config.json`

## ⚙️ Configuration

The server is configured using a single JSON file. Here is an example `config.json`:

```json
{
  "proxmox": [
    {
      "name": "pve-cluster-1",
      "host": "192.168.1.10",
      "port": 8006,
      "verify_ssl": true
    },
    {
      "name": "pve-node-standalone",
      "host": "10.0.0.5",
      "port": 8006,
      "verify_ssl": false
    }
  ],
  "auth": {
    "user": "root@pam",
    "token_name": "mcp_token",
    "token_value": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
  },
  "logging": {
    "level": "INFO"
  }
}
```

### Configuration Details

-   **`proxmox`** (list): A list of your Proxmox servers or clusters.
    -   `name` (string, required): A unique name to identify this server (e.g., "lab-cluster"). This name is used in every tool call.
    -   `host` (string, required): The IP address or hostname of the Proxmox server.
    -   `port` (integer, optional): The API port, defaults to `8006`.
    -   `verify_ssl` (boolean, optional): Set to `false` if using self-signed SSL certificates. Defaults to `true`.
-   **`auth`** (object): Your Proxmox API credentials.
    -   `user` (string, required): The user, including the realm (e.g., `root@pam`).
    -   `token_name` (string, required): The name of the API token.
    -   `token_value` (string, required): The secret value of the API token.
-   **`logging`** (object): Logging configuration.
    -   `level` (string, optional): The log level (e.g., "INFO", "DEBUG"). Defaults to "INFO".

### Proxmox API Token Setup
1.  Log into your Proxmox web interface.
2.  Navigate to **Datacenter** → **Permissions** → **API Tokens**.
3.  Click **Add** and create a token for a user with sufficient permissions.
4.  **Important**: Securely copy the **Token ID** (`token_name`) and the **Secret** (`token_value`). The secret is only shown once.

## 🚀 Running the Server

You can run the server directly for testing or integrate it with an MCP client.

### Direct Execution
```bash
python -m src.proxmox_mcp.server
```

### MCP Client Integration
For clients like Claude Code, add the following to your MCP configuration:
```json
{
  "mcpServers": {
    "proxmox-manager": {
      "command": "python",
      "args": ["-m", "src.proxmox_mcp.server"],
      "cwd": "/absolute/path/to/mcp-proxmox"
    }
  }
}
```
**Note:** Remember to replace `/absolute/path/to/mcp-proxmox` with the actual path to the project directory.

## 🔧 Available Tools

All tools require a `server` parameter to specify which Proxmox instance to target.

---

### `get_nodes`
Lists all nodes in a specified Proxmox cluster.
-   **Parameters**:
    -   `server` (string, required): The name of the server/cluster to target.

---

### `get_node_status`
Gets detailed status for a specific node.
-   **Parameters**:
    -   `server` (string, required): The name of the server/cluster to target.
    -   `node` (string, required): The name of the node to query.

---

### `get_vms`
Lists all virtual machines in a specified cluster.
-   **Parameters**:
    -   `server` (string, required): The name of the server/cluster to target.

---

### `execute_vm_command`
Executes a command inside a VM using the QEMU Guest Agent.
-   **Parameters**:
    -   `server` (string, required): The name of the server/cluster to target.
    -   `node` (string, required): The node where the VM is located.
    -   `vmid` (string, required): The ID of the VM.
    -   `command` (string, required): The command to execute.

---

### `get_storage`
Lists all storage pools in a specified cluster.
-   **Parameters**:
    -   `server` (string, required): The name of the server/cluster to target.

---

### `get_cluster_status`
Gets the overall health and status of a specified Proxmox cluster.
-   **Parameters**:
    -   `server` (string, required): The name of the server/cluster to target.

## 📁 Project Structure

```
mcp-proxmox/
├── src/
│   └── proxmox_mcp/
│       ├── __init__.py
│       ├── server.py         # Main MCP server implementation
│       ├── config/           # Configuration models and loader
│       ├── core/             # Core logic (Proxmox manager)
│       └── tools/            # Tool implementations
├── tests/                    # Test suite
├── config.json.example       # Example configuration
├── requirements.in           # Project dependencies
├── .env.example              # Example environment file
└── README.md                 # This documentation
```

## 📄 License

MIT License
