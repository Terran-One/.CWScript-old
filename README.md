# CWScript

CWScript is a scripting language for writing smart contracts that run on blockchains such as Terra that use the CosmWasm as an execution layer.

## Features

- familiar syntax: can be learned and used easily without prior knowledge of Rust
- built-in language constructs for contract semantics
- compiles into conventional CosmWasm Rust following best practices
- provides a common framework for communicating contracts with non-developers
- bundled with helpful tooling & generators, and easily extensible
- provides a better framework for composability and code-reusability

## Examples

### Kitchen Sink Tutorial

```rust
// line-comments with double slash
// contract definition block
contract CW20 {
	// declare a single error
	error ImproperFormat(user: Addr, input: String)

	// define multiple error definitions using an 'errors' block
	errors {
		// you can now omit the prefixing 'error' keyword
		#[annotations]
		NotEnabled(req_level: enum Levels { #[item] Admin, Student }),
		Unauthorized, // both args () and body {} can be omitted if not needed
		InsufficientFunds(balance: Uint128, needed: Uint128)
	}

	// declare a single event type
	event Action(method: String, owner: String, count: String)

	// like errors, you can define multiple event types in an 'events' block
	events {
		// events don't have {} bodies like errors
		// however I'm planning to support it in the future
		Increment(),
		Reset(method: String)
	}

	// you can define state either as a series of state... statements
	// or grouped into a 'state' block.
	state curr_num: i32 // simple singleton (item mode)
	state balances[Addr]: Uint128 // you can also define maps

	// you are most likely going to use the 'state' block
	// as contracts usually need to declare a lot of state and it can get repetitive
	state {
		config: struct ConfigData { // another singleton, with in-place defn
			owner: Addr,
			count: i32,
			fee_percent: Decimal
		},

		// you can easily make storage with complex deep maps
		// the labels for map keys are mainly for annotation purposes
		// they are optional (see middle)
		token_balances[user: Addr][Addr][bucket: u32]: Uint128
	}

	// the 'instantiate' logic is here
	instantiate(count: i32, fee_percent: Dec) {
		$state.config = ConfigData {
			owner: $env.sender,
			count: count,
			fee_percent: fee_percent,
		}
		emit! Action("instantiate", $env.sender, count)
	}

	// you define the ExecuteMsg handlers as such:
	exec msg_name_snake_case(arg1: u32, arg2: Option<String>) {
		// you don't need to return anything or write anything here
	}

	exec { // you could also do it like this
		increment() {
			$state.config.count += 1
			if (( $state.config.count )) < 2 {
				Intensity {
					item: 23,
					power23: 722391,
					my_power: ally("call", 12)
				}
			}
		}

		reset(count: i32) {
			if $env.sender != $state.config.owner {
				fail! Unauthorized
			}
			$state.config.count = count
		}
	}

	// we can use inline type declarations to make it more convenient
	query count() -> struct CountResponse { count: i32 } {
		CountResponse { count: $state.config.count }
	}

	query item() -> struct ItemResponse { item: ([int????], &&[Fire::boy], struct Unit, struct Tiger { item: u32? }) }

	// however, we can use another pattern...
	query user_balance_for_token(user: Addr, token: Addr) responds {
		#[echo("hello")] user: Addr = user,
		#[derive(Sata, ansdf)] token: Addr = token,
		balance: Uint128 = $state.token_balances[user][token][1],
	}

	// this is equivalent to:
	query user_balance_for_token(user: Addr, token: Addr) -> struct UserBalanceForTokenResponse { balance: Uint128 } {
		UserBalanceForTokenResponse { balance: $state.token_balances[user][token][1] }
	}

	// such is the power of the contextual type declaration and assignment
}
```

### Translation of CW20-Base (CosmWasm Plus)

#### cw20.cws

```rust
interface CW20 {

    struct TokenInfo {
        name: String,
        symbol: String,
        decimals: u8,
        total_supply: Uint128,
        mint?: MinterData
    }

    exec {
        transfer(recipient: Addr, amount: Uint128)
        send(contract: Addr, amount: Addr, msg: Msg)
        increase_allowance(spender: Addr, amount: Uint128, expires?: Expiration)
        decrease_allowance(spender: Addr, amount: Uint128, expires?: Expiration)
        transfer_from(owner: Addr, recipient: Addr, amount: Uint128)
        send_from(owner: Addr, contract: Addr, amount: Uint128, msg: Binary)
        burn_from(owner: Addr, amount: Uint128)
        mint(recipient: String, amount: Uint128)
    }

    query {
        balance(address: Addr) responds {
            balance: Uint128
        }
        token_info() responds {
            name: String,
            symbol: String,
            decimals: u8,
            total_supply: Uint128
        }
        allowance(owner: String, spender: String) responds {
            allowance: Uint128,
            expires: Expiration
        }
        minter() repsponds (minter: Addr, cap?: Uint128)
        marketing_info() responds {
            project?: String,
            description?: String,
            logo?: LogoInfo,
            marketing?: Addr
        }
        download_logo(mime_type: String, data: Binary)
        all_allowances(
            owner: Addr,
            start_after?: Addr,
            limit?: u32
        ) responds {
            allowances: AllowanceInfo[]
        }
        all_accounts(owner: Addr, start_after?: Addr, limit?: u32) responds {
            accounts: Addr[]
        }
    }
}
```

#### cw20base.cws

```rust
import CW20 from "cw20.cws"

contract CW20Base implements CW20 {

    state token_info: @CW20::structs::TokenInfo
    state balances[user: Addr]: Uint128

    instantiate(
        name: String,
        symbol: String,
        decimals: u8,
        initial_balances: [struct Cw20Coin { address: Addr, amount: Uint128 }],
        mint?: @CW20::query::mint::response
    ) {
        total_supply = Uint128(0)
        for { address, amount } in initial_balances {
            $state.balances[address]
            total_supply += amount
        }

        $state.token_info = TokenInfo {
            name: name,
            symbol: symbol,
            decimals: decimals,
            total_supply: total_supply,
        }
    }

    check not0: $arg == 0 -> InvalidZeroAmount

    check not0 {
        if $arg == 0 {
            fail! InvalidZeroAmount
        }
    }

    // translates into:
    // if ($arg == 0) {
    //   fail! InvalidZeroAmount
    // }

    check valid for Addr: $api.addr_validate($arg)

    exec transfer(recipient: Addr, amount: Uint128#not0) {
        $state.balances[$msg.sender] -= amount
        $state.balances[recipient] += amount
        emit! Transfer($msg.sender, recipient, amount)
    }

    exec burn(amount: Uint128#not0) {
        $state.balances[$info.sender] -= amount
        $state.token_supply -= amount
        emit! Burn($info.sender, amount)
    }

    exec mint(recipient: Addr#valid, amount: Uint128#not0) {
        config = $state.token_info
        if (config.mint == None) or (config.mint.minter != $msg.sender) {
            fail! Unauthorized
        }

        config.total_supply += amount
        if? (limit = config.get_cap()) and config.total_supply > limit {
            fail! CannotExceedCap
        }

        $state.token_info = config
        $state.balances[recipient] += amount
        emit! Mint(recipient, amount)
    }

    exec send(contract: Addr#valid, amount: Uint128#non0, msg: Binary) {
        $state.balances[$msg.sender] -= amount
        $state.balances[contract] += amount
        emit! Send($msg.sender, contract, amount)
        exec! (CW @ CW20Receiver).receive(sender: $msg.sender, amount, msg)
    }

    query balance(address: Addr#valid) responds {
        balance: Uint128 = $state.balances[address] or 0
    }

    query token_info() responds {
        token_info: TokenInfo = $state.token_info
    }

    query minter() -> @CW20::query::minter::response? {
        meta = $state.token_info
        if? meta.minter {
            return minter
        } else {
            return None
        }
    }

}

contract MyToken(CW20Base) implements CW20, CW721 {

}
```
