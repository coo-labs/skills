# Setup

Install the skills and agents into a Claude Code project (or your
user-global `~/.claude/` directory).

## cloud-setup.sh

```sh
# Install into a specific project
./setup/cloud-setup.sh /path/to/your-project

# Install into ~/.claude (user-global)
./setup/cloud-setup.sh --user
```

The script symlinks (or copies, with `--copy`) the contents of
`skills/` into `<target>/.claude/skills/` and `agents/` into
`<target>/.claude/agents/`.

By default it skips `agents/reference/` (those carry VADE-internal
memo references and are meant to be forked, not installed
verbatim). Pass `--include-reference` to install them anyway.

## mcp.json.template

The template encodes one pattern: **secrets resolve through
1Password CLI with environment-variable fallback.**

References take the form `op://Vault/Item/field` and resolve via
the [1Password CLI](https://developer.1password.com/docs/cli/) when
the Claude Code session is run inside an `op run -- claude` wrapper
(or equivalent). When 1Password is not available, the same fields
can be filled in with plain environment-variable values.

The shape:

```json
{
  "mcpServers": {
    "<server-name>": {
      "command": "<binary>",
      "args": ["..."],
      "env": {
        "SECRET_ENV_VAR": "op://Personal/<item>/<field>"
      }
    }
  }
}
```

The included servers are `mem0`, `github`, and `agentmail`. Remove
any you don't need and add any your project does. The template is
not consumed automatically — copy it to `.mcp.json` in your project
root, then edit.

## Why secrets through 1Password

A single-vault, single-service-account pattern keeps the exposure
surface small and auditable. The same `.mcp.json` works across
machines as long as the operator has `op` access to the vault; CI
pipelines substitute env-var values instead.

This is one expression of the pattern; an in-app secrets surface is
on the longer-term roadmap.
