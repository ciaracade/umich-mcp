# umich-mcp
〽️ MCP server for Univeristy of Michigan public APIs.

1. Clone this repository.
```
git clone https://github.com/ciaracade/umich-mcp.git
```

2. Create an `.env` file and input API key and secret.
```
UMICH_API_KEY = 
UMICH_API_SECRET = 
```

3. Follow this guide [here](https://modelcontextprotocol.io/quickstart/user) for Claude Desktop (recommended) or whichever client you are hosting the server on.

4. If using Claude Desktop configure MCP server in your `claude_desktop_config.json` like this:
```
{
  "mcpServers": {
    "umich": {
      "command": "python3",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/PARENT/FOLDER/umich-mcp/server.py",
      ]
    }
  }
}
```

5. Restart Claude Desktop.

6. If you are experiencing issues with your server, check out the official Claude Desktop Quickstart [here](https://modelcontextprotocol.io/quickstart/user) or [submit an issue](https://github.com/ciaracade/umich-mcp/issues).

## Contributing
Contributions are welcome. Due to the nature of the project, only University of Michigan faculty, staff, sponsored affiliates, and students can contribute to this repository. Contributing guide coming soon.

## Go Blue! 〽️
<a href="https://github.com/ciaracade/umich-mcp/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ciaracade/umich-mcp" />
</a>