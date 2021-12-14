# Events

It is usually not sufficient to just call functions on a smart contract. We often want some way to record some relevant data about the operation calculated during execution and a way to easily parse and extract these details for further processing.

For instance, a contract that manages a basket of CW20 assets may want to record the sender and amount whenever some user deposits into it or withdraws from it, such that the evolution of the contract's balance can be retraced and studied easily. To do so, they could define an event inside their contract like:

```rust
event BalanceChanged(
    user: Addr, // user performing interaction
    asset: Addr, // asset involved
    before: Uint128, // amount before
    after: Uint128 // amount after
)
```

Then, inside the code of `exec` functions related to user deposits and withdrawals, they can simply issue a `log!` statement wherever the contract records a balance change in its state.

```rust
exec deposit_asset(asset: Addr, amount: Uint128) {
    before = $state.balance[asset]
    state.balance[asset] = before + amount
    log! BalanceChanged($msg.sender, asset, before, before + amount)
}
```
