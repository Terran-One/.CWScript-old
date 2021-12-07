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

{% for resp in model.query_responses %}
{% for  in query %}
    {{ query_fn.name }} {
        {% for arg in exec_fn.args %}
            {{arg.name}}: {{arg.type.generate_code(env)}},
        {% endfor %}
    },
{% endfor %}
{% endfor %}
#[derive(Serialize, Deserialize, Clone, Debug, PartialEq, JsonSchema)]
pub struct CountResponse {
    pub count: i32,
}
