# Files and Projects

A CWScript source file (`.cws`) can contain any number of contract / interface definitions, import directives, pragma directives, and function and type definitions.

Although not required, it is recommended that each smart contract be defined inside its own `.cws` file, which can be imported where needed by other smart contracts.

## Multi-contract Projects

Typically, CosmWasm dApps are structured as separate contracts that implement a parts of a protocol, which are deployed as separate contracts and connected by holding references to each other. Sometimes, a directory contract is deployed alongside the functional components, which keeps the contract addresses and logic for routing a function to the proper contract.

As this is the most conventional way to structure large projects, CWScript provides support for working with multi-contract projects.

### CWScript.toml

```toml
[project]
contracts = [
    "contracts/foo-governance.cws",
    "contracts/foo-token.cws",
    "contracts/foo-oracle.cws",
]
```

## Contracts

## Interfaces
