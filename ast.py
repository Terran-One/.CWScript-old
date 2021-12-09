FileCode(
    body=[
        DeclContract(
            defn=ContractDefn(
                name=Ident(symbol=Token("__ANON_16", "CW20")),
                body=[
                    DeclError(
                        defns=[
                            ErrorDefn(
                                name=Ident(symbol=Token("__ANON_16", "ImproperFormat")),
                                members=[
                                    TypeAssign(
                                        name=Ident(symbol=Token("__ANON_15", "user")),
                                        type=Typename(
                                            name=Ident(
                                                symbol=Token("__ANON_15", "Addr")
                                            )
                                        ),
                                    ),
                                    TypeAssign(
                                        name=Ident(symbol=Token("__ANON_15", "input")),
                                        type=Typename(
                                            name=Ident(
                                                symbol=Token("__ANON_15", "String")
                                            )
                                        ),
                                    ),
                                ],
                                body=[
                                    IfExpr(
                                        if_clause=IfClause(
                                            predicate=InfixOpExpr(
                                                lhs=Ident(
                                                    symbol=Token("__ANON_15", "input")
                                                ),
                                                op=Token("__ANON_11", "!="),
                                                rhs=Ident(
                                                    symbol=Token("__ANON_15", "None")
                                                ),
                                            ),
                                            body=[
                                                String(
                                                    value=Token(
                                                        "ESCAPED_STRING",
                                                        '"wrong format for user, got {input}"',
                                                    )
                                                )
                                            ],
                                        ),
                                        else_if_clauses=None,
                                        else_body=[
                                            String(
                                                value=Token(
                                                    "ESCAPED_STRING",
                                                    '"wrong format for user"',
                                                )
                                            )
                                        ],
                                    )
                                ],
                            )
                        ]
                    ),
                    DeclError(
                        defns=[
                            ErrorDefn(
                                name=Ident(symbol=Token("__ANON_16", "NotEnabled")),
                                members=[
                                    TypeAssign(
                                        name=Ident(
                                            symbol=Token("__ANON_15", "req_level")
                                        ),
                                        type=EnumDefn(
                                            name=Ident(
                                                symbol=Token("__ANON_16", "Levels")
                                            ),
                                            variants=[
                                                EnumVariantUnit(
                                                    name=Ident(
                                                        symbol=Token(
                                                            "__ANON_16", "Admin"
                                                        )
                                                    )
                                                ),
                                                EnumVariantUnit(
                                                    name=Ident(
                                                        symbol=Token(
                                                            "__ANON_16", "Student"
                                                        )
                                                    )
                                                ),
                                            ],
                                        ),
                                    )
                                ],
                                body=[
                                    IfExpr(
                                        if_clause=IfClause(
                                            predicate=InfixOpExpr(
                                                lhs=Ident(
                                                    symbol=Token(
                                                        "__ANON_15", "req_level"
                                                    )
                                                ),
                                                op=Token("__ANON_10", "=="),
                                                rhs=InfixOpExpr(
                                                    lhs=Ident(
                                                        symbol=Token(
                                                            "__ANON_15", "Levels"
                                                        )
                                                    ),
                                                    op=Token("__ANON_14", "::"),
                                                    rhs=Ident(
                                                        symbol=Token(
                                                            "__ANON_15", "Admin"
                                                        )
                                                    ),
                                                ),
                                            ),
                                            body=[
                                                String(
                                                    value=Token(
                                                        "ESCAPED_STRING",
                                                        '"you must be an admin to access this portion"',
                                                    )
                                                )
                                            ],
                                        ),
                                        else_if_clauses=None,
                                        else_body=[
                                            String(
                                                value=Token(
                                                    "ESCAPED_STRING",
                                                    '"the required level is student, unfortunately"',
                                                )
                                            )
                                        ],
                                    )
                                ],
                            ),
                            ErrorDefn(
                                name=Ident(symbol=Token("__ANON_16", "Unauthorized")),
                                members=[],
                                body=[],
                            ),
                            ErrorDefn(
                                name=Ident(
                                    symbol=Token("__ANON_16", "InsufficientFunds")
                                ),
                                members=[
                                    TypeAssign(
                                        name=Ident(
                                            symbol=Token("__ANON_15", "balance")
                                        ),
                                        type=Typename(
                                            name=Ident(
                                                symbol=Token("__ANON_15", "Uint128")
                                            )
                                        ),
                                    ),
                                    TypeAssign(
                                        name=Ident(symbol=Token("__ANON_15", "needed")),
                                        type=Typename(
                                            name=Ident(
                                                symbol=Token("__ANON_15", "Uint128")
                                            )
                                        ),
                                    ),
                                ],
                                body=[
                                    String(
                                        value=Token(
                                            "ESCAPED_STRING",
                                            '"you only had {balance}, which is less than the {needed} required"',
                                        )
                                    )
                                ],
                            ),
                        ]
                    ),
                    DeclEvent(
                        defns=[
                            EventDefn(
                                name=Ident(symbol=Token("__ANON_16", "Action")),
                                members=[
                                    TypeAssign(
                                        name=Ident(symbol=Token("__ANON_15", "method")),
                                        type=Typename(
                                            name=Ident(
                                                symbol=Token("__ANON_15", "String")
                                            )
                                        ),
                                    ),
                                    TypeAssign(
                                        name=Ident(symbol=Token("__ANON_15", "owner")),
                                        type=Typename(
                                            name=Ident(
                                                symbol=Token("__ANON_15", "String")
                                            )
                                        ),
                                    ),
                                    TypeAssign(
                                        name=Ident(symbol=Token("__ANON_15", "count")),
                                        type=Typename(
                                            name=Ident(
                                                symbol=Token("__ANON_15", "String")
                                            )
                                        ),
                                    ),
                                ],
                                body=[],
                            )
                        ]
                    ),
                    DeclEvent(
                        defns=[
                            EventDefn(
                                name=Ident(symbol=Token("__ANON_16", "Increment")),
                                members=[],
                                body=[],
                            ),
                            EventDefn(
                                name=Ident(symbol=Token("__ANON_16", "Reset")),
                                members=[
                                    TypeAssign(
                                        name=Ident(symbol=Token("__ANON_15", "method")),
                                        type=Typename(
                                            name=Ident(
                                                symbol=Token("__ANON_15", "String")
                                            )
                                        ),
                                    )
                                ],
                                body=[],
                            ),
                        ]
                    ),
                    DeclState(
                        defns=[
                            ItemDefn(
                                key=Ident(symbol=Token("__ANON_15", "curr_num")),
                                type_expr=Typename(
                                    name=Ident(symbol=Token("__ANON_15", "i32"))
                                ),
                            )
                        ]
                    ),
                    DeclState(
                        defns=[
                            MapDefn(
                                prefix=Ident(symbol=Token("__ANON_15", "balances")),
                                type_keys=[
                                    MapKeyDefn(
                                        key=None,
                                        type=Typename(
                                            name=Ident(
                                                symbol=Token("__ANON_15", "Addr")
                                            )
                                        ),
                                    )
                                ],
                                type_value=Typename(
                                    name=Ident(symbol=Token("__ANON_15", "Uint128"))
                                ),
                            )
                        ]
                    ),
                    DeclState(
                        defns=[
                            ItemDefn(
                                key=Ident(symbol=Token("__ANON_15", "config")),
                                type_expr=StructDictDefn(
                                    name=Ident(symbol=Token("__ANON_16", "ConfigData")),
                                    members=[
                                        TypeAssign(
                                            name=Ident(
                                                symbol=Token("__ANON_15", "owner")
                                            ),
                                            type=Typename(
                                                name=Ident(
                                                    symbol=Token("__ANON_15", "Addr")
                                                )
                                            ),
                                        ),
                                        TypeAssign(
                                            name=Ident(
                                                symbol=Token("__ANON_15", "count")
                                            ),
                                            type=Typename(
                                                name=Ident(
                                                    symbol=Token("__ANON_15", "i32")
                                                )
                                            ),
                                        ),
                                        TypeAssign(
                                            name=Ident(
                                                symbol=Token("__ANON_15", "fee_percent")
                                            ),
                                            type=Typename(
                                                name=Ident(
                                                    symbol=Token("__ANON_15", "Decimal")
                                                )
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            MapDefn(
                                prefix=Ident(
                                    symbol=Token("__ANON_15", "token_balances")
                                ),
                                type_keys=[
                                    MapKeyDefn(
                                        key=Ident(symbol=Token("__ANON_15", "user")),
                                        type=Typename(
                                            name=Ident(
                                                symbol=Token("__ANON_15", "Addr")
                                            )
                                        ),
                                    ),
                                    MapKeyDefn(
                                        key=None,
                                        type=Typename(
                                            name=Ident(
                                                symbol=Token("__ANON_15", "Addr")
                                            )
                                        ),
                                    ),
                                    MapKeyDefn(
                                        key=Ident(symbol=Token("__ANON_15", "bucket")),
                                        type=Typename(
                                            name=Ident(symbol=Token("__ANON_15", "u32"))
                                        ),
                                    ),
                                ],
                                type_value=Typename(
                                    name=Ident(symbol=Token("__ANON_15", "Uint128"))
                                ),
                            ),
                        ]
                    ),
                    DeclInstantiate(
                        defn=InstantiateDefn(
                            args=[
                                TypeAssign(
                                    name=Ident(symbol=Token("__ANON_15", "count")),
                                    type=Typename(
                                        name=Ident(symbol=Token("__ANON_15", "i32"))
                                    ),
                                ),
                                TypeAssign(
                                    name=Ident(
                                        symbol=Token("__ANON_15", "fee_percent")
                                    ),
                                    type=Typename(
                                        name=Ident(symbol=Token("__ANON_15", "Dec"))
                                    ),
                                ),
                            ],
                            body=[
                                AssignStmt(
                                    lhs=IdentPath(
                                        parts=[
                                            Ident(symbol=Token("__ANON_15", "$state")),
                                            Ident(symbol=Token("__ANON_15", "config")),
                                        ]
                                    ),
                                    assign_op="=",
                                    rhs=StructDictVal(
                                        name=Ident(
                                            symbol=Token("__ANON_16", "ConfigData")
                                        ),
                                        members_vals=[
                                            StructDictAssign(
                                                name=Ident(
                                                    symbol=Token("__ANON_15", "owner")
                                                ),
                                                value=MemberAccessExpr(
                                                    item=Ident(
                                                        symbol=Token(
                                                            "__ANON_15", "$env"
                                                        )
                                                    ),
                                                    member=Ident(
                                                        symbol=Token(
                                                            "__ANON_15", "sender"
                                                        )
                                                    ),
                                                ),
                                            ),
                                            StructDictAssign(
                                                name=Ident(
                                                    symbol=Token("__ANON_15", "count")
                                                ),
                                                value=Ident(
                                                    symbol=Token("__ANON_15", "count")
                                                ),
                                            ),
                                            StructDictAssign(
                                                name=Ident(
                                                    symbol=Token(
                                                        "__ANON_15", "fee_percent"
                                                    )
                                                ),
                                                value=Ident(
                                                    symbol=Token(
                                                        "__ANON_15", "fee_percent"
                                                    )
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                EmitStmt(
                                    expr=FnCallExpr(
                                        fn_name=Ident(
                                            symbol=Token("__ANON_15", "Action")
                                        ),
                                        args=[
                                            String(
                                                value=Token(
                                                    "ESCAPED_STRING", '"instantiate"'
                                                )
                                            ),
                                            MemberAccessExpr(
                                                item=Ident(
                                                    symbol=Token("__ANON_15", "$env")
                                                ),
                                                member=Ident(
                                                    symbol=Token("__ANON_15", "sender")
                                                ),
                                            ),
                                            Ident(symbol=Token("__ANON_15", "count")),
                                        ],
                                    )
                                ),
                            ],
                        )
                    ),
                    DeclExec(
                        defns=[
                            ExecDefn(
                                name=Ident(
                                    symbol=Token("__ANON_15", "msg_name_snake_case")
                                ),
                                args=[
                                    TypeAssign(
                                        name=Ident(symbol=Token("__ANON_15", "arg1")),
                                        type=Typename(
                                            name=Ident(symbol=Token("__ANON_15", "u32"))
                                        ),
                                    ),
                                    TypeAssign(
                                        name=Ident(symbol=Token("__ANON_15", "arg2")),
                                        type=ParamzdTypeExpr(
                                            base_type=Typename(
                                                name=Ident(
                                                    symbol=Token("__ANON_15", "Option")
                                                )
                                            ),
                                            param=Typename(
                                                name=Ident(
                                                    symbol=Token("__ANON_15", "String")
                                                )
                                            ),
                                        ),
                                    ),
                                ],
                                body=[],
                            )
                        ]
                    ),
                    DeclExec(
                        defns=[
                            ExecDefn(
                                name=Ident(symbol=Token("__ANON_15", "increment")),
                                args=[],
                                body=[
                                    AssignStmt(
                                        lhs=IdentPath(
                                            parts=[
                                                Ident(
                                                    symbol=Token("__ANON_15", "$state")
                                                ),
                                                Ident(
                                                    symbol=Token("__ANON_15", "config")
                                                ),
                                                Ident(
                                                    symbol=Token("__ANON_15", "count")
                                                ),
                                            ]
                                        ),
                                        assign_op="+=",
                                        rhs=Integer(value=Token("__ANON_19", "1")),
                                    )
                                ],
                            ),
                            ExecDefn(
                                name=Ident(symbol=Token("__ANON_15", "reset")),
                                args=[
                                    TypeAssign(
                                        name=Ident(symbol=Token("__ANON_15", "count")),
                                        type=Typename(
                                            name=Ident(symbol=Token("__ANON_15", "i32"))
                                        ),
                                    )
                                ],
                                body=[
                                    IfExpr(
                                        if_clause=IfClause(
                                            predicate=MemberAccessExpr(
                                                item=MemberAccessExpr(
                                                    item=InfixOpExpr(
                                                        lhs=MemberAccessExpr(
                                                            item=Ident(
                                                                symbol=Token(
                                                                    "__ANON_15", "$env"
                                                                )
                                                            ),
                                                            member=Ident(
                                                                symbol=Token(
                                                                    "__ANON_15",
                                                                    "sender",
                                                                )
                                                            ),
                                                        ),
                                                        op=Token("__ANON_11", "!="),
                                                        rhs=Ident(
                                                            symbol=Token(
                                                                "__ANON_15", "$state"
                                                            )
                                                        ),
                                                    ),
                                                    member=Ident(
                                                        symbol=Token(
                                                            "__ANON_15", "config"
                                                        )
                                                    ),
                                                ),
                                                member=Ident(
                                                    symbol=Token("__ANON_15", "owner")
                                                ),
                                            ),
                                            body=[
                                                FailStmt(
                                                    expr=Ident(
                                                        symbol=Token(
                                                            "__ANON_15", "Unauthorized"
                                                        )
                                                    )
                                                )
                                            ],
                                        ),
                                        else_if_clauses=None,
                                        else_body=None,
                                    ),
                                    AssignStmt(
                                        lhs=IdentPath(
                                            parts=[
                                                Ident(
                                                    symbol=Token("__ANON_15", "$state")
                                                ),
                                                Ident(
                                                    symbol=Token("__ANON_15", "config")
                                                ),
                                                Ident(
                                                    symbol=Token("__ANON_15", "count")
                                                ),
                                            ]
                                        ),
                                        assign_op="=",
                                        rhs=Ident(symbol=Token("__ANON_15", "count")),
                                    ),
                                ],
                            ),
                        ]
                    ),
                    DeclQuery(
                        defns=[
                            QueryDefnFn(
                                name=Ident(symbol=Token("__ANON_15", "count")),
                                args=[],
                                response_type=StructDictDefn(
                                    name=Ident(
                                        symbol=Token("__ANON_16", "CountResponse")
                                    ),
                                    members=[
                                        TypeAssign(
                                            name=Ident(
                                                symbol=Token("__ANON_15", "count")
                                            ),
                                            type=Typename(
                                                name=Ident(
                                                    symbol=Token("__ANON_15", "i32")
                                                )
                                            ),
                                        )
                                    ],
                                ),
                                body=[
                                    StructDictVal(
                                        name=Ident(
                                            symbol=Token("__ANON_16", "CountResponse")
                                        ),
                                        members_vals=StructDictAssign(
                                            name=Ident(
                                                symbol=Token("__ANON_15", "count")
                                            ),
                                            value=MemberAccessExpr(
                                                item=MemberAccessExpr(
                                                    item=Ident(
                                                        symbol=Token(
                                                            "__ANON_15", "$state"
                                                        )
                                                    ),
                                                    member=Ident(
                                                        symbol=Token(
                                                            "__ANON_15", "config"
                                                        )
                                                    ),
                                                ),
                                                member=Ident(
                                                    symbol=Token("__ANON_15", "count")
                                                ),
                                            ),
                                        ),
                                    )
                                ],
                            )
                        ]
                    ),
                    DeclQuery(
                        defns=[
                            QueryDefnResponds(
                                name=Ident(
                                    symbol=Token("__ANON_15", "user_balance_for_token")
                                ),
                                args=[
                                    TypeAssign(
                                        name=Ident(symbol=Token("__ANON_15", "user")),
                                        type=Typename(
                                            name=Ident(
                                                symbol=Token("__ANON_15", "Addr")
                                            )
                                        ),
                                    ),
                                    TypeAssign(
                                        name=Ident(symbol=Token("__ANON_15", "token")),
                                        type=Typename(
                                            name=Ident(
                                                symbol=Token("__ANON_15", "Addr")
                                            )
                                        ),
                                    ),
                                ],
                                response_defn=QueryResponseDefn(
                                    body=[
                                        TypeAssignAndSet(
                                            type_assign=TypeAssign(
                                                name=Ident(
                                                    symbol=Token("__ANON_15", "user")
                                                ),
                                                type=Typename(
                                                    name=Ident(
                                                        symbol=Token(
                                                            "__ANON_15", "Addr"
                                                        )
                                                    )
                                                ),
                                            ),
                                            value=Ident(
                                                symbol=Token("__ANON_15", "user")
                                            ),
                                        ),
                                        TypeAssignAndSet(
                                            type_assign=TypeAssign(
                                                name=Ident(
                                                    symbol=Token("__ANON_15", "token")
                                                ),
                                                type=Typename(
                                                    name=Ident(
                                                        symbol=Token(
                                                            "__ANON_15", "Addr"
                                                        )
                                                    )
                                                ),
                                            ),
                                            value=Ident(
                                                symbol=Token("__ANON_15", "token")
                                            ),
                                        ),
                                        TypeAssignAndSet(
                                            type_assign=TypeAssign(
                                                name=Ident(
                                                    symbol=Token("__ANON_15", "balance")
                                                ),
                                                type=Typename(
                                                    name=Ident(
                                                        symbol=Token(
                                                            "__ANON_15", "Uint128"
                                                        )
                                                    )
                                                ),
                                            ),
                                            value=TableLookupExpr(
                                                item=TableLookupExpr(
                                                    item=TableLookupExpr(
                                                        item=MemberAccessExpr(
                                                            item=Ident(
                                                                symbol=Token(
                                                                    "__ANON_15",
                                                                    "$state",
                                                                )
                                                            ),
                                                            member=Ident(
                                                                symbol=Token(
                                                                    "__ANON_15",
                                                                    "token_balances",
                                                                )
                                                            ),
                                                        ),
                                                        key=Ident(
                                                            symbol=Token(
                                                                "__ANON_15", "user"
                                                            )
                                                        ),
                                                    ),
                                                    key=Ident(
                                                        symbol=Token(
                                                            "__ANON_15", "token"
                                                        )
                                                    ),
                                                ),
                                                key=Integer(
                                                    value=Token("__ANON_19", "1")
                                                ),
                                            ),
                                        ),
                                    ]
                                ),
                            )
                        ]
                    ),
                    DeclQuery(
                        defns=[
                            QueryDefnFn(
                                name=Ident(
                                    symbol=Token("__ANON_15", "user_balance_for_token")
                                ),
                                args=[
                                    TypeAssign(
                                        name=Ident(symbol=Token("__ANON_15", "user")),
                                        type=Typename(
                                            name=Ident(
                                                symbol=Token("__ANON_15", "Addr")
                                            )
                                        ),
                                    ),
                                    TypeAssign(
                                        name=Ident(symbol=Token("__ANON_15", "token")),
                                        type=Typename(
                                            name=Ident(
                                                symbol=Token("__ANON_15", "Addr")
                                            )
                                        ),
                                    ),
                                ],
                                response_type=StructDictDefn(
                                    name=Ident(
                                        symbol=Token(
                                            "__ANON_16", "UserBalanceForTokenResponse"
                                        )
                                    ),
                                    members=[
                                        TypeAssign(
                                            name=Ident(
                                                symbol=Token("__ANON_15", "balance")
                                            ),
                                            type=Typename(
                                                name=Ident(
                                                    symbol=Token("__ANON_15", "Uint128")
                                                )
                                            ),
                                        )
                                    ],
                                ),
                                body=[
                                    StructDictVal(
                                        name=Ident(
                                            symbol=Token(
                                                "__ANON_16",
                                                "UserBalanceForTokenResponse",
                                            )
                                        ),
                                        members_vals=StructDictAssign(
                                            name=Ident(
                                                symbol=Token("__ANON_15", "balance")
                                            ),
                                            value=TableLookupExpr(
                                                item=TableLookupExpr(
                                                    item=TableLookupExpr(
                                                        item=MemberAccessExpr(
                                                            item=Ident(
                                                                symbol=Token(
                                                                    "__ANON_15",
                                                                    "$state",
                                                                )
                                                            ),
                                                            member=Ident(
                                                                symbol=Token(
                                                                    "__ANON_15",
                                                                    "token_balances",
                                                                )
                                                            ),
                                                        ),
                                                        key=Ident(
                                                            symbol=Token(
                                                                "__ANON_15", "user"
                                                            )
                                                        ),
                                                    ),
                                                    key=Ident(
                                                        symbol=Token(
                                                            "__ANON_15", "token"
                                                        )
                                                    ),
                                                ),
                                                key=Integer(
                                                    value=Token("__ANON_19", "1")
                                                ),
                                            ),
                                        ),
                                    )
                                ],
                            )
                        ]
                    ),
                ],
            )
        )
    ]
)
