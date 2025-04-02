# config

```json
"simple-calc-docker": {
  "command": "docker",
  "args": [
	"run",
	"-i",
	"--rm",
	"-p",
	"3010:3000",
	"mcp/seminar"
  ]
},
"simple-calc": {
  "command": "uv",
  "args": [
	"--directory",
	"C:\\Users\\chjw1\\mcp\\MCP05",
	"run",
	"src\\calc_server.py"
  ]
}
```