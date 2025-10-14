"""
Proxmox API setup and management.

This module handles the core Proxmox API integration, providing:
- Secure API connection setup and management
- Token-based authentication
- Connection testing and validation
- Error handling for API operations

The ProxmoxManager class serves as the central point for all Proxmox API
interactions, ensuring consistent connection handling and authentication
across the MCP server.
"""
import logging
from typing import Dict, Any, List
from proxmoxer import ProxmoxAPI
from ..config.models import ProxmoxConfig, AuthConfig

class ProxmoxManager:
    """Manager class for Proxmox API operations.
    
    This class handles:
    - API connection initialization and management for multiple servers
    - Configuration validation and merging
    - Connection testing and health checks
    - Token-based authentication setup
    
    The manager provides a single point of access to the Proxmox API,
    ensuring proper initialization and error handling for all API operations.
    """
    
    def __init__(self, proxmox_configs: List[ProxmoxConfig], auth_config: AuthConfig):
        """Initialize the Proxmox API manager for multiple servers.

        Args:
            proxmox_configs: List of Proxmox connection configurations
            auth_config: Authentication configuration
        """
        self.logger = logging.getLogger("proxmox-mcp.proxmox")
        self.apis: Dict[str, ProxmoxAPI] = {}

        for proxmox_config in proxmox_configs:
            config = self._create_config(proxmox_config, auth_config)
            api = self._setup_api(config)
            self.apis[proxmox_config.name] = api

    def _create_config(self, proxmox_config: ProxmoxConfig, auth_config: AuthConfig) -> Dict[str, Any]:
        """Create a configuration dictionary for ProxmoxAPI.

        Merges connection and authentication configurations into a single
        dictionary suitable for ProxmoxAPI initialization. Handles:
        - Host and port configuration
        - SSL verification settings
        - Token-based authentication details
        - Service type specification

        Args:
            proxmox_config: Proxmox connection configuration (host, port, SSL settings)
            auth_config: Authentication configuration (user, token details)

        Returns:
            Dictionary containing merged configuration ready for API initialization
        """
        return {
            'host': proxmox_config.host,
            'port': proxmox_config.port,
            'user': auth_config.user,
            'token_name': auth_config.token_name,
            'token_value': auth_config.token_value,
            'verify_ssl': proxmox_config.verify_ssl,
            'service': proxmox_config.service
        }

    def _setup_api(self, config: Dict[str, Any]) -> ProxmoxAPI:
        """Initialize and test Proxmox API connection.

        Performs the following steps:
        1. Creates ProxmoxAPI instance with configured settings
        2. Tests connection by making a version check request
        3. Validates authentication and permissions
        4. Logs connection status and any issues

        Returns:
            Initialized and tested ProxmoxAPI instance

        Raises:
            RuntimeError: If connection fails due to:
                        - Invalid host/port
                        - Authentication failure
                        - Network connectivity issues
                        - SSL certificate validation errors
        """
        try:
            self.logger.info(f"Connecting to Proxmox host: {config['host']}")
            api = ProxmoxAPI(**config)
            
            # Test connection
            api.version.get()
            self.logger.info(f"Successfully connected to Proxmox API at {config['host']}")
            
            return api
        except Exception as e:
            self.logger.error(f"Failed to connect to Proxmox at {config['host']}: {e}")
            raise RuntimeError(f"Failed to connect to Proxmox at {config['host']}: {e}")

    def get_api(self, server_name: str) -> ProxmoxAPI:
        """Get the initialized Proxmox API instance for a specific server.
        
        Provides access to the configured and tested ProxmoxAPI instance
        for making API calls. The instance maintains connection state and
        handles authentication automatically.

        Args:
            server_name: The name of the server to get the API for.

        Returns:
            ProxmoxAPI instance ready for making API calls.

        Raises:
            KeyError: if the server_name is not found.
        """
        if server_name not in self.apis:
            raise KeyError(f"Server '{server_name}' not found in configured servers.")
        return self.apis[server_name]

    def get_all_apis(self) -> Dict[str, ProxmoxAPI]:
        """Get all initialized Proxmox API instances.

        Returns:
            A dictionary of ProxmoxAPI instances, keyed by server name.
        """
        return self.apis
