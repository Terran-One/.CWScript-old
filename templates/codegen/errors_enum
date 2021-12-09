use cosmwasm_std::StdError;
use thiserror::Error;

#[derive(Error, Debug, PartialEq)]
pub enum ContractError {
    #[error("{0}")]
    Std(#[from] StdError),
    {%- for err in contract.errors -%}
    {{ err.name }} {
        {%- for member in err.members -%}
        {{ member.name }}: {{ member.type.typestr }},
        {%- endfor -%}
    },
    {%- endfor -%}
}
