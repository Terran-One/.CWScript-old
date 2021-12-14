# Contracts

A **contract** is declared using the `contract` keyword.

- name
- contract it extends (inherits definitions)
- interfaces implemented

```rust
contract MyToken extends CW20Base {
    // (...contract body)
}
```

## Structure

A contract can contain the following elements:

### Errors

```rust
contract ... {
    error Hello
}
```

### Events

```rust
contract ... {
    event SomethingHappened()
}
```

### Instantiate

```rust
contract ... {
    instantiate(a: Uint128, b: Uint128, c?: Uint128) {
        // body
    }
}
```

### Exec

### Query
