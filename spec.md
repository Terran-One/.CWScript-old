# CWScript Language Specification

## Comments

Line comments begin with double slash `//`. Where used, all text in the same line appearing
after will be ignored by the compiler.

```cws

```

There are no block-style comments such as those you can find in C: `/* comment */`

## Entrypoints

An **entrypoint** is a call site on a smart contract where execution of contract code can
be triggered. In CWScript, entrypoints are functions defined inside the body of a contract
which are marked as one of `instantiate`, `exec`, `query`, or `migrate` -- the distinct
contexts in which contract code can execute.

- `instantiate` - code run just after a new contract is created
- `exec` - analagous to a "contract call" on Ethereum that modifies state
- `query` - analagous to a pure + readonly contract call on Ethereum
- `migrate` - called when contract code is migrated over (contract address will point to a different code ID)

## Instantiate Handler (constructor)

The Instantiate Handler is a functioned trigged promptly after a new instance of your contract
has been created (assigned an address and transffered any coins sent in the MsgInstantiateMsg).
You have access to the new instance's contract address.

```cws
contract ... {
    instantiate(
        owner: Addr,

    )
}
```

A contract can only have 1 instantiate handler --

## Exec Handler (function)

A contract can contain any number of Exec Handlers.

During compilation, the interfaces of all exec handlers found inside a contract are collected
and bundled together as different variants of `enum ExecuteMsg`, named as the PascalCase version
of the original exec handler's name, which conventionally should be snake_case.

## Query Handler (function)

A contract can contain any number of Query Handlers.

Similar to how Exec Handlers are processed, Query Handlers will be parsed to derive an `enum QueryMsg`
with variants corresponding to the name and argument interface of the original query handler.

Query Handlers differ from Exec Handlers in 2 main ways. Firstly, they are unable to modify
the state of the blockchain; both writing to contract's local store and calling exec handlers
on other functions are inaccessible within a `query` call context. Second, Query Handlers are
expected to return data back to the caller. In CWScript, the data returned by a Query Handler
is referred to as its "response."

A Query Handler must define the type of the response. Conventionally, query responses are
represented as a `struct` (but in rare cases, an `enum`), named as XXXResponse, where XXX
is the PascalCase version of the original handler's name.

```cws
contract ... {
    query my_query_name(arg1: Addr, arg2?: Uint128) = {
    }
}
```

## Checks

And now for a unique feature to CWScript: Checks.

A _check_ is are validation functions that are only used when defining a function's arguments.
After specifying the argument's permitted type, you have the option of additionally adding
any number of checks by prefixing a check function's name with the # symbol.

Prior to the start of a function's execution, checks for each argument will be called sequentially
in the order in which they appear in the argument's definition. For example:

#### Example: Check call order

```
check A
check B
check C

fn test(arg1: T #A #B, arg2: T #C #A, arg3: T #A #B #C)

A(arg1)
B(arg1)
C(arg2)
A(arg2)
A(arg3)
B(arg3)
C(arg4)
```

```cws
contract ... {
    exec try_something(balance: Uint128 #notzero)
}
```

Checks are actually macro-expressions, as the compiler collects
the checks for each of the function's arguments and copies the directly inserts the
expanded macro before.

Checks
