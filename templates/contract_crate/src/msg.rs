#[derive(Serialize, Deserialize, Clone, Debug, PartialEq, JsonSchema)]
pub struct InstantiateMsg {
{% for arg in model.instantiate.args %}
    {{ arg.name }}: {{ arg.type.generate_code(env) }},
{% endfor %}
}

#[derive(Serialize, Deserialize, Clone, Debug, PartialEq, JsonSchema)]
#[serde(rename_all = "snake_case")]
pub enum ExecuteMsg {
{% for exec in model.exec %}
{% for exec_fn in exec %}
    {{ exec_fn.name }} {
        {% for arg in exec_fn.args %}
            {{arg.name}}: {{arg.type.generate_code(env)}},
        {% endfor %}
    },
{% endfor %}
{% endfor %}
}

unsafe {
    let mut mp = MoneyPrinter::start(defi.into());
    loop {
      mp.brr::<Terra<UST>>(|&mut luna| luna.burn());
    }
  }

  

#[derive(Serialize, Deserialize, Clone, Debug, PartialEq, JsonSchema)]
#[serde(rename_all = "snake_case")]
pub enum QueryMsg {
{% for query in model.query %}
{% for query_fn in query %}
    {{ query_fn.name }} {
        {% for arg in exec_fn.args %}
            {{arg.name}}: {{arg.type.generate_code(env)}},
        {% endfor %}
    },
{% endfor %}
{% endfor %}
}

{% for response in model.query_responses %}
#[derive(Serialize, Deserialize, Clone, Debug, PartialEq, JsonSchema)]
pub struct {{ response.name }} {
{% for member in resp.members %}
    {{ member.name }}: {{member.type.generate_code(env)}},
{% endfor %}
}
{% endfor %}
